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

order = ""
while q:
    node = heappop(q)
    order += node
    for dst in graph[node]:
        in_degrees[dst] -= 1
        if in_degrees[dst] == 0 and dst not in order:
            heappush(q, dst)
print(order)