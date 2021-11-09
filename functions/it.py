import string


def totenth(num, base):
    """converts number to standard number system"""
    num = num.upper()
    num = num.split('.')
    res1 = 0.0
    for power, n in enumerate(reversed(list(num[0]))):
        try:
            x = int(n)
        except:
            x = 10 + string.ascii_uppercase.find(n)
        res1 += x * base ** power
    res2 = 0.0
    if len(num) > 1:
        for power, n in enumerate(list(num[1])):
            try:
                x = int(n)
            except:
                x = 10 + string.ascii_uppercase.find(n)
            res2 += x * base ** -(power + 1)
    return str(res1 + res2)


def fromtenth(num, base):
    """converts number from standard number system to other(system must be less 26)"""
    x = int(num.split('.')[0])
    res = ''
    while x >= base:
        if x % base > 10:
            res += string.ascii_uppercase[x % base // 1 - 10]
        else:
            res += str(x % base)
        x = x // base
    res += str(x)
    res = res[::-1]
    if len(num.split('.')) > 1:
        res += '.'
        x = float('0.' + num.split('.')[1])
        for i in range(5):
            x *= base
            res += str(x)[0] if x % 1 < 10 else string.ascii_uppercase[x // 1 - 10]
            x %= 1
            if x == 0:
                return res
    return res
