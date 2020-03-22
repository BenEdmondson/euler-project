import time

time_1 = time.time()
total_1 = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        total_1 += i
print(total_1)
print(time.time() - time_1)

# time_2 = time.time()
# total_2 = 0
# print(list(range(3, 1002, 3)))
# print(list(range(5, 1000, 5)))
# for i in range(3, 1002, 3):
#     if i % 5 != 0:
#         total_2 += i
# for i in range(5, 1000, 5):
#     total_2 += i
# print(time.time() - time_2)
# print(total_2)
