from math import log10, sqrt


def getRandom(x, a, b, M):
    randomNum = (a*x + b) % M
    return randomNum


def getH():
    h = (max(u) - min(u)) / (1 + 3.3221 * log10(len(u)))
    return h


def getLists(u, h):
    uCopy = u.copy()
    minimal = min(u)
    res = []
    inters = []
    while len(uCopy) != 0:
        n = []
        for i in uCopy:
            if (i >= minimal and i < minimal + h):
                n.append(i)
        for i in n:
            uCopy.remove(i)
        inters.append([minimal, minimal + h])
        minimal += h
        res.append(n)
    return res, inters

# a

def getN(lst):
    n = []
    for l in lst:
        n.append(len(l))
    return n

def getSampleAvg(lst):
    n = len(lst)
    s = sum(lst)
    return s/n


def getDispersion(lst):
    sa = getSampleAvg(lst)
    n = len(u)
    s = 0
    for x in u:
        s += (x - sa) ** 2
    return s/n


def getSigma(dispersion):
    return sqrt(dispersion)


def getSegmentEnds(sigma):
    a = sa - sqrt(3) * sigma
    b = sa + sqrt(3) * sigma
    return a, b


def getDensityProb(a, b):
    return 1 / (b - a)


def getFreqs(countInters, a, b, n):
    freqs = []
    xmin = inters[0][0]
    h = inters[0][1] - inters[0][0]
    for i in range(countInters):
        if i == 0:
            freq = n * (xmin + h/2 - a) / (b - a)
            xmid = xmin + h/2
        elif i == countInters - 1:
            freq = n / (b - a) * (b - xmid)
        else:
            freq = n / (b - a) * h
            xmid += h
        freqs.append(freq)
    return freqs


def getXPirs(freqs, n, np):
    x = 0
    for i in range(len(np)):
        x += (np[i] - freqs[i]) ** 2 / freqs[i]
    return x

# b


def getMed(lst):
    lstCopy = lst.copy()
    lstCopy.sort()
    n = len(lst)
    if n % 2 == 0:
        return 0.5 * (lstCopy[int(n/2)] + lstCopy[int(n/2) + 1])
    return lstCopy[int((n+1)/2)]


def getSeries(lst, med):
    series = ""
    for num in lst:
        if num >= med:
            series += "+"
        else:
            series += "-"
    return series


def getCountSeries(series):
    count = 1
    lst = list(series)
    for i in range(1, len(lst)):
        if lst[i] != lst[i-1]:
            count += 1
    return count

# c


def getRKoef(lst):
    n = len(lst)
    ix = 0
    x2 = 0
    x = 0
    xn = 0
    for i in range(n):
        ix += i * lst[i]
        xn += lst[i] * (n+1)/2
        x2 += lst[i] ** 2
        x += lst[i]
    ch = 1/n * ix - 1/n * xn
    zn = (1/n * x2 - (1/n * x) ** 2) * (n * n - 1) / 12
    return ch/zn


def getRMax(za, rKoef, n):
    return za * (1 - rKoef ** 2) / sqrt(n)


x = 38
a = 37
b = 1
M = 1000
u = []
for i in range(100):
    print(f"X={x} U={x/1000}")
    u.append(x/1000)
    x = getRandom(x, a, b, M)

# a
print("КРИТЕРИЙ X^2 ПИРСОНА")
ns, inters = getLists(u, getH())
countInters = len(inters)
n = getN(ns)
sa = getSampleAvg(u)
dispersion = getDispersion(u)
sigma = getSigma(dispersion)
a, b = getSegmentEnds(sigma)
f = getDensityProb(a, b)
freqs = getFreqs(countInters, a, b, len(u))
xN = getXPirs(freqs, countInters, n)
xCrit = 11.1
print(f"H: {getH()}")
print(f"Интервалы:")
countX = 0
for inter in ns:
    countX += len(inter)
for i in range(countInters):
    print(i + 1)
    print(inters[i])
    print(ns[i])
print(f"Nx: {countX}")
print()
print(f"Выборочное среднее: {sa}")
print(f"D: {dispersion}")
print(f"Сигма: {sigma}")
print(f"a*: {a}, b*: {b}")
print(f"f: {f}")
print(f"Теоретические частоты: {freqs}")
print(f"X набл: {xN}")

if (xN < xCrit):
    print("Принимаем гипотезу о равномерном распределении генеральной совокупности")
else:
    print("Отвергаем гипотезу о равномерном распределении генеральной совокупности")
print()

# b
print("КРИТЕРИЙ СЕРИЙ")
print()
median = getMed(u)
series = getSeries(u, median)
seriesCount = getCountSeries(series)
s1 = 40
s2 = 61
print(f"Med(N): {median}")
print(f"Серия: {series}")
print(f"S: {seriesCount}")
if seriesCount > s1 and seriesCount < s2:
    print("Принимаем гипотезу о случайности H0")
else:
    print("Отвергаем гипотезу о случайности H0")
print()

# c
print("КОЭФФИЦИЕНТ КОРРЕЛЯЦИИ")
za = 1.96
r = getRKoef(u)
rmax = getRMax(za, r, len(u))
print(f"r: {r}")
print(f"rmax: {rmax}")
if (abs(r) < rmax):
    print("Принимаем гипотезу о независимости между псевдослучайными числами")
else:
    print("Отвергаем гипотезу о независимости между псевдослучайными числами")
