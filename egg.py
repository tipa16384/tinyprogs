#!/usr/bin/python

class Egg:
	def __init__(self, name, order=0, eggs = {}):
		self.name = name
		self.order = order
		self.eggs = eggs
	
	def addEgg(self, eggarr):
		self.eggs.update(eggarr)
	
	def __str__(self):
		return "Egg({}, {})".format(self.name, self.eggs)
	
	def __repr__(self):
		return "Egg({}, {})".format(self.name, self.eggs)
	
	def list(self):
		x = {}
		self.rlist(x, self.eggs)
		title = "Making {}".format(self.name.upper())
		print title
		print '='*len(title)
		for e in sorted(x, key=lambda y: y.order):
			print "{}: {}".format(e.name,x[e])
		print
	
	def rlist(self, x, eg):
		for e in eg.keys():
			n = eg[e]
			if e in x:
				x[e] += n
			else:
				x[e] = n
			for i in range(n):
				self.rlist(x, e.eggs)

red = Egg('Red Egg')
blue = Egg('Blue Egg')
rainbow = Egg('Rainbow Egg',1)
mind = Egg('Crystal Egg of Mind',100)
power = Egg('Crystal Egg of Power',100)
chocolate = Egg('Chocolate Egg', 2, {red:10, blue:30})
great = Egg('Great Egg', 2, {red:30, blue:10})
magical = Egg('Magical Egg', 3, {chocolate:3, rainbow:5})
radiant = Egg('Radiant Egg', 3, {great:3, rainbow:5})
crown = Egg('Crown of Justice', 4, {magical:2})
bandana = Egg('Black Bandana', 4, {radiant:2, magical:2, rainbow:5})
staff = Egg('Staff of Wrath', 4, {radiant:2})
knife = Egg('Second Knife', 5, {staff:2, crown:1, bandana:1, power:1})
snap = Egg('Cold Snap', 5, {bandana:2, staff:1, mind:1})
veins = Egg('Icy Veins', 5, {staff:1, crown:1})

alleggs = [red, blue, rainbow, mind, power, chocolate, great, magical, radiant, crown, bandana, staff, knife, snap, veins]
roweggs = [x for x in alleggs if x.eggs]
roweggs = sorted(roweggs, key=lambda y: y.order, reverse=True)
coleggs = [x for x in alleggs if [y for y in alleggs if x in y.eggs]]
coleggs = sorted(coleggs, key=lambda y: y.order, reverse=False)

print ",{}".format(','.join(x.name for x in coleggs))
for x in roweggs:
	rx = {}
	x.rlist(rx, x.eggs)
	a = [x.name]
	for ae in coleggs:
		if ae in rx:
			a.append(str(rx[ae]))
		else:
			a.append('')
	print ','.join(a)


