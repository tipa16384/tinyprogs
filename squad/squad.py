#!/usr/bin/python

import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from itertools import combinations
from recruit import Recruit
import sys

trainingPoints = 400
maxTraining = 6

dividerSquad = 'Squad'
dividerMission = 'Missions'
dividerTraining = 'Initial Training'

squad = []
goals = []
initialTraining = None

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1VYxKi_1jk1zm0F5tCT0BDaFUaBm6jAr9GEacl1c7GwE'
SAMPLE_RANGE_NAME = 'squad!A2:J'

def validTraining(training, trainingPoints):
	#print 'testing',training,trainingPoints
	
	p = training.getPhys()
	m = training.getMent()
	t = training.getTact()
	
	if (p + m + t) > trainingPoints:
		#print p,m,t,'greater than',trainingPoints
		return False
	
	if p < 0 or m < 0 or t < 0:
		#print p,m,t,'something feels negative'
		return False
	
	return True

def testtrainingtype(expected, actual):
	if expected != actual:
		print ("expected '{}', got '{}'".format(expected, actual))
		sys.exit(1)

def variant(trainingPoints, newName, newLevel, opt, pbonus, mbonus, tbonus, trainingtype):
	tot = opt.getPhys() + pbonus + opt.getMent() + mbonus + opt.getTact() + tbonus
	
	if tot > trainingPoints:
		if pbonus == 40:
			mbonus = -20
			tbonus = -20
			testtrainingtype('P', trainingtype)
		elif pbonus == 20:
			if mbonus == 20:
				testtrainingtype('PM', trainingtype)
				tbonus = -20
			else:
				testtrainingtype('PT', trainingtype)
				mbonus = -20
		elif mbonus == 40:
			testtrainingtype('M', trainingtype)
			pbonus = -20
			tbonus = -20
		elif mbonus == 20:
			testtrainingtype('MT', trainingtype)
			pbonus = -20
		else:
			testtrainingtype('T', trainingtype)
			pbonus = -20
			mbonus = -20
	
	return Recruit(newName, newLevel, opt.getPhys()+pbonus, opt.getMent()+mbonus, opt.getTact()+tbonus, trainingtype)

def getTraining(initialTraining,trainingPoints):
	options = [initialTraining]
	optIndex = 0
	optLen = 1
	
	while optIndex < optLen:
		opt = options[optIndex]
		optIndex += 1
		yield opt
		
		# max of three training sessions
		if opt.getLevel() > maxTraining:
			continue
		
		newLevel = opt.getLevel()+1
		newName = 'Training {}'.format(newLevel)
		
		variants = []
		variants.append(variant(trainingPoints, newName, newLevel, opt, 40, 0, 0, 'P'))
		variants.append(variant(trainingPoints, newName, newLevel, opt, 0, 40, 0, 'M'))
		variants.append(variant(trainingPoints, newName, newLevel, opt, 0, 0, 40, 'T'))
		variants.append(variant(trainingPoints, newName, newLevel, opt, 20, 20, 0, 'PM'))
		variants.append(variant(trainingPoints, newName, newLevel, opt, 20, 0, 20, 'PT'))
		variants.append(variant(trainingPoints, newName, newLevel, opt, 0, 20, 20, 'MT'))
		
		for v in variants:
			if validTraining(v, trainingPoints) and v not in options:
				v.setHistory(opt.getHistory() + [opt])
				options.append(v)
		
		optLen = len(options)

def mission(xyz, training, initialTraining, goal, goalZeroes):
	for x in xyz:
		x.setGoal(xyz, goal)
	
	phys = sum([x.getPhys(xyz, goal) for x in xyz])
	ment = sum([x.getMent(xyz, goal) for x in xyz])
	tact = sum([x.getTact(xyz, goal) for x in xyz])
	
	dphys = max(0,goal.getPhys() - training.getPhys() - phys)
	dment = max(0,goal.getMent() - training.getMent() - ment)
	dtact = max(0,goal.getTact() - training.getTact() - tact)
	
	diff = dphys + dment + dtact
	zeroes = sum([1 for z in [dphys, dment, dtact] if not z])
	
	if zeroes == goalZeroes:
		affinities = [x.getActiveAffinity() for x in xyz if x.getActiveAffinity()]
		return (xyz,training,diff,affinities)
	else:
		return None
		
