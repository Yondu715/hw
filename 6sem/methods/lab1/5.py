from math import log10, log


def f(x):
    return x * log10(x) - 1.2


def f2(x):
    return 1/log(10)*x


def f1(x):
    return log(x)/log(10) + 1/log(10)


def newton(a, b, eps):
    tmp = f2(a)
    if (tmp * f(a) > 0):
        x0 = a
    else:
        x0 = b
    xn = x0 - f(x0)/f1(x0)
    n = 1
    while (abs(xn - x0)) > eps:
        x0 = xn
        xn = x0 - f(x0)/f1(x0)
        n += 1
    return xn, n

def cheb(a, b, eps):
    tmp = f2(a)
    if (tmp * f(a) > 0):
        x0 = a
    else:
        x0 = b
    xn = x0 - f(x0)/f1(x0) - (f2(x0)* f(x0) * f(x0)) / (2 * (f1(x0)) ** 3)
    n = 1
    while (abs(xn - x0)) > eps:
        x0 = xn
        xn = x0 - f(x0)/f1(x0) - (f2(x0) * f(x0) * f(x0)) / (2 * (f1(x0)) ** 3)
        n += 1
    return xn, n


a = 2
b = 3
eps = 1e-5
x, n = newton(a, b, eps)

print("f(x) = x * log10(x) - 1.2")
print(f"[{a}, {b}]")
print(f"eps = {eps}")
print("Метод Ньютона")
print(f"x = {x}")
print(f"n = {n}")
print(f"f(x) = {f(x)}")


x, n = cheb(a, b, eps)
print("Метод Чебышева")
print(f"x = {x}")
print(f"n = {n}")
print(f"f(x) = {f(x)}")
