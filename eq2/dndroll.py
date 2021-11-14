from random import randint
import sys
import os
import sqlite3

rollDb = 'roller.db'


# rulebook

rules = [('PHB','Player\'s Handbook'),
				 ('PHB2','Player\'s Handbook 2'),
				 ('PHB3','Player\'s Handbook 3')
				]

# stats
ss = 'STR'
sd = 'DEX'
si = 'INT'
sw = 'WIS'
sc = 'CON'
sa = 'CHA'

dac = "Armor Class"
dfort = "Fortitude"
dref = "Reflexes"
dwill = "Will"

sn = ''

stats = [ss,sd,sw,sc,si,sa]

# roles
rl = 'Leader'
rs = 'Striker'
rc = 'Controller'
rd = 'Defender'

roles = [rc,rd,rl,rs]

# power pools
pm = 'Martial'
pd = 'Divine'
pa = 'Arcane'
ps = 'Shadow'
py = 'Psionic'
pp = 'Primal'

# races
races = [
	('Dragonborn',{ss:2,sa:2}),
	('Dwarf',{sc:2,sw:2}),
	('Eladrin',{sd:2,si:2}),
	('Elf',{sd:2,sw:2}),
	('Half-Elf',{sc:2,sa:2}),
	('Halfling',{sd:2,sa:2}),
	('Human',{}),
	('Tiefling',{si:2,sa:2}),
		
# phb2 races
	('Deva',{si:2,sw:2}),
	('Gnome',{si:2,sa:2}),
	('Goliath',{ss:2,sc:2}),
	('Half-Orc',{ss:2,sd:2}),
	('Shifter-Tooth',{ss:2,sw:2}),
	('Shifter-Claw',{sd:2,sw:2})
]

lowbon = 8
highbon = 8

lowprime = 16
lowsec = 14
lowtert = 12

subs = {
	'TITLE': 'D&D 4e Character Roller 0.9',
	ss: '',
	si: '',
	sd: '',
	sw: '',
	sa: '',
	sc: '',
	'ARGS': '',
	'ROLE': '',
	'RACE': '',
	'BONUS': '',
	'LINK': '',
	'RULE': ''
}

class Defense:
	def __init__(self,name,mods):
		self.name = name
		self.mods = mods

class Class:
	classId = 1
	
	@classmethod
	def getClassId(cls):
		return cls.classId
	
	@classmethod
	def setClassId(cls,cid):
		cls.classId = cid
	
	def export(self):
		conn = sqlite3.connect(rollDb)
		
		try:
			c = conn.execute("create table CLASSES (classId int, name text, prime text, sec text, tert text, pool text, role text, hp int, surges int, rules text)")
			c = conn.execute("create table DEFS (classId int, def text, bonus int)")
		except sqlite3.OperationalError:
			pass
		
		c = conn.execute("insert into CLASSES values (?,?,?,?,?,?,?,?,?,?)", \
			(self.classId,self.name,self.prime,self.sec,self.tert,self.pool,self.role,self.hp,self.surges,self.rules))
		for k in self.defs:
			c = conn.execute("insert into DEFS values(?,?,?)",(self.classId,k,self.defs[k]))
		
		conn.commit()
		conn.close()
			
	def __init__(self,cid,name,prime,sec,tert,pool,role,hp,defs,surges,rules):
		self.classId = cid
		self.name = name
		self.prime = prime
		self.sec = sec
		self.tert = tert
		self.pool = pool
		self.role = role
		self.defs = defs
		self.hp = hp
		self.surges = surges
		self.rules = rules
  
	def __str__(self):
		return "%d %30s %3s %3s %3s %-10s %-10s" % (self.classId,self.name,self.prime,self.sec,self.tert,self.pool,self.role)

defenses = []

defenses.append(Defense(dac,[]))
defenses.append(Defense(dfort,[ss,sc]))
defenses.append(Defense(dref,[sd,si]))
defenses.append(Defense(dwill,[sw,sa]))

classes = []

def writeClasses(subs):
	for c in classes:
		c.export()

