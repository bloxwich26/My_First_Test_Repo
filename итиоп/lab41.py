import numpy as np
import matplotlib.pyplot as plt

# t <= -pi< f(t) = sin(t)
T1 = np.arange(-2*np.pi, -np.pi, 0.01)
F1 = np.sin(T1)

# -pi < t <= 0, f(t) = 0
T2 = np.array([-np.pi, 0])
F2 = np.array([0, 0])

# 0 < t <= 1, f(t) = t
T3 = np.array([0, 1])
F3 = np.array([0, 1])

# 1 < t <= 2, f(t) = 2 - t
T4 = np.array([1, 1.2, 2])
F4 = 2 - T4

# t > 2, f(t) = -sin(t - 2)
T5 = np.arange(2, 2*np.pi, 0.01)
F5 = -np.sin(T5 - 2) 

plt.figure(1)
plt.title('График кусочно заданной функции')
plt.grid()
plt.plot(T1, F1, 'g', label = 'f(t)', lw = '2')
plt.plot(T2, F2, 'g', lw = '2')
plt.plot(T3, F3, 'g', lw = '2')
plt.plot(T4, F4, 'g', lw = '2')
plt.plot(T5, F5, 'g', lw = '2')
plt.show(block = False)
plt.xlabel('t')
plt.ylabel('f') 
plt.legend()
