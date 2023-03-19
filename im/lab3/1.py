from random import random
import numpy as np


def getRandom(n, lamb):
    x = []
    for _ in range(n):
        num = -1/lamb * np.log(random())
        x.append(num)
    return x


def getInters(x, k, h):
    minimal = np.min(x)
    inters = []
    for _ in range(k):
        inters.append([minimal, minimal + h])
        minimal += h
    return inters


def getProbs(mean, inters):
    mark_lamb = 1/mean
    probs = []
    for inter in inters:
        prob = np.exp(-mark_lamb*inter[0]) - np.exp(-mark_lamb*inter[1])
        probs.append(prob)
    return probs


def getIntersAndFreqs(x, k, h):
    freqs = []
    minimal = np.min(x)
    inters = []
    for _ in range(k):
        n = []
        for i in x:
            if (i >= minimal and i <= minimal + h):
                n.append(i)
        inters.append([minimal, minimal + h])
        minimal += h
        freqs.append(len(n))
    return freqs, inters


def getXPirs(pracFreqs, teorFreqs):
    tmp = []
    new_pracFreq = 0
    new_teorFreq = 0
    for i in range(len(pracFreqs)):
        if pracFreqs[i] < 5:
            tmp.append(i)
            new_pracFreq += pracFreqs[i]
            new_teorFreq += teorFreqs[i]
    tmp.reverse()
    for idx in tmp:
        pracFreqs.pop(idx)
        teorFreqs.pop(idx)
    pracFreqs.append(new_pracFreq)
    teorFreqs.append(new_teorFreq)
    print(pracFreqs)
    print(teorFreqs)
    x = 0
    for i in range(len(pracFreqs)):
        x += (pracFreqs[i] - teorFreqs[i]) ** 2 / teorFreqs[i]
    return x


lamb = 0.1
n = 100
x = getRandom(n, lamb)
k = round(1 + 3.3221*np.log10(n))
h = (np.max(x) - np.min(x)) / k
pracFreqs, inters = getIntersAndFreqs(x, k, h)
mean = np.mean(inters)
probs = getProbs(mean, inters)
teorFreqs = [n*probs[i] for i in range(len(probs))]
print(getXPirs(pracFreqs, teorFreqs))
