import time


def eratosthenes_sieve(check_range, bool_list, segment_ceil):
    for i in check_range:
        # Skip if the number itself isn't a prime
        if bool_list[i - check_range[0]] is True:
            deactivate_prime_index = 2 * i
            while deactivate_prime_index <= segment_ceil:
                bool_list[deactivate_prime_index - check_range[0]] = False
                deactivate_prime_index += i
    new_primes = [check_range[i] for i in range(len(check_range)) if bool_list[i] is True]

    return new_primes


time_1 = time.time()

segment_ceil = 2000000
check_range = list(range(2, segment_ceil + 1))
bool_list = [True] * len(check_range)
primes = eratosthenes_sieve(check_range, bool_list, segment_ceil)

print(sum(primes))

print(time.time() - time_1)

