from itertools import chain
from collections import Counter

def manhattan_distance(pt1, pt2):
    return abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])

GRID_SIZE = 1000
input = open('input.txt').read().split('\n')
pairs = [(int(s.split(',')[0]), int(s.split(',')[1][1:])) for s in input]

def mark_infinite(pairs, infinite, point):
    # point is infinite iff it's the uniquely closest point to a point on the bounding rectangle
    distances = [manhattan_distance(point, coord) for coord in pairs]
    closest = min(distances)
    if distances.count(closest) == 1: 
        infinite[distances.index(closest)] = True

infinite = [False] * len(pairs)
for y in range(GRID_SIZE):
    for x in [0, GRID_SIZE-1]:
        mark_infinite(pairs, infinite, (x,y))
for x in range(GRID_SIZE):
    for y in [0, GRID_SIZE-1]:
        mark_infinite(pairs, infinite, (x,y))
pairs = list(zip(infinite, pairs))

grid = [[-1 for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]
for x in range(GRID_SIZE):
    for y in range(GRID_SIZE):
        distances = [manhattan_distance((x,y), pair[1]) for pair in pairs]
        closest = min(distances)
        if distances.count(closest) == 1: 
            grid[x][y] = distances.index(closest)

totals = Counter(i for i in list(chain.from_iterable(grid)) if i != -1).most_common()
for i, count in totals:
    if not infinite[i]:
        print("part 1:", count)
        break

MAX_DISTANCE = 10000
region_size = 0
for x in range(GRID_SIZE):
    for y in range(GRID_SIZE):
        total_distance = sum([manhattan_distance((x,y), pair[1]) for pair in pairs])
        if total_distance < MAX_DISTANCE:
            region_size += 1
print("part 2:", region_size)
    
