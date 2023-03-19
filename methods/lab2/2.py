def f1(x, y):
    return x**2 - y**2 - 1


def f2(x, y):
    return x * y**3 - y - 4


def getF1PR(x, y):
    prX = 2 * x
    prY = -2 * y
    return prX, prY


def getF2PR(x, y):
    prX = y ** 3
    prY = 3 * x * y * y - 1
    return prX, prY


def getJacobian(x, y):
    x1, y1 = getF1PR(x, y)
    x2, y2 = getF2PR(x, y)
    jacobian = x1 * y2 - x2 * y1
    return jacobian


def getHL(x, y, jacobian):
    prX1, prY1 = getF1PR(x, y)
    prX2, prY2 = getF2PR(x, y)
    h = -1/jacobian * (f1(x, y) * prY2 - f2(x, y) * prY1)
    l = -1/jacobian * (prX1 * f2(x, y) - prX2 * f1(x, y))
    return h, l


def methodNewton(x0, y0, eps):
    jacobian = getJacobian(x0, y0)
    if jacobian == 0:
        return "error"
    h, l = getHL(x0, y0, jacobian)
    x1 = x0 + h
    y1 = y0 + l
    n = 1
    while (abs(x1-x0) > eps or abs(y1-y0) > eps):
        x0, y0 = x1, y1
        h, l = getHL(x0, y0, jacobian)
        x1 = x0 + h
        y1 = y0 + l
        n += 1
    return x1, y1, n


x0, y0 = 1.75, 1.5
eps = 1e-8
res = methodNewton(x0, y0, eps)
if res != "error":
    x = res[0]
    y = res[1]
    n = res[2]
    print("1. x^2 - y^2 - 1 = 0")
    print("2. xy^3 - y - 4 = 0")
    print(f"eps = {eps}")
    print("Метод Ньютона")
    print(f"x = {x}")
    print(f"y = {y}")
    print(f"n = {n}")
    print(f"f1(x, y) = {f1(x, y)}")
    print(f"f2(x, y) = {f2(x, y)}")
