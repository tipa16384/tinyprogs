# Fortune League

# HE Mystic, I Defiler, DE Necro
from random import shuffle, choice, random
import curses
import csv
import numpy
import time

bparty = ['Human Monk',
         'Kerran Monk',
         'Darkelf Assassin',
         'Halfelf Dirge',
         'Ratonga Dirge',
         'Highelf Templar']

party = ['Human Monk',
         'Kerran Monk',
         'Darkelf Assassin',
         'Darkelf Dirge',
         'Ratonga Dirge',
         'Highelf Templar']

characters = []
maxv = 31224
trxfee = 20
maxtrades = 6

quitFlag = False

class PartyMember:
  def __init__(self,arch,clazz,score,price):
    self.arch = arch
    self.clazz = clazz
    self.score = score
    self.price = price

class Party:
  def __init__(self):
    self.score = None
    self.chars = []
  def append(self,c):
    self.chars.append(c)
  def scoreParty(self):
    if self.score is not None:
      return self.score
    z = {'Fighter':0,'Mage':0,'Scout':0,'Priest':0}
    score = 0.0
    price = 0
    wallet = maxv
    for c in self.chars:
      if c.clazz not in party:
        wallet -= trxfee
      z[c.arch] += 1
      score += c.score
      price += c.price
    for k in z.keys():
      if z[k] > 3:
        score = 0.0
    if score > 0 and price > wallet:
      score = 0.0
    if score > 0 and len(set(self.chars)) != 6:
      score = 0.0
    if score > 0 and not legacy(self.chars):
      score = 0.0
    self.score = score
    return score
  def value(self):
    return sum([c.price for c in self.chars])

def num(x):
  if x is None or len(x) == 0:
    return 0.0
  return float(x.replace(',',''))

def rowval(row,key):
  try:
    val = num(row[key])
  except KeyError:
    val = 0.0
  return val

def readCharacters():
  characters = []
  fn = '/cygdrive/c/Users/brenda/Downloads/Fortune League.csv'
  f = open(fn,'r')
  rdr = csv.DictReader(f,delimiter=',',quotechar='"')
  now = today()
  for row in rdr:
    #print row
    arch = row['ARCH']
    clazz = row['CLASS']
    price = rowval(row,'PRICE')
    score = 0.0
    
    buff = rowval(row,'BUFF')
    hate = rowval(row,'HATE')
    dmgp = rowval(row,'DMG-P')
    debff = rowval(row,'DEBFF')

    dmgaoe = rowval(row,'DMG-AOE')
    dmgpet = rowval(row,'DMG-PET')
    heal = rowval(row,'HEAL')
    dths = rowval(row,'DTHS')

    dmgm = rowval(row,'DMG-M')

    mdebff = 1.0
    mdmgp = 1.0
    mbuff = 1.0
    mhate = 1.0
    
    mdmgaoe = 1.0
    mdmgpet = 1.0
    mheal = 1.0
    mdths = 1.0
    
    mdmgm = 1.0

#    if now <= pdate('5/02/11'):
#      if arch == 'Mage':
#        mdmgpet = 0.3
    
#    if now <= pdate('5/02/11'):
#      if clazz == 'Arasai Warlock':
#        mdmgaoe = 0.5
    
    if dmgp > 0: score += (mdmgp*dmgp)/3333333.0
    if dmgm > 0: score += (mdmgm*dmgm)/3333333.0
    if hate > 0: score += (mhate*hate)/500000000.0
    if buff > 0: score += (mbuff*buff) / 1430.0
    if debff > 0: score += (mdebff*debff) / 500.0
    
    if dmgaoe > 0: score += (mdmgaoe*dmgaoe)/500000.0
    if dmgpet > 0: score += (mdmgpet*dmgpet)/1000000.0
    if heal > 0: score += (mheal*heal)/1000000.0
    if dths > 0: score += 500 - (mdths*dths)

    #print clazz,score
    p = PartyMember(arch,clazz,score,price)
    characters.append(p)
  return characters

def today():
  tt = time.localtime(time.time())
  return time.mktime((tt[0],tt[1],tt[2],0,0,0,0,0,0))