def loadClasses(subs):
	global classes

	classes = []
	rule = subs['RULE']
	role = subs['ROLE']
	args = []
	sql = []
	
	sql.append("select * from classes where 1 = 1")
	if rule:
		sql.append("and rules = ?")
		args.append(rule)
	if role:
		sql.append("and role = ?")
		args.append(role)
	sql.append("order by name")
	
	conn = sqlite3.connect(rollDb)
	if args:
		c = conn.execute(' '.join(sql),tuple(args))
	else:
		c = conn.execute(' '.join(sql))
		
	for d in c:
		cl = Class(d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7],{},d[8],d[9])
		dfs = conn.execute('select def, bonus from defs where classId = ?',(cl.classId,))
		for df in dfs:
			cl.defs[df[0]] = df[1]
		classes.append(cl)
	
	conn.close()


def getStats(subs):
	while True:
		s = {}

		if subs['LINK']:
			for i in range(len(stats)):
				s[stats[i]] = ord(subs['LINK'][i+3]) - ord('A')
			yield s
		else:
			for st in stats:
				s[st] = sum([randint(1,6) for i in range(3)])

			m = None
			for r, m1 in races:
				if r == subs['RACE']:
					m = m1
					break

			if not m:
				m = {subs['BONUS']:2}
		
			for st in m:
				s[st] += m[st]
		
			bon = sum([s[st]/2 - 5 for st in stats])

			if bon >= lowbon and bon <= highbon:
				yield s

def matchClasses(stats,subs):
	return [c for c in classes 
		if stats[c.prime] >= lowprime
		and stats[c.sec] >= lowsec
		and stats[c.tert] >= lowtert]

def getEnviron(subs):
	env = os.environ['QUERY_STRING'] if 'QUERY_STRING' in os.environ and os.environ['QUERY_STRING'] else ''
	try:
		params = dict([p.split('=') for p in env.split('&')])
		for p in params:
			v = params[p].replace('%28','(').replace('%29',')')
			subs[p] = v
	except:
		params = {}

	if not subs['RACE']:
		subs['RACE'] = 'Human'

	if not subs['BONUS']:
		subs['BONUS'] = ss
	
	subs['STATNAMES'] = stats
	
	if subs['LINK']:
		l = subs['LINK']
		subs['RACE'] = races[int(l[0])][0]
		
		rl = l[1]
		if l[1] == 'X':
			subs['ROLE'] = ''
		else:
			subs['ROLE'] = roles[int(rl)]
			
		subs['BONUS'] = stats[int(l[2])]
		
		try:
			subs['RULE'] = rules[int(l[9])][0]
		except Exception:
			subs['RULE'] = ''		
	
def getRoles(subs):
	return roles

def getMod(st):
	return st/2-5
	
def getRaces(subs):
	sr = []
	for r,s in races:
		if not s:
			s1 = 'Choose'
		else:
			s1 = ','.join(["%s:%+d" % (sv,s[sv]) for sv in s])
		sr.append((r,s1))
	return sr

def getBonus(subs):
	return subs['BONUS']

def getDefenses(subs):
	df = []
	for d in defenses:
		if d.mods:
			s = sum([getMod(subs[s]) for s in d.mods])
			v = 10+s
			m = "%+d" % (s)
		else:		# ac - bonus only with no or light armor
			v = 10
			m1 = getMod(subs[sd])/2
			m2 = getMod(subs[si])/2
			m = "%+d" % ((max(m1,m2)))
		df.append((d.name,m,v))
	return df

def getRules(subs):
	return rules

def getLinkURL(subs):
	l = []
	
	raceIndex = 0
	for i in range(len(races)):
		if races[i][0] == subs['RACE']:
			raceIndex = i
			break
	l.append(str(raceIndex))
	
	if not subs['ROLE']:
		l.append('X')
	else:
		l.append(str(roles.index(subs['ROLE'])))
	
	l.append(str(stats.index(subs['BONUS'])))
	
	for s in stats:
		l.append(chr(subs[s]+ord('A')))
	
	ruleIndex = 'X'
	for i in range(len(rules)):
		if rules[i][0] == subs['RULE']:
			ruleIndex = str(i)
			break
	l.append(ruleIndex)

	return 'http://chasingdings.com/cgi-bin/roller.py?LINK=%s' % (''.join(l))
