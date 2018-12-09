from functools import reduce

react = lambda s: reduce(lambda x, y: x[:-1] if x and ord(x[-1]) ^ 32 == ord(y) else x+y, s)
data = react(open('input.txt').read())

print(len(data))
print(min(len(react(filter(lambda x: x.upper() != c, data))) for c in map(chr, range(65, 91))))