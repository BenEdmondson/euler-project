import time


def approach_1(series, multiplication_length):
    products = list()
    for i in range(len(series) - multiplication_length):
        product = 1
        for j in range(i, i + multiplication_length):
            product *= int(series[j])
        products.append(product)
    return max(products)


def approach_2(series, multiplication_length):
    series = series.split('0')
    products = list()
    for block in series:
        if len(block) < multiplication_length:
            continue
        for i in range(len(block) - multiplication_length + 1):
            product = 1
            for j in range(i, i + multiplication_length):
                product *= int(block[j])
            products.append(product)
    return max(products)


def approach_3(series, multiplication_length):
    def culc(s, nt=1):
        for i in series[s - multiplication_length:s]: nt *= int(i)
        return nt

    return(max([culc(s) for s in range(multiplication_length, len(series))]))


time_1 = time.time()
series = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'

multiplication_length = 13
result = approach_1(series, multiplication_length)
print(result)
print(time.time() - time_1)
time_2 = time.time()
result = approach_2(series, multiplication_length)
print(result)
print(time.time() - time_2)
time_3 = time.time()
result = approach_3(series, multiplication_length)
print(result)
print(time.time() - time_3)