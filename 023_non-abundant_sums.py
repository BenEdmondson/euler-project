import time
import math
# 13.69 - 4179871
# cache = {}


def is_abundant(integer):
    # global cache
    divisor_list = [1]
    for i in range(2, math.floor(math.sqrt(integer)) + 1):
        if integer % i == 0:
            divisor_list += [i, integer / i]
    divisor_total = sum(set(divisor_list))
    return divisor_total > integer


time_1 = time.time()

total = 0
abundant_numbers = []
for i in range(1, 28124):
    if i % 1000 == 0:
        print(f'testing abundance {i}')
    if is_abundant(i):
        abundant_numbers.append(i)

number_list = []
for index, i in enumerate(abundant_numbers):
    print(f'summing with {i}')
    for index2, j in enumerate(abundant_numbers):
        if index2 > index or (i + j) >= 28124:
            break
        number_list.append(i + j)
print(f'{len(number_list)}, {len(set(number_list))}')

main_list = list(set(range(1, 28124)) - set(number_list))
total = sum(main_list)
print(f'Result: {total}')
print(time.time() - time_1)
