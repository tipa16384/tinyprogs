# Riddle at 74,42,23 = cdefab / 2 = abcdef

for a in range(0,10):
    for b in range(0,10,2):
        for c in range(0,10):
            for d in range(0,10):
                for e in range(0,10):
                    for f in range(0,10):
                        dnum = c * 100000 + d * 10000 + e * 1000 + f * 100 + a * 10 + b
                        ddiv = a * 100000 + b * 10000 + c * 1000 + d * 100 + e * 10 + f
                        if dnum / 2 == ddiv:
                            print ("{}{}/{}{}x{}{} (numbers were {} and {})".format(a,b,c,d,e,f,dnum,ddiv))


