import time
time_1 = time.time()
big_int = 600851475143
divider = 2
while big_int > divider:
    if big_int % divider == 0:
        big_int /= divider
    divider += 1
print(big_int)
print(time.time() - time_1)

