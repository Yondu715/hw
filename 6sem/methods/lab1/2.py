import math


def f(x):
    return math.sqrt(x) - math.cos(0.387 * x)


def fi(x):
    return math.cos(0.387 * x)**2


def simpleIterations(a, b, eps):
    x1 = fi(a)
    x2 = 1
    n = 0
    while abs(x2-x1) > eps:
        temp = x2
        x2 = fi(x1)
        x1 = temp
        n += 1
    return x2, n


a = 0.5
b = 1.5
eps = 1e-3
x, n = simpleIterations(a, b, eps)

print("f(x) = x * log10(x) - 1.2")
print(f"[{a}, {b}]")
print(f"eps = {eps}")
print("Метод простых итераций")
print(f"x = {x}")
print(f"n = {n}")
print(f"f(x) = {f(x)}")
