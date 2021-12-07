import statistics

def crab_fuel(pos, dest):
    dist = abs(pos-dest)
    return (dist * (dist + 1)) // 2

with open('puzzle7.dat') as f:
    data = list(map(int, f.read().strip().split(',')))

median = int(statistics.median(data))

print(sum([abs(x-median) for x in data]))

mean = int(statistics.mean(data))

val1 = sum([crab_fuel(x, mean) for x in data])
val2 = sum([crab_fuel(x, mean+1) for x in data])

print(min(val1, val2))
