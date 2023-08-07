import numpy as np
import pandas as pd
from runge import runge


def y_pr(x, y):
    return np.exp(x-y)-np.exp(x)


def y_toch(x, y):
    return np.log(1+2.7182818*np.exp(-np.exp(x)))


def adams(x1, y1, h, f):
    x_arr = []
    y_arr = []
    y_t_arr = []
    for i in range(4):
        x_arr.append(x1)
        y_arr.append(f.iloc[i, 1])
        y_t_arr.append(f.iloc[i, 2])
        x1 += h
    y1 = y_arr[-1]
    x1 = x_arr[-1]
    for i in range(3, n):
        y_p = y1 + h * (55*y_pr(x1, y1) - 59*y_pr(x1-h,
                        y_arr[i-1]) + 37*y_pr(x1-2*h, y_arr[i-2]) - 9*y_pr(x1-3*h, y_arr[i-3])) / 24
        f_p = y_pr(x1+h, y_p)
        y1 += h * (9*f_p + 19*y_pr(x1, y1) - 5 *
                   y_pr(x1-h, y_arr[i-1]) + y_pr(x1-2*h, y_arr[i-2])) / 24
        y_arr.append(y1)
        x1 += h
        y_t_arr.append(y_toch(x1, y1))
        x_arr.append(x1)
    

    R = [np.abs(y_t_arr[i] - y_arr[i]) for i in range(len(y_arr))]
    dt = pd.DataFrame([x_arr, y_arr, y_t_arr, R],
                      index=["x", "y", "y_toch", "R"]).T
    return dt


x_range = [0, 1]
x1, y1 = 0, np.log(2)
n = 10
h = (x_range[1] - x_range[0]) / n
x = []
y = []
y_t = []

print("Метод Адамса")
print("y' = e^(x-y)-e^x")
print("yt = ln[1+2.7182818*e^(-e^x)]")
f = runge(x1, y1, h).loc[:3]
dt = adams(x1, y1, h, f)
print(dt)
