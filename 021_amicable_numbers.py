import time
import functools
import math


@functools.lru_cache(maxsize=10000)
def sum_of_factors(number):
    total_factor = 0
    for i in range(1, math.ceil(number/2) + 1):
        if number % i == 0:
            total_factor += i

    return total_factor


time_1 = time.time()

total_amicable_number = 0
for i in range(1, 10001):
    first = sum_of_factors(i)
    second = sum_of_factors(first)
    if second == i and first != second:
        total_amicable_number += i

print(total_amicable_number)
print(time.time() - time_1)