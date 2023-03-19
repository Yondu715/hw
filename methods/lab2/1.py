from math import sqrt


def f1(x, y):
    return x**2 - y**2 - 1


def f2(x, y):
    return x * y**3 - y - 4


def fi1(x, y):
    return sqrt(1+y*y)


def fi2(x, y):
    return ((4 + y) / x) ** (1/3)


def getFi1PR(x, y):
    prX = 0
    prY = y/sqrt(y*y+1)
    return prX, prY


def getFi2PR(x, y):
    prX = -(y+4) ** (1/3) / (3 * x ** (4/3))
    prY = 1/(3*x**(1/3)*(y+4)**(2/3))
    return prX, prY


def methodSimpleIter(x0, y0, limXY, eps):
    x1, y1 = getFi1PR(limXY[0], limXY[1])
    x2, y2 = getFi2PR(limXY[0], limXY[1])
    if (abs(x1) + abs(y1) >= 1) or (abs(x2) + abs(y2) >= 1):
        return "error"
    x1 = fi1(x0, y0)
    y1 = fi2(x0, y0)
    n = 1
    while (abs(x1 - x0) > eps) or (abs(y1 - y0) > eps):
        x0 = x1
        y0 = y1
        x1 = fi1(x0, y0)
        y1 = fi2(x0, y0)
        n += 1
    return x1, y1, n


x0 = 1.75
y0 = 1.5
eps = 1e-8
limXY = [2, 1.6]
res = methodSimpleIter(x0, y0, limXY, eps)
if res != "error":
    x = res[0]
    y = res[1]
    n = res[2]
    print("1. x^2 - y^2 - 1 = 0")
    print("2. xy^3 - y - 4 = 0")
    print(f"eps = {eps}")
    print("Метод простых итераций")
    print(f"x = {x}")
    print(f"y = {y}")
    print(f"n = {n}")
    print(f"f1(x, y) = {f1(x, y)}")
    print(f"f2(x, y) = {f2(x, y)}")
