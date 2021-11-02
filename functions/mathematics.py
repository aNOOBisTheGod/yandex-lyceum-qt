import math
import time


def niceeval(a):
    """converts simple string like x ** 3 to x * x * x (usage implemented in charts)"""
    a = a.split(' ')
    x = a.index('**')
    power = a[x + 1]
    try:
        power = int(power)
    except Exception as e:
        return ''.join(a)
    if power <= 1:
        return ''.join(a)
    letter = a[x - 1]
    a[x - 1] = '(' + a[x - 1]
    a[x] = ' '
    powerstr = f'* {letter} '
    for _ in range(power - 2):
        powerstr += f'* {letter} '
    a[x + 1] = powerstr + ')'
    a = ''.join(a)
    return a


def diophantic(line):
    """solves diophantine equation ax + by = c, returns x and y"""
    a, b, c = map(int, line.split())
    d, x, y = megagcd(a, b)
    if c % d != 0:
        return 'Impossible'
    else:
        x *= c // d
        y *= c // d

        a //= d
        b //= d
        return ', '.join([str(x % b), str(y + (x - x % b) // b * a)])


def megagcd(a, b):
    """needs in diophantic function"""
    if b == 0:
        return a, 1, 0
    d, x, y = megagcd(b, a % b)
    return d, y, x - y * (a // b)


def median(a):
    """returns median of row of numbers if no median: -inf"""
    a = list(map(float, a.split()))
    d = {}
    a.sort()
    for i in range(len(a) - 1):
        if a[i] == a[i + 1]:
            if a[i] in d:
                d[a[i]] += 1
            else:
                d[a[i]] = 1
    max = -math.inf
    res = -math.inf
    for k, i in d.items():
        if i > max:
            res = k
    return str(res)


def mean(line):
    """returns mean of row of numbers"""
    a = list(map(float, line.split()))
    res = 0.0
    for i in a:
        res += i
    res /= len(a)
    return str(res)


def fastequation(eq):
    """solves simple equation uses binary search"""
    right = 1000000
    left = -1000000
    ans = float(eq.split('=')[1])
    eq = eq.split('=')[0].replace('x', '{}')
    for i in range(100):
        middle = (right + left) / 2
        print(middle)
        e = float(eval(eq.format(middle)))
        if e > ans:
            right = middle
        elif e < ans:
            left = middle
        else:
            return str(middle)
    return '± ' + str(middle.__round__())


def quadratic(eq):
    """solves simple quadratic equation"""
    a, b, c = map(int, eq.split())
    d = b ** 2 - (4 * a * c)
    if d < 0.0:
        return 'None'
    elif d > 0.0:
        return ', '.join(list(map(str, [(-b + math.sqrt(d)) /(2 * a), (-b - math.sqrt(d)) /(2 * a)])))
    else:
        return str(b /(2 * a))