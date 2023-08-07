import numpy as np
import pandas as pd

def U_t0(x):
    return x*x


def U_x0(t):
    return 0


def U_x1_t(t):
    return 1


a, b = 0, 1
n = 10
k = 200
T = 1
h = (b - a) / n
t = T / k
r = t / (h * h)

x_i = np.arange(0, 1, h)
t_i = np.arange(0, 1, t)


setka = np.zeros([len(t_i), len(x_i)])

for i in range(len(x_i)):
    setka[0][i] = U_t0(x_i[i])

for t in range(len(setka)-1):
    for x in range(len(setka[i])):
        if (x == 0):
            setka[t, 0] = 0
            continue
        if (x == len(setka[i]) - 1):
            setka[t+1, x] = setka[t+1, x-1] + h
            continue
        setka[t+1, x] = r * (setka[t, x+1] + setka[t, x-1]) + (1 - 2*r)*setka[t, x]

df = pd.DataFrame(setka)
print(df)
