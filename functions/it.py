import string


def fromidektotenth(num, base):
    num = num.split('.')
    res1 = 0.0
    for power, n in enumerate(reversed(list(num[0]))):
        if n in string.ascii_uppercase:
            n = 10 + string.ascii_uppercase.find(n)
        res1 += n * base ** power
    res2 = 0.0
    if len(num) > 1:
        for power, n in enumerate(list(num[1])):
            if n in string.ascii_uppercase:
                n = 10 + string.ascii_uppercase.find(n)
            res2 += n * base ** -(power + 1)
    return res1 + res2


def fromtenthtoidek(num, base):
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
        for i in range(5):
            x = float(num.split('.')[1])
            x *= base
            print(x)
            res += str(x)[0] if x % 1 < 10 else string.ascii_uppercase[x // 1 - 10]

    return res


print(fromtenthtoidek('39.5', 4))
#
# def systemconverter(num, basef, baset):
#
