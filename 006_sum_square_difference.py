import time

time_1 = time.time()

target_number = 100

sum_of_squares = 0
sums = 0
for i in range(target_number):
    sum_of_squares += (i + 1) ** 2
    sums += i + 1
square_of_sums = sums ** 2

difference = square_of_sums - sum_of_squares
print(difference)
print(time.time() - time_1)
