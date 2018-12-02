from collections import Counter, defaultdict
import difflib
import itertools

with open('input.txt') as f:
    ids = f.read().splitlines()

dd = defaultdict(int)
for ss in [set(v for _, v in Counter(s).items() if v in [2,3]) for s in ids]:
    for v in ss:
        dd[v] += 1

print(dd[2] * dd[3])

def find_common(ids):
    for a, b in itertools.combinations(ids, 2):
        diff = list(difflib.ndiff(a, b))
        if len(diff) == len(a) + 1: # works because all ids are the same length
            return ''.join([v[2] for v in diff if v[0] not in ['+', '-']])

print(find_common(ids))