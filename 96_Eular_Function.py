import sys

l, n = map(lambda x: int(x), raw_input().split())

isPrime = [True for i in xrange(n+1)]
primeList = [0 for i in xrange(n+1)]
phi = [1 for i in xrange(n+1)]
primeCount = 0

for i in range(2, n+1):
    if isPrime[i]:
        primeCount += 1
        primeList[primeCount] = i
        phi[i] = i - 1
    j = 1
    while i*primeList[j] <= n:
        isPrime[i * primeList[j]] = False
        if i % primeList[j] == 0:
            phi[i * primeList[j]] = phi[i] * primeList[j]
            break
        else:
            phi[i * primeList[j]] = phi[i] * (primeList[j] - 1)
        j += 1

print phi[l:].index(min(phi[l:]))+l
