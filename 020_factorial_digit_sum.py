import time

time_1 = time.time()

factorial = 100

number = 1
for i in range(2, factorial + 1):
    number *= i

print(sum([int(x) for x in str(number)]))
print(time.time() - time_1)