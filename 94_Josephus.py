t = int(raw_input())


def josephus(n, k):
    tmp1 = 0
    i = 2
    while i <= n:
        if tmp1 + k < i:
            x = (i - tmp1) / k
            if i + x < n:
                i += x
                tmp2 = tmp1 + x * k
                tmp1 = tmp2
            else:
                tmp2 = tmp1 + (n - i) * k
                tmp1 = tmp2
                i = n
        tmp2 = (tmp1 + k) % i
        tmp1 = tmp2
        i += 1
    return tmp2


while t:
    n, k = raw_input().split()
    print josephus(int(n), int(k))
    t -= 1
