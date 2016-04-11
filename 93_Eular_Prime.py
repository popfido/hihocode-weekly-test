n = int(raw_input())

isPrime = [True for i in range(n+1)]
primeList = [0 for i in range(n+1)]
primeCount = 0

for i in range(2,n+1):
    if isPrime[i]:
        primeCount += 1
        primeList[primeCount] = i
    j = 1
    while i*primeList[j] <= n:
        isPrime[i * primeList[j]] = False
        if i % primeList[j] == 0:
            break
        j += 1

print primeCount