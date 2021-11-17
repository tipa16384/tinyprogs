#!/usr/bin/python

import re
import sys

races = ['AURA', 'LALAFELL', 'MIQOTE', 'ROEGADYN', 'HYUR', 'ELEZEN']
jobs = ['CONJURER', 'ARCANIST', 'LANCER', 'ARCHER', 'THAUMATURGE', 'ROGUE', 'WARRIOR', 'GLADIATOR', 'PUGILIST']

def affinityLog(rule, scrub, ability, increase, bonus):
	scrub.setActiveAffinity('{} matched affinity {} bonus of {}'.format(scrub.getName(), rule, bonus))
	#print scrub.getActiveAffinity()

def activeSquadron(scrub, squad, goal, m, affinitybonus):
	ability = m.group(1)
	increase = float(m.group(2))/100.0
	
	bonus = decodeAbility(ability, increase, affinitybonus)
	
	affinityLog('activeSquadron', scrub, ability, increase, bonus)
	
	return bonus

def accompanying(scrub, squad, goal, m, affinitybonus):
	ability = m.group(2)
	increase = float(m.group(3))/100.0
	label = m.group(1).upper()
	
	earned = True if affinitybonus > 1.0 else False
	bonus = (1.0,1.0,1.0)

	for x in squad:
		if x.getName() != scrub.getName():
			if label in x.getLabels().upper():
				earned = True
				break
	
	if earned:
		bonus = decodeAbility(ability, increase, affinitybonus)
		affinityLog('accompanying', scrub, ability, increase, bonus)

	return bonus

def notaccompanying(scrub, squad, goal, m, affinitybonus):
	ability = m.group(1)
	increase = float(m.group(2))/100.0

	# find own race
	race = None
	
	for x in scrub.getLabels().upper().split():
		if x in races:
			race = x
			break
	
	if not race:
		print "No race found for",scrub
		sys.exit(1)

	earned = True if affinitybonus > 1.0 else False
	bonus = (1.0,1.0,1.0)

	if not earned:
		earned = True
		for x in squad:
			if x.getName() != scrub.getName():
				if race in x.getLabels().upper():
					earned = False
					break

	if earned:
		bonus = decodeAbility(ability, increase, affinitybonus)
		affinityLog('notaccompanying', scrub, ability, increase, bonus)
	
	return bonus

def differentRace(scrub, squad, goal, m, affinitybonus):
	"no dupes among squad races"
	
	ability = m.group(1)
	increase = float(m.group(2))/100.0
	
	raceCount = {}
	for r in races:
		raceCount[r] = 0
	
	for s in squad:
		for r in races:
			if r in s.getLabels().upper():
				raceCount[r] += 1
				break
	
	earned = True
	bonus = (1.0,1.0,1.0)
	
	#print "races",raceCount,squad
	
	for r in raceCount:
		if raceCount[r] > 1:
			earned = False
			break
	
	if earned:
		bonus = decodeAbility(ability, increase, affinitybonus)
		affinityLog('differentRace', scrub, ability, increase, bonus)
	
	return bonus

def samerace(scrub, squad, goal, m, affinitybonus):
	"someone else in squad of same race"
	ability = m.group(1)
	increase = float(m.group(2))/100.0

	# find own class
	race = None
	
	for x in scrub.getLabels().upper().split():
		if x in races:
			race = x
			break
	
	if not race:
		print "No race found for", scrub
		sys.exit(1)

	earned = True if affinitybonus > 1.0 else False
	bonus = (1.0,1.0,1.0)
		
	for x in squad:
		if x.getName() != scrub.getName():
			if race in x.getLabels().upper():
				earned = True
				break

	if earned:
		bonus = decodeAbility(ability, increase, affinitybonus)
		affinityLog('sameclass', scrub, ability, increase, bonus)
	
	return bonus

def sameclass(scrub, squad, goal, m, affinitybonus):
	ability = m.group(1)
	increase = float(m.group(2))/100.0

	# find own class
	job = None
	
	for x in scrub.getLabels().upper().split():
		if x in jobs:
			job = x
			break
	
	if not job:
		print "No job found for", scrub
		sys.exit(1)

	earned = True if affinitybonus > 1.0 else False
	bonus = (1.0,1.0,1.0)
		
	for x in squad:
		if x.getName() != scrub.getName():
			if job in x.getLabels().upper():
				earned = True
				break

	if earned:
		bonus = decodeAbility(ability, increase, affinitybonus)
		affinityLog('sameclass', scrub, ability, increase, bonus)
	
	return bonus

def manysameclass(scrub, squad, goal, m, affinitybonus):
	ability = m.group(2)
	increase = float(m.group(3))/100.0
	howmany = int(m.group(1))

	counts = {}
	for j in jobs:
		counts[j] = 0
		
	for j in jobs:
		for x in squad:
			if j in x.getLabels().upper():
				counts[j] += 1
				break

	earned = False
	for c in counts:
		if counts[c] >= howmany:
			earned = True
			break

	bonus = (1.0,1.0,1.0)
		
	if earned:
		bonus = decodeAbility(ability, increase, affinitybonus)
		affinityLog('manysameclass', scrub, ability, increase, bonus)
	
	return bonus

