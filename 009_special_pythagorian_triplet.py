import time
import math


time_1 = time.time()

for i in range(1, 333):
    for j in range(i + 1, math.floor((1000 - i) / 2)):
        k = 1000 - i - j
        if i ** 2 + j ** 2 == k ** 2:
            print(i * j * k)

print(time.time() - time_1)

