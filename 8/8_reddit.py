# solution found on Reddit https://www.reddit.com/r/adventofcode/comments/a47ubw/2018_day_8_solutions/ebc82oj/

def solve(child, meta):
    if child == 0:
        return sum(next(data) for _ in range(meta))
    value = 0
    children = {}
    for i in range(1, child+1):
        #value += solve(next(data), next(data))
        children[i] = solve(next(data), next(data))
    for _ in range(meta):
        #value += next(data)
        value += children.get(next(data), 0)
    return value

data = iter(map(int, open('input.txt').read().split()))

print(solve(next(data), next(data)))