def nobonus(scrub, squad, goal, m, affinitybonus):
	return (1.0,1.0,1.0)
	
def decodeAbility(ability, increase, affinitybonus):
	p = 1.0
	m = 1.0
	t = 1.0
	
	if ability == 'physical ability':
		p += increase * affinitybonus
	elif ability == 'mental ability':
		m += increase * affinitybonus
	elif ability == 'tactical ability':
		t += increase * affinitybonus
	
	return (p,m,t)
	
affinityPatterns = [
	(u'^When an active squadron member\, (.+) (?:is increased|increase) by (\d+)\%.?$', activeSquadron),
	(u'^When accompanying (?:a|an) (.*)\, (.+) (?:is increased|increase) by (\d+)\%.?$', accompanying),
	(u'^When accompanying (?:a|an) (.*)\, there is a (\d+)\% chance to receive (.+).?$', nobonus),
	(u'^When not accompanying someone of the same race, (.+) (?:is increased|increase) by (\d+)\%.?$', notaccompanying),
	(u'^When accompanying someone of the same class, (.+) (?:is increased|increase) by (\d+)\%.?$', sameclass),
	(u'^When accompanying someone of the same race, (.+) (?:is increased|increase) by (\d+)\%.?$', samerace),
	(u'^When accompanying someone of the same class, there is a (\d+)\% chance to receive (.+).?$', nobonus),
	(u'^When all squadron members are of a different race, (.+) (?:is increased|increase) by (\d+)\%.?$', differentRace),
	(u'^When (\d+) or more members are of the same class, (.+) (?:is increased|increase) by (\d+)\%.?$', manysameclass),
	(u'^When above level 50, there is a (\d+)\% chance to receive (.+).?$', nobonus),
	(u'^$', nobonus)
]

def decodeAffinity(scrub, squad, goal, affinitybonus):
	chem = scrub.getFullChemistry()
	
	found = False
	func = None
	
	for p in affinityPatterns:
		m = re.match(p[0], chem)
		if m and p[1]:
			func = p[1]
			found = True
			break

	if not found:
		print "Could not find",scrub,chem
		sys.exit(1)

	return func(scrub, squad, goal, m, affinitybonus)
	
class Recruit():
	def __init__(self, name, level, phys, ment, tact, labels='', fullchemistry=''):
		self.name = name
		self.level = level
		self.phys = phys
		self.ment = ment
		self.tact = tact
		self.physbonus = 1.0
		self.mentbonus = 1.0
		self.tactbonus = 1.0
		self.labels = labels
		self.fullchemistry = fullchemistry
		self.activeaffinity = ''
		self.history = []
		
	def __eq__(self, other):
		#print "Compare {} to {}".format(self, other)
		if self.phys != other.phys:
			return False
		if self.ment != other.ment:
			return False
		if self.tact != other.tact:
			return False
		return True
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __str__(self):
		return "{} ({},{},{})".format(self.name,self.phys,self.ment,self.tact)
	
	def __repr__(self):
		return self.name
	
	def setActiveAffinity(self, affine):
		self.activeaffinity = affine
	
	def getActiveAffinity(self):
		return self.activeaffinity
	
	def getName(self):
		return self.name
	
	def getLevel(self):
		return self.level
	
	def getLabels(self):
		return self.labels

	def getHistory(self):
		return self.history
	
	def setHistory(self, history):
		self.history = history
	
	def getFullChemistry(self):
		return self.fullchemistry
	
	def setFullChemistry(self, fullchemistry):
		self.fullchemistry = fullchemistry
	
	def setGoal(self, squad, goal):
		self.activeaffinity = ''
		affinitybonus = 2.0 if self.getAffinity(goal) else 1.0
		self.physbonus, self.mentbonus, self.tactbonus = decodeAffinity(self, squad, goal, affinitybonus)
		if self.activeaffinity and affinitybonus == 2.0:
			self.activeaffinity = '{} - MAX AFFINITY'.format(self.activeaffinity)
	
	def getAffinity(self, goal):
		if not goal or not self.labels or not goal.getLabels():
			return False
		toks = self.labels.split(' ')
		affinities = goal.getLabels().split(' ')
		return len([t for t in toks if t in affinities]) > 0

	def getPhys(self, squad=None, goal=None):
		return self.phys * self.physbonus

	def getMent(self, squad=None, goal=None):
		return self.ment * self.mentbonus

	def getTact(self, squad=None, goal=None):
		return self.tact * self.tactbonus
	
	def toDict(self, type):
		dict = {}

		dict['type'] = type
		dict['name'] = self.name
		dict['level'] = self.level
		dict['physical'] = self.phys
		dict['mental'] = self.ment
		dict['tactical'] = self.tact
		dict['labels'] = self.labels
		dict['fullchemistry'] = self.fullchemistry
		return dict

def countLabels(squad, tag):
	return sum([1 for x in squad if tag in x.getLabels()])
