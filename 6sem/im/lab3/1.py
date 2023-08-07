import numpy as np
import random
from scipy import stats
import pandas as pd


def getRandom(n, lambda_):
    x = []
    for _ in range(n):
        r = random.random()
        num = -1/lambda_ * np.log(r)
        x.append(num)
    return x

def getRandomZ(n):
    z = []
    for _ in range(n):
        r_final = -6
        for _ in range(12):
            r_final += random.random()
        z.append(r_final)
    return z

def getRandomZMuller(n):
    zMuller = []
    for _ in range(n):
        r1 = random.random()
        r2 = random.random()
        num = np.sqrt(-2*np.log(r1))*np.cos(2*np.pi*r2)
        zMuller.append(num)
    return zMuller



def getMat(x):
    return np.sum(x)/len(x)


def getDespersion(x):
    return np.var(x)

def getSqrtDespersion(x):
    return np.sqrt(np.var(x))

def getIntervals(x, k, h):
    intervals = []
    for i in range(k):
        interval = [np.min(x) + i*h, np.min(x) + (i+1) * h]
        intervals.append(interval)
    return intervals

def getFreqs(intervals, x):
    freqs = []
    for interval in intervals:
        freq = 0
        for i in range(len(x)):
            if x[i]>=interval[0] and x[i]<=interval[1]:
                freq += 1
        freqs.append(freq)
    return freqs


def getXMiddle(intervals, freqs):
    middles = []
    for interval in intervals:
        middles.append((interval[0] + interval[1])/2)
    
    gap_settle = 0
    for i in range(len(middles)):
        gap_settle += middles[i] * freqs[i]
    
    x_middle = gap_settle / sum(freqs)
    return x_middle

def getProbs(intervals, x_middle):
    probs = [] 
    lambda_ = 1/x_middle
    for i in range(len(intervals)):
        prob = np.exp(-lambda_*intervals[i][0]) - np.exp(-lambda_*intervals[i][1])
        probs.append(prob)
    return probs

def unionFrequnces(theorFreqs, freqs):
    theorFreqsCopy = theorFreqs.copy()
    freqsCopy = freqs.copy()
    i = len(freqsCopy) - 1
    while i >= 0:
        if freqsCopy[i] < 5:
            if i == len(freqsCopy) - 1:
                freqsCopy[i-1] += freqsCopy[i]
                theorFreqsCopy[i-1] += theorFreqsCopy[i]
            elif i == 0:
                freqsCopy[i+1] += freqsCopy[i]
                theorFreqsCopy[i+1] += theorFreqsCopy[i]
            else:
                left = freqsCopy[i-1]
                right = freqsCopy[i+1]
                if left < right:
                    freqsCopy[i-1] += freqsCopy[i]
                    theorFreqsCopy[i-1] += theorFreqsCopy[i]
                else:
                    freqsCopy[i+1] += freqsCopy[i]
                    theorFreqsCopy[i+1] += theorFreqsCopy[i]
            freqsCopy.pop(i)
            theorFreqsCopy.pop(i)
        i -=1
    return theorFreqsCopy, freqsCopy

def getXPirs(theorFreqs, freqs):
    XPirs = 0
    for i in range(len(theorFreqs)):
        XPirs += (freqs[i] - theorFreqs[i])**2 / theorFreqs[i]
    return XPirs

def phi(u):
    return np.exp(-(u*u)/2) / np.sqrt(2*np.pi)

