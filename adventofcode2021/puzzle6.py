# puzzle the sixth day of advent of code

data_file_name = 'puzzle6.dat'

def read_ages():
    with open(data_file_name) as f:
        return [int(x) for x in f.read().strip().split(',')]
    raise Exception('could not read file')

buckets = [0 for i in range(0,9)]
for fish in read_ages():
    buckets[int(fish)] += 1
for i in range(256):
    cycle = buckets[0]
    for i in range(1,9):
        buckets[i-1] = buckets[i]
    buckets[8] = cycle
    buckets[6] += cycle
print (sum(buckets))
