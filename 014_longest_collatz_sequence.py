import time


time_1 = time.time()
cache = {}
largest_allowed_start = 1000000
max_count = 0
# we only care about odd numbers
if largest_allowed_start % 2 == 0:
    largest_allowed_start -= 1
for number in range(1, largest_allowed_start + 1, 2):
    value = number
    count = 1
    while value != 1:
        if value in cache.keys():
            count += cache[value] - 2
            value = 1
        # Even number
        elif value % 2 == 0:
            value = value / 2
        # Odd number
        else:
            value = value * 3 + 1
        count += 1
    cache[number] = count
    if count > max_count:
        max_count = count
        max_sequence_value = number

print(max_sequence_value)
print(max_count)
print(time.time() - time_1)
