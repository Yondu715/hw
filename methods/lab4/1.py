import pandas as pd


def F(x):
    return 2*x*x


def P(x):
    return -0.5


def Q(x):
    return 3


a = 1
b = 1.3
n = 20
k1 = 1
k2 = 2
l1 = 1
l2 = 0
R1 = 0.6
R2 = 1
h = (b - a) / n

x = []
Ai = []
Bi = []
Ci = []

for i in range(n + 1):
    x.append(a + h * i)
    Ai.append(1 / (h * h) - P(x[i]) / (2 * h))
    Bi.append(2 / (h * h) - Q(x[i]))
    Ci.append(1 / (h * h) + P(x[i]) / (2 * h))

v1 = -k2 / (k1 * h - k2)
w1 = (h * R1) / (k1 * h - k2)
v2 = l2 / (l1 * h + l2)
w2 = (h * R2) / (l1 * h + l2)

alpha = [v1]
beta = [w1]

for i in range(n):
    alpha.append(-Ci[i+1] / (Ai[i+1] * alpha[i] - Bi[i+1]))
    beta.append((F(x[i+1]) - Ai[i+1] * beta[i]) /
                (Ai[i+1] * alpha[i] - Bi[i+1]))

y = [(v2 * beta[n] + w2) / (1 - v2 * alpha[n])]

for i in range(n - 1, -1, -1):
    y.append(alpha[i] * y[n - (i + 1)] + beta[i])

y.reverse()
kray1 = k1 * y[0] + k2 * ((y[1] - y[0]) / h)
kray2 = l1 * y[-1] + l2 * ((y[-1] - y[-2]) / h)
df = pd.DataFrame([x, y, alpha, beta],
                  index=["x", "y", "alpha", "beta"]).T

print("Метод Сеток")
print("y'' + xy' + y = x + 1")
print("Краевые условия:")
print("\ty(0.5) + 2y'(0.5) = 1")
print("\ty'(0.8) = 1.2")
print(f"a = {a} b = {b}")
print(f"h = {h} n = {n}")
print(f"k1 = {k1} k2 = {k2}")
print(f"l1 = {l1} l2 = {l2}")
print(f"R1 = {R1} R2 = {R2}")
print("F = x + 1")
print(f"v1 = {v1} v2 = {v2}")
print(f"w1 = {w1} w2 = {w2}")
print(df)
print("Проверка краевых условий")
print(kray1)
print(kray2)
