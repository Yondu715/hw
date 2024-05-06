import numpy as np

nn = 100
NN = 500
nnT = 100
NNT = 200
errors = 0

def randomFloat(a, b):
    return np.random.uniform(a, b)

def scalar(a, b, nab):
    value = 0
    for i in range(nab):
        value += a[i] * b[i]
    return value

def phi(y):
    if (y > 0):
        return 1
    return -1;

def c_cc(a, b, nab):
    value = 0
    for i in range(nab):
        value += np.power(a[i] - b[i], 2)
    return np.sqrt(2 * value / (scalar(a, a, nab) + scalar(b, b, nab)))

# def y_Zc(y, z, c, n, N):
#     value = 0
#     err = 0
#     for i in range(N):
#         sc = phi(scalar(z[i], c, n))
#         if (y[i] * sc < 0):
#             err += 1
#         value += np.power(y[i] - sc, 2)
#     print('Кол-во ошибок:', err, "Ошибка:", err / N)
#     return np.sqrt(value / scalar(y, y, N))

def y_Zc(y, z, c, n, N):
    global errors
    value = 0
    for i in range(N):
        sc = phi(scalar(z[i], c, n))
        if (y[i] * sc < 0):
            errors += 1
        value += np.power(y[i] - sc, 2)
    return value / scalar(y, y, N) / 4


def form_z_c_y(eps, cc, y, z, n, N):
    for i in range(n):
        for j in range(N):
            z[j][i] = randomFloat(-1, 1)
    for i in range(N):
        y[i] = phi(scalar(z[i], cc, n))

    cy = 3 * np.sqrt(scalar(y, y, N) / N) * eps
    for i in range(N):
        y[i] += randomFloat(0, 1) * cy

def form_A_Y(Y, A, y, z, n, N):
    for i in range(n):
        Y[i] = 0
        for j in range(N):
            Y[i] += z[j][i] * y[j]
    for i in range(n):
        for j in range(n):
            A[i][j] = 0
            for k in range(N):
                A[i][j] += z[k][i] * z[k][j]

def invers_A(a, n, al):
    h = list(range(nn))
    p = 0
    for i in range(1, n+1):
        p += a[i-1][i-1]
    p = p / n * al
    for i in range(1, n+1):
        a[i-1][i-1] += p
    for k in range(n, 0, -1):
        p = a[0][0]
        for i in range(2, n+1):
            q = a[i-1][0]
            if i > k:
                h[i-1] = q / p
            else:
                h[i-1] = -q / p
            for j in range(2, i+1):
                a[i-2][j-2] = a[i-1][j-1] + q * h[j-1]
        a[n-1][n-1] = 1 / p
        for i in range(2, n+1):
            a[n-1][i-2] = h[i-1]
    for i in range(1, n+1):
        for j in range(1, n+1):
            a[i-1][j-1] = a[j-1][i-1]

def sigmo(s):
    return 1 / (1 + np.exp(-s))

n = nn
N = NN
nT = nnT
NT = NNT

z = [[0] * n for _ in range(N)]
zT = [[0] * nT for _ in range(NT)]
A = [[0] * n for _ in range(n)]
ccopt = [0] * n
y = [0] * N
Y = [0] * n
yT = [0] * NT
c0 = [0] * n
C = [0] * n
ccc = [0] * n
h = 0.001
al = 0.05

k0 = 10000
k1 = 5000
nc = n // 3
nzz = 1

nzz = 1
eps = 0
np.random.seed(17)
print(" Razmer n=", n, " Dannie N=", N)
if nzz == 1:
    print(" delenie zz", nzz, " Pogrechnost eps =", eps)
if nzz == 0:
    print(" no delenie zz", nzz, " Pogrechnost eps =", eps)
for i in range(n):
    C[i] = randomFloat(0, 1)
for i in range(n):
    ccopt[i] = 0
for i in range(nc):
    ccopt[i] = i
form_z_c_y(eps, ccopt, y, z, n, N)
form_z_c_y(0, ccopt, yT, zT, nT, NT)

# al = 0.1
# print("  al=", al, "  Regularizacia Tixonova c*=((M+alI)**-1)*Y")
# for k in range(1, 5):
#     form_A_Y(Y, A, y, z, n, N)
#     invers_A(A, n, al)
#     for i in range(n):
#         ccc[i] = 0
#         for j in range(n):
#             ccc[i] += A[i][j] * Y[j]
#     norm = c_cc(ccc, ccopt, n)
#     norm1 = y_Zc(y, z, ccc, n, N)
#     norm1T = y_Zc(yT, zT, ccc, nT, NT)
#     print("al=", al, "|| c* - c || =", norm, "  norm1=", norm1, "  norm1T=", norm1T)
#     al = al / 10

# k0 = 5000
# h = 0.001
# print("k0=", k0, "  h=", h, "  NOU Regularizacia")
# for i in range(n):
#     c0[i] = randomFloat(0, 1)
# for i in range(n):
#     C[i] = c0[i]
# for k in range(k0):
#     for j in range(N):
#         sc = scalar(z[j], C, n)
#         czz = scalar(z[j], z[j], n)
#         for i in range(n):
#             if nzz == 1:
#                 C[i] = C[i] + h * (y[j] - sc) * z[j][i] / czz
#             if nzz == 0:
#                 C[i] = C[i] + h * (y[j] - sc) * z[j][i]
#     norm = c_cc(ccopt, C, n)
#     norm1 = y_Zc(y, z, C, n, N)
#     norm1T = y_Zc(yT, zT, C, nT, NT)
#     if k % 1000 == 0:
#         print("k= =", k, "  al=", al, "|| c* - c || =", norm, "  norm1=", norm1, "  norm1T=", norm1T)

k1 = 5000
h = 0.001
al = 0.1
# al=0.001
for i in range(n):
    C[i] = c0[i]
# print("  al=", al, "  h=", h, "  Regularizacia Tixonova Iteracia")
# for k in range(k1):
#     for j in range(N):
#         sc = scalar(z[j], C, n)
#         czz = scalar(z[j], z[j], n)
#         for i in range(n):
#             if nzz == 1:
#                 C[i] = C[i] * (1 - al) + h * (y[j] - sc) * z[j][i] / czz
#             if nzz == 0:
#                 C[i] = C[i] * (1 - al) + h * (y[j] - sc) * z[j][i]
#     norm = c_cc(ccopt, C, n)
#     norm1 = y_Zc(y, z, C, n, N)
#     norm1T = y_Zc(yT, zT, C, nT, NT)
#     if k % 1000 == 0:
#         print("k=", k, "  al=", al, "|| c* - c || =", norm, "  norm1=", norm1, "  norm1T=", norm1T)

print("  al=", al, "  h=", h, "  Regularizacia Tixonova Iteracia")
for k in range(k1 + 1):
    for j in range(N):
        sc = scalar(z[j], C, n)
        fi = sigmo(sc)
        ff = 2 * fi - 1
        dff = 2 * fi * (1 - fi) * (ff - y[j])
        for i in range(n):
            C[i] = C[i] - h * dff * z[j][i]
    norm = c_cc(ccopt, C, n)
    norm1 = y_Zc(y, z, C, n, N)
    print('Кол-во ошибок:', errors, "Ошибка:", errors / N)
    errors = 0
    norm1T = y_Zc(yT, zT, C, nT, NT)
    print('Кол-во ошибок(тест):', errors, "Ошибка:", errors / N)
    errors = 0
    if k % 1000 == 0:
        print("k=", k, "  al=", al, "|| c* - c || =", norm, "  norm1=", norm1, "  norm1T=", norm1T)
