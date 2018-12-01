import itertools

def read_ints(filename):
    with open(filename) as f:
        return list(map(int, f))

freqs = read_ints('input.txt')
print(f'resulting frequency: {sum(freqs)}')

seen = set()
sum = 0
for element in itertools.cycle(freqs):
    sum += element
    if sum in seen:
        print(f'first frequency reached twice: {sum}')
        break
    seen.add(sum)