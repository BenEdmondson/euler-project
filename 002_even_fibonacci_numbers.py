import time

time_1 = time.time()
fibonacci = [1, 2]
while fibonacci[-1] < 4000000:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
print(fibonacci)
print(list(range(1, len(fibonacci), 3)))
total = 0
for i in range(1, len(fibonacci), 3):
    total += fibonacci[i]

print(total)
print(time.time() - time_1)