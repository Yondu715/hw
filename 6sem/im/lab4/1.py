import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import random


def num1():
    P_A = 0.8
    P_B = 0.7
    P_C = 0.95
    P_D = 0.85
    P_E = 0.9
    P_F = 0.7

    P = (1 - (1 - P_A) * (1 - P_B)) * P_C * (1 - (1 - P_D) * (1-P_E) * (1-P_F))

    N = 100
    p_arr = np.zeros((N, 6))
    for i in range(N):
        for j in range(6):
            p_arr[i][j] = np.random.rand()

    P_MC = 0
    for i in range(N):
        if (p_arr[i][0] < P_A or p_arr[i][1] < P_B) and (p_arr[i][2] < P_C) and (p_arr[i][3] < P_D or p_arr[i][4] < P_E or p_arr[i][5] < P_F):
            P_MC += 1
    P_MC /= N

    print(f"Вероятность безотказной работы всей системы: {P}")
    print(f"Вероятность безотказной работы системы (Монте-Карло): {P_MC}")
    print(f"|P - P*| = {abs(P-P_MC)}")
    print("------------------------------------------------------------------")


def num2():
    N = 100
    N1 = 2
    N2 = 3
    N3 = 5
    k = N1 + N2 + N3
    P_H = np.array([N1, N2, N3]) / k
    P_AH = np.array([0.8, 0.9, 0.95])

    P = 0
    for i in range(len(P_H)):
        P += P_AH[i]*P_H[i]

    p_arr = np.zeros((N, 3))
    h_arr = np.zeros(N)
    for i in range(N):
        h_arr[i] = np.random.rand()
        for j in range(3):
            p_arr[i][j] = np.random.rand()
    P_MC = 0
    for i in range(N):
        probs = p_arr[i]
        h = h_arr[i]
        if (probs[0] < P_AH[0] and h < P_H[0]) or (probs[1] < P_AH[1] and P_H[0] <= h < P_H[0] + P_H[1]) or (probs[2] < P_AH[2] and (P_H[2] <= h < P_H[0] + P_H[1] + P_H[2])):
            P_MC += 1
    P_MC /= N

    print(f"Вероятность обнаружения сбоя: {P}")
    print(f"Верояность обнаружения сбоя (Монте-Карло): {P_MC}")
    print(f"|P - P*| = {abs(P-P_MC)}")
    print("------------------------------------------------------------------")


def num3():

    def f1(x):
        num = -1 + x*x
        for i in range(len(num)):
            if num[i] < 0:
                num[i] = -(np.abs(num[i]) ** (1/3))
            else:
                num[i] = num[i] ** (1/3)
        return num

    def f2(x):
        return 1-x

    def f1_cond(x, y):
        return -x*x+y*y*y

    def f2_cond(x, y):
        return x+y

    N = [10, 100, 1000, 10000, 100000]
    a, b = -2, 2
    S0 = (abs(a) + abs(b)) ** 2
    S_MC = []
    S = 6.84359
    t = []
    for n in N:
        k = 0
        for _ in range(n):
            x = random.uniform(a, b)
            y = random.uniform(a, b)
            if (f1_cond(x, y) < -1 and f2_cond(x, y) < 1):
                k += 1
        St = S0 * k/n
        S_MC.append(St)
        t.append(abs(St-S)/S)

    df = pd.DataFrame([N, S_MC, t], index=[
        "Кол-во испытаний", "Площадь (Монте-Карло)", "Погрешность"]).T
    print(f"Площадь фигуры (контр. знач.): {S}\n")
    print(df)
    print("------------------------------------------------------------------")

    x_range = np.arange(-3, 3.01, 0.01)
    x = np.arange(-2, 2.01, 0.01)
    y = np.arange(-2, 2.01, 0.01)
    y_range = f1(x)
    y_range2 = f2(x)

    fig, ax = plt.subplots()
    ax.plot(x_range, f1(x_range))
    ax.plot(x_range, f2(x_range))
    ax.fill_between(x, y_range, -2, color="grey")
    ax.fill_between(x, y_range2, f1(x), color="white")
    ax.add_patch(Rectangle((-2, -2), 4, 4, fill=False, edgecolor="red"))
    plt.grid(True)
    plt.show()


def num4():
    N = 1000
    demands = [10000, 20000, 40000, 60000]
    probs = [0.1, 0.35, 0.3, 0.25]
    profit_arr = np.zeros(len(demands))

    for i in range(len(demands)):
        for _ in range(N):
            p = np.random.uniform()
            if (0 <= p < 0.1):
                demand_t = demands[0]
            elif (0.1 <= p < 0.45):
                demand_t = demands[1]
            elif (0.45 <= p <= 0.75):
                demand_t = demands[2]
            elif (0.75 <= p < 1):
                demand_t = demands[3]
            profit = 0
            if (demands[i] == 10000):
                profit = 10000 * 2.5
            if (demands[i] == 20000):
                if (demand_t == 10000):
                    profit = 10000 * 2.5 - 1.3 * 10000
                else:
                    profit = 20000 * 2.5
            if (demands[i] == 40000):
                if (demand_t == 10000):
                    profit = 10000 * 2.5 - 30000 * 1.3
                elif (demand_t == 20000):
                    profit = 20000 * 2.5 - 1.3 * 20000
                else:
                    profit = 40000 * 2.5
            if (demands[i] == 60000):
                if (demand_t == 10000):
                    profit = 10000 * 2.5 - 50000 * 1.3
                elif (demand_t == 20000):
                    profit = 20000 * 2.5 - 1.3 * 40000
                elif (demand_t == 40000):
                    profit = 40000 * 2.5 - 1.3 * 20000
                else:
                    profit = 60000 * 2.5
            profit_arr[i] += profit

        profit_arr[i] /= N

    df = pd.DataFrame([demands, probs, profit_arr], index=[
        "Спрос", "Вероятность", "Средняя прибыль"]).T
    index = df["Средняя прибыль"].idxmax(0)
    print(df)
    print(f"Наименее рискованное решение находится под индексом: {index}")
    print("------------------------------------------------------------------")


def num5():
    N = 100000
    material = 20
    machine1, machine2 = 5, 4
    R11, R12 = 0.08, 0.12
    R21, R22 = 0.03, 0.06
    expenses1, expenses2 = 3, 2
    price = 35
    profit = 0
    expenses = 0
    good_pr = 0

    for _ in range(N):
        r1 = np.random.rand()
        expenses += material + machine1
        if (r1 < R11):
            continue
        if (r1 < R11 + R12):
            expenses += expenses1
        expenses += machine2
        r21 = np.random.rand()
        r22 = np.random.rand()
        first_cond = r21 < R21
        second_cond = r22 < R22
        if (first_cond and second_cond):
            continue
        if (first_cond and not second_cond) or (not first_cond and second_cond):
            expenses += expenses2
        profit += price
        good_pr += 1

    prob_good = good_pr / N
    profit -= expenses
    profit /= N
    print(f"Вероятность выпуска годной детали: {prob_good}")
    print(f"Средняя прибыль предприятия от выпуска одной детали: {profit}")
    print("------------------------------------------------------------------")


# num1()
# num2()
# num3()
num4()
# num5()
