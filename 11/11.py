from operator import itemgetter

s = 18
grid_size = 300
power = dict()
for y in range(1, grid_size+1):
    for x in range(1, grid_size+1):
        power[(x,y)] = (((x + 10) * y) + s) * (x + 10) // 100 % 10 - 5

square_power = dict()
for w in range(1, 301):
    for i in range(1, grid_size+2-w):
        for j in range(1, grid_size+2-w):
            if (w-1,i,j) in square_power:
                total = square_power[(w-1,i,j)]
                x = w - 1 + i
                for y in range(j, j+w):
                    total += power[(x,y)]
                y = w - 1 + j
                for x in range(i, i+w-1):
                    total += power[(x,y)]
                square_power[(w,i,j)] = total
            else:
                square_power[(w,i,j)] = sum(power[(x,y)] for x in range(i, i+w) for y in range(j, j+w))

largest = max(square_power.items(), key=itemgetter(1))
print(largest[0])
