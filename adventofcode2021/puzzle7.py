import statistics

def crab_fuel(pos, dest, weight):
    return weight(abs(pos-dest))

def print_min(data, dest, weight):
    print(min(sum(crab_fuel(x, dest+y, weight) for x in data) for y in range(2)))

with open('puzzle7.dat') as f:
    data = list(map(int, f.read().strip().split(',')))

print_min(data, int(statistics.median(data)), lambda x: x)
print_min(data, int(statistics.mean(data)), lambda x: x * (x + 1) // 2)
