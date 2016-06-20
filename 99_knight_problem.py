def check(s):
    return s[0] == s[1] == s[2]


def move(s):
    for i in [(1, 2), (2, 1)]:
        for j in [(1, 1), (1, -1), (-1, -1), (-1, 1)]:
            for k in range(3):
                v = s[k][0] + i[0] * j[0], s[k][1] + i[1] * j[1]
                if v[0] < 0 or v[0] > 8 or v[1] < 0 or v[1] > 8:
                    continue
                t = list(s)
                t[k] = v
                yield tuple(t)


def solver(s):
    if check(s):
        return 0
    d = {s: 0}
    q = [s]
    while len(q):
        u = q.pop()
        for i in move(u):
            if i in d:
                continue
            d[i] = d[u] + 1
            if check(i):
                return d[i]
            q.insert(0, i)


for c in range(input()):
    s = tuple(((ord(i[0]) - ord('A')), ord(i[1]) - ord('1')) for i in raw_input().split())
    print solver(s)
