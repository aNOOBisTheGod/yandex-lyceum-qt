import math
import time


def equation(equation):
    if equation.count('x') == 2:
        return 'Inset equation with only 1 unknown statement'
    equation = equation.replace('x', '{}')
    equation = equation.replace(' ', '')
    right = 1000
    left = -1000
    equation, ans = tuple(equation.split('='))
    ans = int(ans)
    for i in range(500):
        middle = (right + left) / 2
        result = eval(equation.format(middle))
        if result < ans:
            left = middle
        elif result > ans:
            right = middle
        else:
            return middle
    return middle


def quadraticequation(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return ['R']
            else:
                return ['∅']
        else:
            return[-c / b]
    else:
        D = b ** 2 - 4 * a * c
        if D < 0:
            return ['∅']
        elif D == 0:
            return [-b / (2 * a)]
        else:
            x1 = (-b - D ** 0.5) / (2 * a)
            x2 = (-b + D ** 0.5) / (2 * a)
            return [x1, x2]


def niceeval(a):
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
    if b == 0:
        return a, 1, 0
    d, x, y = megagcd(b, a % b)
    return d, y, x - y * (a // b)


def median(a):
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
    a = list(map(float, line.split()))
    res = 0.0
    for i in a:
        res += i
    res /= len(a)
    return str(res)


def fastequation(eq):
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
    a, b, c = map(int, eq.split())
    d = b ** 2 - (4 * a * c)
    if d < 0.0:
        return 'None'
    elif d > 0.0:
        return ', '.join(list(map(str, [(-b + math.sqrt(d)) /(2 * a), (-b - math.sqrt(d)) /(2 * a)])))
    else:
        return str(b /(2 * a))