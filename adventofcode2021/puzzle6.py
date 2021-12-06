# puzzle the sixth day of advent of code

data_file_name = 'puzzle6.dat'

def read_ages():
    with open(data_file_name) as f:
        return [int(x) for x in f.read().strip().split(',')]
    raise Exception('could not read file')

def solve(days):
    fishes = read_ages()
    buckets = [fishes.count(i) for i in range(9)]
    for i in range(days):
        cycle = buckets[0]
        for i in range(1,9): buckets[i-1] = buckets[i]
        buckets[8] = cycle
        buckets[6] += cycle
    print (sum(buckets))

if __name__ == '__main__':
    solve(80)
    solve(256)

