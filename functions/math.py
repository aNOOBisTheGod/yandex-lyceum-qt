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
    a[x] = ' '
    powerstr = f'* {letter} '
    for _ in range(power - 2):
        powerstr += f'* {letter} '
    a[x + 1] = powerstr
    a = ''.join(a)
    return a