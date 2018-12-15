state = open('input.txt').read().split('\n')[0].split(' ')[2]
rules = {}
for s in open('input.txt').read().split('\n')[2:]:
    rules[s[:5]] = s[9]

sums = [sum(i for i, p in enumerate(state) if p == '#')]
offset = 0
for _ in range(100):
    state = '..' + state + '..'
    offset += 2
    read_state = '..' + state + '..'
    next_state = ['.'] * len(state)
    for i in range(len(state)):
        pattern = read_state[i:i+5]
        next_state[i] = rules.get(pattern, '.')

    while next_state[0] == '.':
        next_state = next_state[1:]
        offset -= 1
    while next_state[-1] == '.':
        next_state = next_state[:-1]

    state = ''.join(next_state)
    sums.append(sum(i - offset for i, p in enumerate(state) if p == '#'))
    
print('part 1:', sums[20])

diffs = [j-i for i, j in zip(sums[:-1], sums[1:])]
prev_diff = -1e9
for i, diff in enumerate(diffs):
    if diff == prev_diff:
        stable_gen = i - 1
        stable_diff = diff
        break
    prev_diff = diff

print('part 2:', (50000000000 - stable_gen) * stable_diff + sums[stable_gen])