import math
import time
import itertools


cache = {}


def factorial(n):
    """Memoized factorial calculator. Probaly overkill for the lists we are working with, but easy enough to build"""
    if n not in cache.keys():
        cache[n] = 1 if n <= 1 else n * factorial(n-1)
    return cache[n]


def the_dumb_way(numbers, nth_number):
    """Works nicely for small sets, but is O2 with length of the list of numbers, which makes it unsuitable for this
    problem"""
    all_the_numbers = [numbers] * len(numbers)
    cartesian = list(itertools.product(*all_the_numbers))
    all_unique = []
    for i in cartesian:
        if len(i) == len(set(i)):
            all_unique.append(i)
    values = [''.join([str(x) for x in y]) for y in all_unique]
    values.sort()
    return values[nth_number]


def the_smart_way(numbers, nth_number):
    """Every digit is placed in the same spot n times when sorted based on the factorial of the rest of the list.
    After that we remove the already allocated option count and drop that digit from the list.
    Works for unsorted lists, duplicates and strings values as well
    """
    number_of_linked_reps = [factorial((len(numbers) - (index + 1))) for index in range(len(numbers))]
    digits = []
    for i in number_of_linked_reps:
        divisor = math.ceil(nth_number / i)
        digits.append(str(numbers[divisor - 1]))
        numbers.pop(divisor - 1)
        nth_number -= math.floor(nth_number / i) * i
    return ''.join(digits)


if __name__ == '__main__':
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    numbers.sort()
    nth_number = 1000000

    time_1 = time.time()

    # dumb_answer = the_dumb_way(numbers, nth_number)
    # print(dumb_answer)
    smart_answer = the_smart_way(numbers, nth_number)
    print(smart_answer)
    print(time.time() - time_1)