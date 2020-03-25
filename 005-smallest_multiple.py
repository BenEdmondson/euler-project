import time


def gcd(a, b):
    start = min(a, b)
    for i in range(start, 0, -1):
        if a % i == 0 and b % i == 0:
            calc_gcd = i
            break
    return calc_gcd


time_1 = time.time()

highest_number = 20
factor_list = list(range(1, highest_number + 1))
tot_lcm = 2  # lcm(1,2)
for i in factor_list[2:-1]:
    calc_gcd = gcd(tot_lcm, i)
    tot_lcm = int(tot_lcm * i / calc_gcd)

print(tot_lcm)


print(time.time() - time_1)
