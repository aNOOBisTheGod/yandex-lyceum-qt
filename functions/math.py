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
    return 0



print(equation('x ** 2 = 10'))