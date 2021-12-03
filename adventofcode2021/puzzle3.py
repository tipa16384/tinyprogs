# this is going to be a super cool program
# that will be able to do a lot of cool stuff

print ("Totally going to win this one")
print ("I'm going to be super cool")

fn = 'puzzle3.dat'

# read in fn as an array of binary numbers
def read_values(fn):
    with open(fn) as f:
        for x in f.read().splitlines():
            yield x

def binary_to_decimal(binary):
    return int(binary, 2)

width = 12

def calc_gamma(sieve):
    bitCount = [0 for x in range(width)]
    count = 0

    for x in sieve:
        count += 1
        for i in range(width):
            if x[i] == '1':
                bitCount[i] += 1

    gamma = ''
    epsilon = ''

    for i in bitCount:
        if i == count/2:
            gamma += '1'
            epsilon += '0'
        elif i > count/2:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    return (gamma, epsilon)

gamma, epsilon = calc_gamma(read_values(fn))

print (gamma, epsilon)
print (binary_to_decimal(gamma) * binary_to_decimal(epsilon))

sieve1 = [x for x in read_values(fn)]

for pos in range(width):
    gamma, epsilon = calc_gamma(sieve1)
    sieve2 = [x for x in sieve1 if x[pos] == gamma[pos]]
    sieve1 = sieve2
    if len(sieve1) == 1:
        break

print (sieve1)
oxygen = binary_to_decimal(sieve1[0])

sieve1 = [x for x in read_values(fn)]

print (sieve1)
for pos in range(width):
    gamma, epsilon = calc_gamma(sieve1)
    sieve2 = [x for x in sieve1 if x[pos] == epsilon[pos]]
    sieve1 = sieve2
    print (sieve1)
    if len(sieve1) == 1:
        break

print (sieve1)
co2 = binary_to_decimal(sieve1[0])

print (oxygen, co2)
print (oxygen * co2)




