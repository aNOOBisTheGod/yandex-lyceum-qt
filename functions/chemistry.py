import requests
from bs4 import BeautifulSoup


def solveequation(x, y):
    url = 'https://chemequations.com/ru/?s=' + x + '+%2B+' + y + '&ref=input'

    def get_html(url, params=None):
        r = requests.get(url, params=params)
        return r

    def get_content(html):
        s = BeautifulSoup(html, 'html.parser')
        pog = s.find('h1', class_='equation main-equation well')
        if pog is None:
            return 'Error, insert valid elements'
        return pog.get_text()

    def parse():
        html = get_html(url)
        if html.status_code == 200:
            return get_content(html.text)
        else:
            return 'Error, enable WI-FI'

    return parse()


def chain(text):
    def get_content(html):
        global y
        s = BeautifulSoup(html, 'html.parser')
        react = s.findAll('div', class_='reac')
        for r in react:
            reaction = r.get_text()
            el = str(reaction).split()
            z = el[0]
            z1 = el[2]
            if z == x or el[2] == x or z[1:] == x or z1[1:] == x:
                totr = reaction
                break
        try:
            return totr
        except:
             return '?'

    def parse():
        def get_html(url, params=None):
            r = requests.get(url, params=params)
            return r

        html = get_html(url)
        if html.status_code == 200:
            return get_content(html.text)
        else:
            return 'Error, enable WI-FI'

    out = []
    c = 0
    a = list(text.split())
    for i in range(len(a) - 1):
        c += 1
        x = a[i]
        y = a[i + 1]
        for j in range(10):
            url = 'https://tutata.ru/chemistry/search?s=%3D+' + y + '&page=' + str(j)
            res = parse()
            if res != '?' or res == 'Error':
                break
        if len(res) == 1:
            out.append(str(c) + ':  ' + '?')
        else:
            out.append(str(c) + ':  ' + ''.join(res)[1:])
    return out


print(*chain('Ca CaO Ca(OH)2 Ca3(PO4)2'), sep='\n')