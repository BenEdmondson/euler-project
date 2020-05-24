import time

time_1 = time.time()

big_number = 2 ** 1000
list = [int(x) for x in str(big_number)]
print(sum(list))

print(time.time() - time_1)