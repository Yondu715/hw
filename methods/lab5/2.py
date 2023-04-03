import numpy as np
import pandas as pd


def U_t0(x):
    return x*x


def U_x0(t):
    return 0


def U_x1_t(t):
    return 1


def kray(row):
    A = r
    B = 1 + 2*r
    C = r
    
    F = [-x for x in row]
    p = [0 for _ in range(len(row))]
    q = [0 for _ in range(len(row))]

    for j in range(len(row)-1):
        p[j+1] = -C/(A*p[j]-B)
        q[j+1] = (F[j]-A*q[j]) / (A*p[j] - B)

    new_row = [0 for _ in range(len(row))]
    new_row[-1] = 1
    for j in range(len(row) - 2, 0, -1):
        new_row[j] = p[j+1]*new_row[j+1]+q[j+1]

    return new_row


a, b = 0, 1
n = 10
k = 10
T = 1
h = (b - a) / n
tay = T / k
r = tay / (h * h)

x_i = np.arange(0, 1+h, h)
t_i = np.arange(0, 1+h, tay)


setka = np.zeros([len(t_i), len(x_i)])
for i in range(len(x_i)):
    setka[0][i] = U_t0(x_i[i])

for t in range(len(setka)-1):
    setka[t+1] = kray(setka[t])

df = pd.DataFrame(setka)
print(df)
