import time
import math


def is_prime(value):
    if value <= 1:
        return False
    # Chekc for even
    if value % 2 == 0:
        return False
    # You only need to check to the sqrt of value because any value over that will always be a
    # multiple of a lower number
    # Also we only need to check odd numbers, starting from 3
    for i in range(3, math.floor(math.sqrt(value)) + 1, 2):
        if value % i == 0:
            return False
    return True


time_1 = time.time()

highest_n = 0
final_a = 0
final_b = 0

# a must be even
for a in range(-999, 1001, 2):
    print(f'Running a={a}')
    # b has to be prime and positive otherwise 0 fails straight away
    # because is_prime fails right away for none-prime b it;s faster to just brute force anyway
    # Also b > -a as per 1 + a + b > 1
    for b in range(max(-a, 1), 1001):
        n = 0
        while True:
            value = n**2 + a * n + b
            if not is_prime(value):
                break
            n += 1
        if n > highest_n:
            highest_n = n
            print(f'New best n={n}| a,b={a},{b}')
            final_a = a
            final_b = b

print(final_a * final_b)
print(time.time() - time_1)