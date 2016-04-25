def gcd(a, b):
    if b == 0:
        return a
    return b if a % b == 0 else gcd(b, a % b)


def ext_gcd(a, b):
    if b == 0:
        return 1, 0

    tmpx, tmpy = ext_gcd(b, a % b)
    x = tmpy
    y = tmpx - (a / b) * tmpy
    return x, y


def soluble(gcd, c):
    return True if c % gcd == 0 else False


def solver(s1, s2, v1, v2, m):
    a = v1 - v2
    b = m
    c = s2 - s1

    if a < 0:
        a = a + m

    d = gcd(a, b)

    if not soluble(d, c):
        return -1

    a = a / d
    b = b / d
    c = c / d

    x, y = ext_gcd(a, b)
    x = (x * c) % b
    while x < 0:
        x = x + b
    return x


s1, s2, v1, v2, m = map(lambda x: int(x), raw_input().split())
if v1 > v2:
    s1, s2, v1, v2 = s2, s1, v2, v1

print solver(s1, s2, v1, v2, m)