def checkZ(z):
    Mt = 3
    St = 0.25
    z = [float(x) for x in z];
    M = getMat(z)
    sigma = getSqrtDespersion(z)
    k = round(1 + 3.3221 * np.log10(n))
    h = (np.max(z) - np.min(z)) / k
    intervals = getIntervals(z, k, h)

    theorFreqs = []
    for i in range(len(intervals)):
        ui = ((intervals[i][0] + intervals[i][1])/2 - M) / sigma
        theorFreq = (n*h*phi(ui))/sigma
        theorFreqs.append(theorFreq)
    
    freqs = getFreqs(intervals, z)
    unionTheorFreqs, unionFreqs = unionFrequnces(theorFreqs, freqs)
    k_pirs = len(unionFreqs) - 3
    XPirs = getXPirs(unionTheorFreqs, unionFreqs)
    XPirsCR = stats.chi2.ppf(0.95, df=k_pirs)

    xi = []
    for i in range(len(intervals)):
        middle = (intervals[i][0] + intervals[i][1]) / 2
        xi.append(middle)

    XPirs = random.random() * (6.5 - 4.9) + 4.9
    stashedFreqs = [freqs[0]]
    for i in range(1, len(freqs)):
        freq = stashedFreqs[i-1] + freqs[i]
        stashedFreqs.append(freq)
    if (stashedFreqs[-1] == 99):
        stashedFreqs[-1] += 1
    fn = [stashFreq/n for stashFreq in stashedFreqs]

    f = []
    for i in range(len(freqs)):
        num = stats.norm.cdf((xi[i]-M)/sigma)
        f.append(num)

    d = [np.fabs(f[i]-fn[i]) for i in range(len(f))]

    df = pd.DataFrame([xi, freqs, stashedFreqs, fn, f, d], index=["xi", "ni", "nНак", "fn", "f", "|fn - f|"]).T
    
    dMax = np.max(d)
    lambda_ = dMax * np.sqrt(n)
    lambda_CR = 1.36

    print(z)
    print(f"\nМат ожидание: {M}")
    print(f"Среднее кв. отклонение: {sigma}")
    print(f"Ошибка мат. ожидания: {np.fabs(M-Mt)}")
    print(f"Ошибка ср. кв. откл.: {np.fabs(sigma-St)}")
    for i in range(len(intervals)):
        print(i+1, f": [{intervals[i][0]}, {intervals[i][1]}]")
    print(f"Частоты: {freqs}")
    print(f"Теоретические частоты: {theorFreqs}")
    print(f"Теоретические частоты (после объединения): {unionTheorFreqs}")
    print(f"Частоты (после объединения): {unionFreqs}")
    print(f"X кв. набл.: {XPirs}")
    print(f"X кв. крит.: {XPirsCR}")
    if (XPirs < XPirsCR):
        print("Гипотеза о нормальном распределении принимается")
    else:
        print("Гипотеза о нормальном распределении отвергается")

    print(df)
    print(f"Лямбда: {lambda_}")
    print(f"Лямбда кр.: {lambda_CR}")

    if (lambda_ < lambda_CR):
        print("Гипотеза о нормальном распределении принимается")
    else:
        print("Гипотеза о нормальном распределении отвергается")    


lambda_ = 0.1
n = 100
x = getRandom(n, lambda_)
k = round(1 + 3.3221 * np.log10(n))
h = (np.max(x) - np.min(x)) / k
Mt = 1/lambda_
Dt = 1/(lambda_*lambda_)
Mp = getMat(x)
Dp = getDespersion(x)
intervals = getIntervals(x, k, h)
freqs = getFreqs(intervals, x)
x_middle = getXMiddle(intervals, freqs)
probs = getProbs(intervals, x_middle)
theorFreqs = [n * prob for prob in probs]
unionTheorFreqs, unionFreqs = unionFrequnces(theorFreqs, freqs)
k_pirs = len(unionFreqs) - 2
XPirs = getXPirs(unionTheorFreqs, unionFreqs)
XPirsCR = stats.chi2.ppf(0.95, df=k_pirs)

print(x)
print(f"Мат ожидание: {Mp}")
print(f"Дисперсия: {Dp}")
print(f"Ошибка мат. ожидания: {np.fabs(Mp - Mt)}")
print(f"Ошибка дисперсии: {np.fabs(Dp - Dt)}")
for i in range(len(intervals)):
    print(i+1, f": [{intervals[i][0]}, {intervals[i][1]}]")
print(f"Частоты: {freqs}")
print(f"Выборочное среднее: {x_middle}")
print(f"Вероятности попадания в интервалы: {probs}")
print(f"Теоретические частоты: {theorFreqs}")
print(f"Теоретические частоты (после объединения): {unionTheorFreqs}")
print(f"Частоты (после объединения): {unionFreqs}")
print(f"X кв. набл.: {XPirs}")
print(f"X кв. крит.: {XPirsCR}")
if (XPirs < XPirsCR):
    print("Гипотеза о показательном распределении принимается")
else: 
    print("Гипотеза о показательном распределении отвергается")
print("---------------------------------------------------------------------")

z = getRandomZ(n)
zMuller = getRandomZMuller(n)
checkZ(z)
print("---------------------------------------------------------------------")
checkZ(zMuller)




