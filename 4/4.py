import operator
from collections import defaultdict

with open('input.txt') as f:
    input = sorted(f.read().split('\n'))

SD = defaultdict(int)
MD = defaultdict(lambda: [0] * 60)
for line in input:
    if 'Guard' in line:
        guard = int(line.split()[3][1:])
    elif 'falls' in line:
        sleep_time = int(line[15:17])
    else:    
        time = int(line[15:17])
        SD[guard] += time - sleep_time
        for i in range(sleep_time, time):
            MD[guard][i] += 1

lazy_guard = max(SD.items(), key=operator.itemgetter(1))[0]
lazy_min = MD[lazy_guard].index(max(MD[lazy_guard]))
print(lazy_guard * lazy_min)

best = None
for guard, mins in MD.items():
    if best is None or max(mins) > best:
        best = max(mins)
        lazy_min = mins.index(best)
        lazy_guard = guard
print(lazy_guard * lazy_min)
