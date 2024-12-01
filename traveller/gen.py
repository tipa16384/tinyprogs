#!/usr/bin/python

from random import randint

str = 'str'
dex = 'dex'
end = 'end'
int = 'int'
edu = 'edu'
soc = 'soc'

stats = {}

hexdigits = '0123456789ABCDEF'

def rollstat():
	return randint(1,6) + randint(1,6)

def statcode(lstats):
	return hexdigits[lstats[str]] \
		+ hexdigits[lstats[dex]] \
		+ hexdigits[lstats[end]] \
		+ hexdigits[lstats[int]] \
		+ hexdigits[lstats[edu]] \
		+ hexdigits[lstats[soc]]

while True:
	stats[str] = rollstat()
	stats[dex] = rollstat()
	stats[end] = rollstat()
	stats[int] = rollstat()
	stats[edu] = rollstat()
	stats[soc] = rollstat()
	avgstat = sum(stats.values())/6.0
	if avgstat > 7.0:
		break

print (stats)
print (statcode(stats))

