from collections import Counter, defaultdict
import itertools

with open('input.txt') as f:
    ids = f.read().splitlines()

dd = defaultdict(int)
for ss in [set(v for _, v in Counter(s).items() if v in [2,3]) for s in ids]:
    for v in ss:
        dd[v] += 1

print(dd[2] * dd[3])

def first_common(ids):
    for a, b in itertools.combinations(ids, 2):
        diffs = [ch1 == ch2 for ch1, ch2 in zip(a, b)]
        if sum(diffs) == len(a) - 1:
            return ''.join(itertools.compress(a, diffs))

print(first_common(ids))