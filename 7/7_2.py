from heapq import heappush, heappop, heapify
from collections import defaultdict

in_degrees = defaultdict(int)
graph = defaultdict(list)
for src, dst in map(lambda s: (s[5], s[-12]), (s for s in open('input.txt').read().split('\n'))):
    in_degrees[dst] += 1
    graph[src].append(dst)

q = []
for node in graph:
    if in_degrees[node] == 0: # root nodes
        q.append(node)
heapify(q)

def node_time(node):
    return ord(node) - 4

workers = [('XX', 0)] * 5
time = 0
while True:
    for i, (node, busy_for) in enumerate(workers):
        if busy_for == 0 and node != 'XX':
            workers[i] = ('XX', 0)
            for dst in graph[node]:
                in_degrees[dst] -= 1
                if in_degrees[dst] == 0:
                    heappush(q, dst)

    free_workers = []
    for i, (node, busy_for) in enumerate(workers):
        if busy_for == 0:
            free_workers.append(i)
    
    for worker_idx in free_workers:
        if q:
            node = heappop(q)
            workers[worker_idx] = (node, node_time(node))

    if not q and sum([busy_for for node, busy_for in workers]) == 0:
        break

    for i, (node, busy_for) in enumerate(workers):
        workers[i] = (node, max(0, busy_for - 1))
    time += 1

print('total time elapsed:', time)