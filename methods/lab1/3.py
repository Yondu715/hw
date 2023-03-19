from math import log10, log


def f(x):
    return x * log10(x) - 1.2

def f2(x):
	return 1/log(10)*x


def hord(a, b, eps):
	tmp = f2(a)
	if (tmp * f(a) > 0):
		x0 = b
		static = a
	else:
		x0 = a
		static = b
	xn = x0 - f(x0)/(f(x0) - f(static)) * (x0 - static)
	n = 1
	while (abs(xn - x0)) > eps:
		x0 = xn
		xn = x0 - f(x0)/(f(x0) - f(static)) * (x0 - static)
		n += 1
	return xn, n


a = 2
b = 3
eps = 1e-9
x, n = hord(a, b, eps)

print("f(x) = x * log10(x) - 1.2")
print(f"[{a}, {b}]")
print(f"eps = {eps}")
print("Метод хорд")
print(f"x = {x}")
print(f"n = {n}")
print(f"f(x) = {f(x)}")
