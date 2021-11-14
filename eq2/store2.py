#!/usr/bin/python

# discount rate. 0=no discount, 1=free
discount = 0.01     # 1% discount
tax = 1.1           # broker tax

def toGold(x):
  a = []
  if x >= 100.0:
    p = int(x/100)
    x -= p * 100
    a.append('%dp' % (p))
  if x >= 1.0:
    g = int(x)
    x -= g
    a.append('%dg' % (g))
  if x >= 0.01:
    s = int(x*100.0)
    x -= float(s)/100.0
    a.append('%ds' % (s))
  if x >= 0.0001:
    c = int(x*10000.0)
    x -= float(c)/10000.0
    a.append('%dc' % (c))
  return ' '.join(a)
    
try:
  while True:
    try:
      v = float(raw_input('Enter broker amount: '))
      print "Broker price: %s" % (toGold(v))
      v = v/tax     # seller's original set price
      v -= v * discount # our discounted price
      print "Sale price %s for a broker price of %s" % \
            (toGold(v),toGold(tax*v))
    except ValueError:
      print "Bad input! Bad!"
      
except EOFError:
  print "\nBye!"
