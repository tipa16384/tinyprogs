# Fortune League

# HE Mystic, I Defiler, DE Necro
from random import shuffle
import curses
import csv

class PartyMember:
  def __init__(self,arch,clazz,score,price):
    self.arch = arch
    self.clazz = clazz
    self.score = score
    self.price = price

def num(x):
  if x is None or len(x) == 0:
    return 0.0
  return float(x.replace(',',''))

def readCharacters():
  characters = []
  fn = '/cygdrive/c/Users/brenda/Downloads/Fortune League.csv'
  f = open(fn,'r')
  rdr = csv.DictReader(f,delimiter=',',quotechar='"')
  for row in rdr:
    print row
    arch = row['ARCH']
    clazz = row['CLASS']
    price = num(row['PRICE'])
    score = 0.0
    
    hate = num(row['HATE'])
    dths = num(row['DTHS'])
    buff = num(row['BUFF'])
    heal = num(row['HEAL'])
    
    if clazz == 'Dwarf Templar':
      heal *= 3.5
    if clazz == 'Darkelf Coercer':
      buff *= 2
    
    if hate > 0:
      score += hate/500000000.0/8.0
    if dths > 0:
      score += 500 - dths/8.0
    if buff > 0:
      score += buff/1430.0/8.0
    if heal > 0:
      score += heal/1000000.0/8.0
    
    p = PartyMember(arch,clazz,score,int(row['PRICE']))
    characters.append(p)
  return characters
  
class Screen:
  def __init__(self):
    h,w = (24,80)
    self.colwidth = min(20,w/3)
  def stop(self):
    pass
  def colheader(self,col,head):
    pass
  def newParty(self):
    self.colheader(0,"SELL")
    self.colheader(1,"BUY")
    self.colheader(2,"KEEP")
    self.sells = []
    self.buys = []
    self.keeps = []
    self.score = 'no score'
  def partyDone(self):
    for s in self.sells:
      print " SELL",s
    for s in self.buys:
      print "  BUY",s
    for s in self.keeps:
      print " KEEP",s
    print self.score
    print
  def addLine(self,s,col,y):
    x = col*self.colwidth+(self.colwidth-len(s))/2
    self.w.addstr(y,x,s)
  def addSell(self,s):
    self.sells.append(s)
  def addBuy(self,s):
    self.buys.append(s)
  def addKeep(self,s):
    self.keeps.append(s)
  def addScore(self,s):
    self.score = s
    
party = ['Ogre Ranger',
         'Highelf Templar',
         'Dwarf Templar',
         'Human Monk',
         'Kerran Monk',
         'Halfelf Defiler']

oldparty = ['Highelf Mystic',
          'Halfelf Defiler',
          'Darkelf Necro']

characters = []
maxv = 32231

quitFlag = False

def quit(scr):
  return False

def legacy(pcs):
  scum = len([c for c in pcs if c.clazz in party])
  #scum = len([c for c in pcs if c.clazz in oldparty])
  return scum >= 0
  
def originalParty():
  return [c for c in characters if c.clazz in party]

def scoreParty(pcs):
  z = {'Fighter':0,'Mage':0,'Scout':0,'Priest':0}
  score = 0.0
  price = 0
  wallet = maxv
  for c in pcs:
    if c.clazz not in party:
      wallet -= 20
    z[c.arch] += 1
    score += c.score
    price += c.price
  for k in z.keys():
    if z[k] > 3:
      score = 0.0
  if price > wallet:
    score = 0.0
  if len(set(pcs)) != 6:
    score = 0.0
  return score

characters = readCharacters()

bestParty = []
bestScore = 0.0
print len(characters),"characters read"

scr = Screen()

for i in range(2000000):
  if quit(scr): break
  shuffle(characters)
  t = characters[:6]
  if not legacy(t): continue
  score = scoreParty(t)
  if score > bestScore:
    scr.newParty()
    bestParty = t
    bestScore = score
    newparty = [c.clazz for c in t]
    for p in party:
      if p not in newparty:
        scr.addSell(p)
    for c in t:
      if c.clazz in party:
        scr.addKeep(c.clazz)
      else:
        scr.addBuy(c.clazz)
    scr.addScore("  %d score: %f %d" % (i,bestScore,sum([c.price for c in t])))
    scr.partyDone()

print "  starting score was",scoreParty(originalParty())

scr.stop()