def trainingDistance(t1,t2):
	p = t1.getPhys() - t2.getPhys()
	m = t1.getMent() - t2.getMent()
	t = t1.getTact() - t2.getTact()
	return pow(pow(p,2)+pow(m,2)+pow(t,2), 0.5)

def getWins(initialTraining, goal, goalZeroes = 3):
	platoon = [x for x in squad if x.getLevel() >= goal.getLevel()]
	
	for xyz in combinations(platoon, 4):
		for training in getTraining(initialTraining, trainingPoints):
			win = mission(xyz, training, initialTraining, goal, goalZeroes)
			if win:
				yield win

def wincmp(a,b):
	global initialTraining
	res = int(round(a[2] - b[2]))
	if res:
		return res
	dist = int(round(trainingDistance(a[1], initialTraining) - trainingDistance(b[1], initialTraining)))
	if dist:
		return dist
	return sum([x.getLevel() for x in a[0]]) - sum([x.getLevel() for x in b[0]])

def readData():
	global initialTraining, goals, squad
	
	"""Shows basic usage of the Sheets API.
	Prints values from a sample spreadsheet.
	"""
	creds = None
	# The file token.pickle stores the user's access and refresh tokens, and is
	# created automatically when the authorization flow completes for the first
	# time.
	if os.path.exists('token.pickle'):
		with open('token.pickle', 'rb') as token:
			creds = pickle.load(token)
	# If there are no (valid) credentials available, let the user log in.
	if not creds or not creds.valid:
		if creds and creds.expired and creds.refresh_token:
			creds.refresh(Request())
		else:
			flow = InstalledAppFlow.from_client_secrets_file(
				'credentials.json', SCOPES)
			creds = flow.run_local_server()
		# Save the credentials for the next run
		with open('token.pickle', 'wb') as token:
			pickle.dump(creds, token)

	service = build('sheets', 'v4', credentials=creds)

	# Call the Sheets API
	sheet = service.spreadsheets()
	result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
							range=SAMPLE_RANGE_NAME).execute()
	values = result.get('values', [])

	if not values:
		print('No data found.')
		sys.exit(1)
	
	for srow in values:
		if not srow or not srow[0]:
			break
		
		row = ['' for x in range(10)]
		for x in range(len(srow)):
			row[x] = srow[x]
		
		rec = Recruit(row[1], int(row[2]), int(row[3]), int(row[4]), 
			int(row[5]), row[6], row[7])
		type = row[0]
		
		if type == dividerTraining:
			initialTraining = rec
		elif type == dividerSquad:
			squad.append(rec)
		elif type == dividerMission:
			goals.append(rec)

def main():
	readData()
			
	goals.sort(key = lambda x: x.getLevel(), reverse = True)

	mvp = {}
	for s in squad:
		mvp[s.getName()] = 0

	for goal in goals:
		totalVictory = True
		for goalZeroes in range(3,1,-1):
			wins = [win for win in getWins(initialTraining, goal, goalZeroes)]
			if wins:
				break
			totalVictory = False
	
		if wins:
			print ("Lv.{} mission: {}".format(goal.getLevel(), goal.getName()))
			if totalVictory:
				print ("   TOTAL VICTORY!!!!!!!!!!!")
			if goal.getLabels():
				print ("   Affinities: {}".format(goal.getLabels()))
			wins.sort(cmp = wincmp)
		
			for win in wins:
				if goal.getLevel() >= 50:
					for x in win[0]:
						mvp[x.getName()] += 1
				print ("   Best training: Physical={}, Mental={}, Tactical={} Diff={} Effort={}".format(
					win[1].getPhys(),win[1].getMent(),win[1].getTact(), win[2], win[1].getLevel()))
				if win[1].getHistory():
					for h in win[1].getHistory():
						print ("      {} {}".format(h, h.getLabels()))
				for x in win[3]:
					print ("   Affinity: {}".format(x))
				print ("   Best team of {}: {}".format(len(wins), ', '.join([x.getName()+' ('+str(x.getLevel())+')' for x in win[0]])))
				break
			print()

	print ("MVPs:")
	print()

	squadScore = [(mvp[s],s) for s in mvp]
	squadScore.sort(reverse = True)

	for score, name in squadScore:
		print ('{:4} {}'.format(score, name))

if __name__ == '__main__':
    main()

