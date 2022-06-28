import time

cache = {
    1: 1,
    2: 1,
}


def fibonacci(n):
    if n in cache.keys():
        return cache[n]
    answer = fibonacci(n - 1) + fibonacci(n - 2)
    cache[n] = answer
    return answer


time_1 = time.time()

n = 3
while len(str(fibonacci(n))) < 1000:
    n += 1

print(n)

print(time.time() - time_1)
