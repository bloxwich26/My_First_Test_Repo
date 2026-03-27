import matplotlib.pyplot as plt
import numpy as np

def deriv(x, y):
    N = len(x)
    dY = np.zeros(N-1)
    for k in range(N):
        dY[k-1] = (y[k] - y[k-1])/(x[k]-x[k-1])
    return dY

def integral(x, y):
    n = len(x)
    S = np.zeros(n)
    for k in range(n-1):
        Sk = y[k]*(x[k+1] - x[k])
        S = np.sum(Sk)
    return S
    
T = np.arange(-1, 3, 1)
F = 2 * T + 1

ystrih = deriv(T, F)
xstrih = T[1:]

plt.figure(1)
plt.plot(T, F)
plt.grid()
plt.show(block = False)

plt.figure(2)
plt.plot(xstrih, ystrih)
plt.grid()
plt.show(block = False)

print(integral(T, F))






