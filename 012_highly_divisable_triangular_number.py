import time
import math


def check_if_prime(number):
    # This will fail for pseudoprimes
    if 2 ** (number - 1) % number == 1 or number in [2]:
        return True
    else:
        return False


def determine_number_of_divisors2(number):
    divisors_count = 0
    for i in range(1, math.ceil(math.sqrt(number) + 1)):
        if number % i == 0:
            divisors_count += 1
    return divisors_count * 2


def determine_number_of_divisors(number):
    divisors = [[], [number]]
    while len(divisors[-2]) != len(divisors[-1]):
        new_divisors = list()
        for value in divisors[-1]:
            if str(value) in cache.keys():
                new_divisors += cache[str(value)]
            else:
                if not check_if_prime(value):
                    for i in range(2, value+1):
                        if value % i == 0:
                            new_divisors += [i, int(value / i)]
                            break
                else:
                    new_divisors += [value]
        divisors.append(new_divisors)
    factor_list = divisors[-1]
    cache[str(number)] = factor_list
    used_factors = set(factor_list)
    counts = list()
    for factor in used_factors:
        counts.append(factor_list.count(factor))
    product = 1
    for count in counts:
        product *= count + 1

    return product


time_1 = time.time()
cache = {}

required_divisors = 500

triangle_numbers = [3]
for i in range(3, 200000):
    triangle_numbers.append(triangle_numbers[-1] + i)
for value in triangle_numbers:
    number_of_divisors = determine_number_of_divisors2(value)
    print(value, number_of_divisors)
    if number_of_divisors >= required_divisors:
        print(value)
        break
print(time.time() - time_1)
