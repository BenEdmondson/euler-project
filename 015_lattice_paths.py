import time

time_1 = time.time()

grid_size = 20
pascal_triangle_level = grid_size * 2
level = [1, 1]
for i in range(pascal_triangle_level - 1):
    next_level = list()
    for j in range(len(level)):
        if j == 0:
            next_level.append(1)
            next_level.append(level[0] + level[1])
        elif j == len(level) - 1:
            next_level.append(1)
        else:
            next_level.append(level[j] + level[j+1])
    level = next_level
print(level)
print(max(level))
print(time.time() - time_1)