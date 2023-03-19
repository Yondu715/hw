import numpy as np
import pandas as pd


def y_pr(x, y):
    return np.exp(x-y)-np.exp(x)


def y_toch(x, y):
    return np.log(1+2.7182818*np.exp(-np.exp(x)))


def euler(x1, y1, h):
    x_arr = []
    y_arr = []
    y_t_arr = []
    for _ in range(n + 1):
        x_arr.append(x1)
        y_arr.append(y1)
        y_t_arr.append(y_toch(x1, y1))
        y_prev = y1
        y_next = y1 + h * y_pr(x1, y1)
        y1 = y_prev + h / 2 * (y_pr(x1, y_prev) + y_pr(x1+h, y_next))
        x1 += h
    R = [np.abs(y_t_arr[i] - y_arr[i]) for i in range(len(y_arr))]
    dt = pd.DataFrame([x_arr, y_arr, y_t_arr, R], index=["x", "y", "y_toch", "R"]).T
    return dt


x_range = [0, 1]
x1, y1 = 0, np.log(2)
n = 10
h = (x_range[1] - x_range[0]) / n
x = []
y = []
y_t = []

print("Метод Эйлера")
print("y' = e^(x-y)-e^x")
print("yt = ln[1+2.7182818*e^(-e^x)]")
dt = euler(x1, y1, h)
print(dt)