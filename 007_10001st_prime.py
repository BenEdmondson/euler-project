import time
import math


def prime_1():
    prime_target = 10001
    prime_counter = 0
    iterator = 2
    while prime_counter < prime_target:
        prime = True
        for i in range(2, iterator):
            if iterator % i == 0:
                prime = False
                break
        if prime is True:
            prime_counter += 1

        iterator += 1
        print(prime_counter)
    print(iterator - 1)


def eratosthenes_sieve(check_range, bool_list, segment_ceil):
    for i in check_range:
        # Skip if the number itself isn't a prime
        if bool_list[i - check_range[0]] is True:
            deactivate_prime_index = 2 * i
            while deactivate_prime_index < segment_ceil:
                bool_list[deactivate_prime_index - check_range[0]] = False
                deactivate_prime_index += i
    new_primes = [check_range[i] for i in range(len(check_range)) if bool_list[i] is True]

    return new_primes


def segmented_eratosthenes_sieve(segment_floor, segment_size, first_run, old_primes=None):
    segment_ceil = segment_floor + segment_size
    check_range = range(segment_floor, segment_ceil)
    bool_list = [True] * segment_size
    if not first_run:
        for prime in old_primes:
            # First multiple of a number which is inside the window
            first_mulitple = math.ceil(segment_floor / prime) * prime
            while first_mulitple < segment_ceil:
                bool_list[first_mulitple - check_range[0]] = False
                first_mulitple += prime
    new_primes = eratosthenes_sieve(check_range, bool_list, segment_ceil)
    return new_primes


def prime_2():
    prime_target = 10001
    prime_numbers = list()
    segment_size = 1000
    segment_floor = 2
    new_primes = segmented_eratosthenes_sieve(segment_floor, segment_size, True)
    prime_numbers += new_primes
    while len(prime_numbers) < prime_target:
        new_primes = segmented_eratosthenes_sieve(segment_floor, segment_size, False, old_primes=prime_numbers)
        prime_numbers += new_primes
        segment_floor += segment_size

    print(prime_numbers[10000])
    print(len(prime_numbers))
    print(prime_numbers)

time_1 = time.time()

prime_2()

print(time.time() - time_1)