def pdate(sdate):
  tt = time.strptime(sdate,'%m/%d/%y')
  return time.mktime((tt[0],tt[1],tt[2],0,0,0,0,0,0))

class Screen:
  def __init__(self,characters):
    h,w = (24,80)
    self.colwidth = min(20,w/3)
    self.chrs = characters
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
    tscore = 0.0
    tprice = 0.0
    for s in self.sells:
      c = getCharacter(self.chrs,s)
      print "%4s %5d %5d %s" % ('SELL',int(c.score),int(c.price),s)
    for s in self.buys:
      c = getCharacter(self.chrs,s)
      tscore += c.score
      tprice += c.price
      print "%4s %5d %5d %s" % ('BUY',int(c.score),int(c.price),s)
    for s in self.keeps:
      c = getCharacter(self.chrs,s)
      print "%4s %5d %5d %s" % ('KEEP',int(c.score),int(c.price),s)
      tscore += c.score
      tprice += c.price
    print "%4s %5d %5d %s" % (' ',int(tscore),int(tprice),'TOTAL')
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
    
def quit(scr):
  return False

def legacy(pcs):
  if maxtrades >= 6: return True
  scum = len([c for c in pcs if c.clazz in party])
  #scum = len([c for c in pcs if c.clazz in oldparty])
  return scum >= (6-maxtrades)
  
def originalParty():
  p = Party()
  for c in characters:
    if c.clazz in party:
      p.append(c)
  return p

def ranParty(parties):
  scores = [p.scoreParty() for p in parties]
  sm = sum(scores)*random()
  for i in range(len(scores)):
    sm -= scores[i]
    if sm <= 0.0:
      return parties[i]
  return choice(parties)

def getInitialPopulation(characters,popSize):
  parties = []
  for i in range(popSize):
    p = Party()
    for pi in range(6):
      p.append(choice(characters))
    parties.append(p)
  return parties

def getNewPopulation(characters,popSize,oldParties):
  parties = []
  for i in range(popSize):
    if random() < 0.01:
      pm = characters
    else:
      p1 = ranParty(oldParties)
      p2 = ranParty(oldParties)
      pm = p1.chars + p2.chars
    p = Party()
    for j in range(6):
      p.append(choice(pm))
    parties.append(p)
  return parties

def getCharacter(characters,clazz):
  for c in characters:
    if c.clazz == clazz:
      return c
  return None

def genes(parties):
  genemap = {}
  for p in parties:
    if p.scoreParty > 0.0:
      for c in p.chars:
        s = c.clazz
        if s in genemap:
          genemap[s] += 1
        else:
          genemap[s] = 1

  return genemap

characters = readCharacters()
popSize = 500

print len(characters),"characters read"

scr = Screen(characters)

parties = getInitialPopulation(characters,popSize)

bestParty = originalParty()
bestScore = bestParty.scoreParty()
bestavg = 0
beststd = 10000

print "  starting score was",bestScore
print "  starting value was",bestParty.value()

for i in range(500):
  for t in parties:
    score = t.scoreParty()
    if score > bestScore:
      scr.newParty()
      bestParty = t
      bestScore = score
      newparty = [c.clazz for c in t.chars]
      for p in party:
        if p not in newparty:
          scr.addSell(p)
      for c in t.chars:
        if c.clazz in party:
          scr.addKeep(c.clazz)
        else:
          scr.addBuy(c.clazz)
      scr.addScore("  %d score: %f %d" % (i,bestScore,sum([c.price for c in t.chars])))
      scores = [w.scoreParty() for w in parties if w.scoreParty() > 0]
      pavg = numpy.average(scores)
      pstd = numpy.std(scores)
      print "gen:%d avg:%f std:%f" % (i,pavg,pstd)
      scr.partyDone()
  parties = getNewPopulation(characters,popSize,parties)
  
  if bestParty is not None:
    parties.append(bestParty)
    for j in range(6):
      np = Party()
      for c in bestParty.chars:
        np.append(c)
      np.chars[j] = choice(characters)
      parties.append(np)

scr.stop()

genemap = genes(parties)
g = []

for k in genemap.keys():
  g.append((genemap[k],k))

g.sort()
g.reverse()

for gg in g[:20]:
  print '%5d %s' % gg
