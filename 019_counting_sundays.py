import time

time_1 = time.time()

month_days = {1: 31,
              2: 28,
              3: 31,
              4: 30,
              5: 31,
              6: 30,
              7: 31,
              8: 31,
              9: 30,
              10: 31,
              11: 30,
              12: 31}

start_day = 1  # Monday
sunday_counter = 0
for i in range(100):
    for j in range(1, 13):
        start_day += month_days[j]
        if j == 2 and i % 4 == 0:
            if i % 100 != 0:
                if i % 400 == 0:
                    start_day += 1
            else:
                start_day += 1
        if start_day % 7 == 0:
            sunday_counter += 1

print(sunday_counter)
print(time.time() - time_1)