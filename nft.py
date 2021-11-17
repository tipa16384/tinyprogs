#/usr/bin/python

prob = 0.00014

priceperpack = 0.80
moneytospend = 15000
tries = int(moneytospend / priceperpack)

for i in range(tries,tries+1):
  p = 1 - pow(1 - prob, i)
  if p >= 0.5:
    print "to have a {}% chance of getting Asteroids, buy {} packs!".format(p * 100, i)
    break

