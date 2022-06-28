import time
import math


def get_reciprocal_length(i):
    seen_values = []
    value_remainder = (0, 1)
    while value_remainder not in seen_values:
        seen_values.append(value_remainder)
        old_remainder = value_remainder[1] * 10
        new_remainder = old_remainder % i
        if new_remainder == 0:
            return i, 0
        new_value = math.floor(old_remainder / i)
        value_remainder = (new_value, new_remainder)
    seen_values.append(value_remainder)
    first_occurance = seen_values.index(value_remainder, 0, -1)
    return i, len(seen_values) - first_occurance - 1


time_1 = time.time()

max_length = 0
goal_integer = 0
for i in range(1, 1001):
    integer, reciprocal_length = get_reciprocal_length(i)
    if reciprocal_length > max_length:
        max_length = reciprocal_length
        goal_integer = integer
print(goal_integer)
print(max_length)
print(1/goal_integer)
print(time.time() - time_1)