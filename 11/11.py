# https://en.wikipedia.org/wiki/Summed-area_table
# https://www.codeproject.com/Articles/441226/Haar-feature-Object-Detection-in-Csharp#integral
s = 1308
grid_size = 300
get_power = lambda x, y: (((x + 10) * y) + s) * (x + 10) // 100 % 10 - 5
integral = dict()
for y in range(grid_size):
    for x in range(grid_size):
        integral[(x, y)] = get_power(x, y) + integral.get((x, y-1), 0) \
                         + integral.get((x-1, y), 0) - integral.get((x-1, y-1), 0)

gp = dict()
for size in range(2, grid_size):
    for y in range(size-1, grid_size):
        for x in range(size-1, grid_size):
            rect_power = integral[(x, y)] - integral.get((x-size, y), 0) \
                       - integral.get((x, y-size), 0) + integral.get((x-size, y-size), 0)
            gp[(x-size+1, y-size+1, size)] = rect_power

print('part 1: power={}, size=3x3, x={}, y={}'.format(*max((power, x, y) for (x, y, size), power in gp.items() if size == 3)))
print('part 2: power={0}, size={1}x{1}, x={2}, y={3}'.format(*max((power, size, x, y) for (x, y, size), power in gp.items())))