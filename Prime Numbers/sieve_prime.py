def sievesPrime(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, n + 1):
        for j in range(i+i, n + 1, i):
            if primes[j]:
                primes[j] = False
    return primes


primesNos = sievesPrime(1000000)

if primesNos[9908] == True:
    print('Its a prime')

# for index, items in enumerate(primesNos):
#     print(index)
