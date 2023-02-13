import time

time_1 = time.time()

"""The top-left to bottom-right diagonal has numbers with spaces between them of: 
    [2] * 4, [3] * 4 etc. 
Also note that a n by n spiral has (2 * n - 1) numbers on it's diagonal. Knowing this"""

n = 1001
spaces = []
for i in range(2, n, 2):
    spaces += [i] * 4

diagonals = 1
next_number = 1
for number in spaces:
    next_number = number + next_number
    diagonals += next_number

print(f'Result: {diagonals}')

print(time.time() - time_1)
