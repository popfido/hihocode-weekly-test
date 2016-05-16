import operator as op

opType = [op.add, (lambda a,b: a-b), op.mul, op.div, (lambda a,b: b-a), (lambda a,b: b/a)]


def makeNum(depth):
    if depth >= 4:
        return makeOperation(0)
    for i in range(0,4):
        if not used[i]:
            nowNum[depth] = numbers[i]
            used[i] = True
            if makeNum(depth+1):
                return True
            used[i] = False
    return False


def operation(op, a, b):
    if op == 0:
        return a+b
    elif op == 1:
        return a-b
    elif op == 2:
        return a*b
    elif op == 3:
        return a/b
    elif op == 4:
        return b-a
    else:
        return b/a


def makeOperation(depth):
    if depth >= 3:
        try:
            if operation(ops[2], operation(ops[1], operation(ops[0], nowNum[0], nowNum[1]), nowNum[2]), nowNum[3]) == 24.0:
            #if ops[2](ops[1](ops[0](nowNum[0], nowNum[1]), nowNum[2]), nowNum[3]) == 24.0:
                return True
            elif operation(ops[2], operation(ops[0], nowNum[0], nowNum[1]), operation(ops[1], nowNum[2], nowNum[3])) == 24.0:
            #elif ops[2](ops[0](nowNum[0], nowNum[1]),ops[1](nowNum[2], nowNum[3])) == 24.0:
                return True
            else:
                return False
        except Exception as e:
            return False
    else:
        for i in range(0,6):
            #ops[depth] = opType[i]
            ops[depth] = i
            if makeOperation(depth+1):
                return True
        return False

for i in range(int(raw_input())):
    numbers = map(lambda x: float(x), raw_input().split())

    used = [False] * 4

    nowNum = [0, 0, 0, 0]
    ops = [0, 0, 0]
    if makeNum(0):
        print "Yes"
    else:
        print "No"
