import math
import random
import matplotlib.pyplot as plt
import numpy as np

# 1

t1 = 2
t2 = 1
n = 100

p1 = math.e**(-1/t1 * 1.5)
p2 = math.e**(-1/t2 * 1.5)

pa = p1 * p2
pb = p1 * (1 - p2)
pc = (1 - p1) * (1 - p2)

pa_simulated = 0
pb_simulated = 0
pc_simulated = 0

for i in range(n):
    x1 = random.uniform(0, 1)
    x2 = random.uniform(0, 1)
    if (x1 < p1) and (x2 < p2):
        pa_simulated += 1
    if (x1 < p1) and (x2 >= p2):
        pb_simulated += 1
    if (x1 >= p1) and (x2 >= p2):
        pc_simulated += 1

print("№1")
print("Аналитические вероятности:")
print(f"P(ни один блок не откажет) = {pa}")
print(f"P(откажет только второй блок) = {pb}")
print(f"P(откажут оба блока) = {pc}\n")

print("Вероятности по имитационному моделированию:")
print(f"P(ни один блок не откажет) = {pa_simulated/n}")
print(f"P(откажет только второй блок) = {pb_simulated/n}")
print(f"P(откажут оба блока) = {pc_simulated/n}\n")

# 2
Tn = 100
lambda_ = 8/24
Mx = 10
sigma = 4

train_times = []
train_carriages = []
while sum(train_times) < Tn:
    train_time = random.expovariate(lambda_)
    if sum(train_times) + train_time > Tn:
        break
    train_carriages_count = round(random.normalvariate(10, 4))
    train_times.append(train_time)
    train_carriages.append(train_carriages_count)


print("№2")
print(train_times)
print(f"Кол-во поездов: {len(train_times)}")
print(f"Среднее количество вагонов: {np.mean(train_carriages)}\n")
# plt.eventplot(train_times, color='black')
# plt.xlabel('Время')
# plt.ylabel('Поезда')
# plt.show()

# 3
Tn = 100
Mx = 1.5
sigma = 0.5

lambdaK = 1 / Mx
k = 1 / (sigma ** 2 * lambdaK ** 2)
lambda_ = lambdaK * k
t = 0

lights_time = []

while (t<Tn):
    n = 0
    while n < k:
        r = np.random.uniform()
        T = -1/lambda_ * np.log(r)
        t += T
        n += 1
    lights_time.append(t)
    

print("№3")
print(f"Время выхода из строя лампочек:\n {lights_time}")
print(f"Кол-во сгоревших лампочек за 100 лет: {len(lights_time)}")
print(f"Ожидаемое сгоревших лампочек за 100 лет: {Tn/Mx}")
