def gcd(a, b):
    if b == 0:
        return a
    return b if a % b == 0 else gcd(b, a % b)

def soluble(gcd, c):
    return True if c % gcd == 0 else False

def ext_gcd(a, b):
    if b == 0:
        return 1, 0

    tmpx, tmpy = ext_gcd(b, a % b)
    x = tmpy
    y = tmpx - (a / b) * tmpy
    return x, y


N = int(raw_input())
m = []
r = []
for i in range(N):
    tmp = map(lambda x: int(x), raw_input().split())
    m.append(tmp[0])
    r.append(tmp[1])

M = m[0]
R = r[0]
for i in range(1,N):
    d = gcd(M, m[i])
    c = r[i] - R
    if not soluble(d, c):
        print -1
    k1, k2 = ext_gcd(M/d, m[i]/d)
    k1 = (c / d * k1) % (m[i]/d)
    R = R + k1 * M
    M = M / d * m[i]
    R %= M

if R < 0:
    R = R + M
print R
