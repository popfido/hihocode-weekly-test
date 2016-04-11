import random
import math

t = int(raw_input())


def compute_power(a, p, m):
    result = 1
    p_bin = bin(p)[2:]
    length = len(p_bin)
    for i in range(0, length):
        result = result ** 2 % m
        if p_bin[i] == '1':
            result = result * a % m

    return result


def miller_rabin_witness(a, p):
    if p == 1:
        return False
    if p == 2:
        return True

    n = p - 1
    t = int(math.floor(math.log(n, 2)))
    u = 1
    while t > 0:
        u = n / 2 ** t
        if n % 2 ** t == 0 and u % 2 == 1:
            break
        t -= 1

    b1 = b2 = compute_power(a, u, p)
    for i in range(1, t + 1):
        b2 = b1 ** 2 % p
        if b2 == 1 and b1 != 1 and b1 != (p - 1):
            return False
        b1 = b2
    if b1 != 1:
        return False

    return True


def prime_test_miller_rabin(p, k):
    while k > 0:
        a = random.randint(1, p - 1)
        if not miller_rabin_witness(a, p):
            return False
        k -= 1
    return True


for i in range(t):
    a = long(raw_input())
    if prime_test_miller_rabin(a, 100):
        print "YES"
    else:
        print "NO"
