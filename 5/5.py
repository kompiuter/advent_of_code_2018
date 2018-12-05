from functools import reduce

def trigger(x, y):
    return False if not x else ord(x[-1]) ^ 32 == ord(y)

def react(polymer):
    return reduce((lambda x, y: x[:-1] if trigger(x, y) else x+y), polymer)

polymer = open('input.txt').read()
print('p1', len(react(polymer)))
print('p2', min([len(react(polymer.replace(chr(i), '').replace(chr(i-32), ''))) for i in range(ord('a'), ord('z') + 1)]))