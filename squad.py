#/usr/bin/python

from itertools import combinations

maxdiff = 10000
best = 'Nobody'
bestZeroes = 0
bestTraining = None
trainingPoints = 280

def countLabels(squad, tag):
	return sum([1 for x in squad if tag in x.getLabels()])

class Recruit():
	def __init__(self, name, phys, ment, tact, labels='', chemistry='', effect=''):
		self.name = name
		self.phys = phys
		self.ment = ment
		self.tact = tact
		self.labels = labels
		self.chemistry = chemistry
		self.effect = effect
	
	def __str__(self):
		return "{} ({},{},{})".format(self.name,self.phys,self.ment,self.tact)
	
	def __repr__(self):
		return self.name
	
	def getName(self):
		return self.name
	
	def getLabels(self):
		return self.labels

	def getChemistry(self):
		return self.chemistry

	def getPhys(self, squad=None):
		if squad:
			return self.getStat('phys', lambda x: x.getPhys(), squad)
		return self.phys

	def getMent(self, squad=None):
		if squad:
			return self.getStat('ment', lambda x: x.getMent(), squad)
		return self.ment

	def getTact(self, squad=None):
		if squad:
			return self.getStat('tact', lambda x: x.getTact(), squad)
		return self.tact
	
	def getStat(self, stat, statter, squad=None):
		bonus = 0
		if squad and stat in self.effect:
			toks = self.chemistry.split(' ')
			#print "Chemistry",toks
			count = countLabels(squad, toks[0])
			if toks[1] == '<' and count < int(toks[2]):
				ineffect = True
			elif toks[1] == '>' and count > int(toks[2]):
				ineffect = True
			else:
				ineffect = False;
			if ineffect:
				toks = self.effect.split(' ')
				bonus = statter(self) * float(toks[2])
				#print "applying bonus",bonus
		return statter(self) + bonus

def getTraining(trainingPoints):
	increment = 20
	for phys in range(0,trainingPoints+increment,increment):
		for ment in range(0,trainingPoints+increment,increment):
			if phys + ment > trainingPoints:
				break
			yield Recruit('Training', phys, ment, trainingPoints - phys - ment)

def mission(xyz,training):
	global maxdiff, best, bestZeroes, bestTraining
	
	phys = sum([x.getPhys(xyz) for x in xyz])
	ment = sum([x.getMent(xyz) for x in xyz])
	tact = sum([x.getTact(xyz) for x in xyz])
	
	dphys = max(0,goal.getPhys() - training.getPhys() - phys)
	dment = max(0,goal.getMent() - training.getMent() - ment)
	dtact = max(0,goal.getTact() - training.getTact() - tact)
	
	#print xyz, dphys, dment, dtact

	diff = dphys + dment + dtact
	zeroes = sum([1 for z in [dphys, dment, dtact] if not z])
	
	if zeroes < bestZeroes:
		return
	elif zeroes > bestZeroes:
		maxdiff = 10000
	bestZeroes = zeroes
	if diff < maxdiff:
		best = xyz
		maxdiff = diff
		bestTraining = training
		print dphys,dment,dtact,best,diff,zeroes,training

squad = [
	Recruit('Cecily', 26, 120, 34, 'Hyur Conjurer', 'Conjurer < 4', 'score * 0.2'),
	Recruit('Nanasomi', 41, 26, 115, 'Lalafell Archer', 'Lancer > 0', 'score * 0.1'),
	Recruit('Hastaloeya', 112, 26, 46, 'Roegadyn Marauder', 'Roegadyn < 2', 'tact * 0.1'),
	Recruit('Elchi', 56, 25, 95, 'AuRa Lancer', 'Miqote > 0', 'score * 0.1'),
	Recruit('Totodi', 58, 35, 71, 'Lalafell Pugilist'),
	Recruit('Rivienne', 23, 114, 29, 'Elezen Conjurer', 'Lalafell > 0', 'score * 0.1'),
	Recruit('Sofine', 24, 84, 60, 'Elezen Arcanist'),
	Recruit('Saiun', 102, 24, 42, 'AuRa Marauder')
]

#goal = Recruit('Flagged Mission: Crystal Recovery', 315, 325, 340)
#goal = Recruit('Allied Maneuvers', 310, 480, 170)
goal = Recruit('Search and Rescue', 185, 310, 465)

for xyz in combinations(squad, 4):
	for training in getTraining(trainingPoints):
		mission(xyz, training)
		
print best,maxdiff,bestTraining
