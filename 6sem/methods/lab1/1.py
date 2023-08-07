from math import log10


def f(x):
    return x * log10(x) - 1.2


def dihotomy(a, b, eps):
    mid = None
    n = 0
    while (abs(f(a)-f(b)) > 2*eps):
        mid = (a+b)/2
        if (abs(f(mid)) < 2*eps):
            return mid, n
        elif (f(mid) * f(a) < 0):
            b = mid
        elif (f(mid) * f(b) < 0):
            a = mid
        n += 1


a = 2
b = 3
eps = 1e-3
x, n = dihotomy(a, b, eps)

print("f(x) = x * log10(x) - 1.2")
print(f"[{a}, {b}]")
print(f"eps = {eps}")
print("Метод дихотомии")
print(f"x = {x}")
print(f"n = {n}")
print(f"f(x) = {f(x)}")
