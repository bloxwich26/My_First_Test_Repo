import numpy as np
import matplotlib.pyplot as plt

# 0 <= t <= pi/4, f(t) = 4 * e**(-3 * t) * tg(t) 
T = np.arange(0, np.pi/4, 0.01)
F = 4 * np.exp(-3 * T) * np.tan(T)
t1 = 0.2
t2 = 0.4
t3 = 0.6
f1 = 4 * np.exp(-3 * t1) * np.tan(t1)
f2 = 4 * np.exp(-3 * t2) * np.tan(t2)
f3 = 4 * np.exp(-3 * t3) * np.tan(t3)

max_index = np.argmax(F)
max_x = T[max_index]
max_y = F[max_index]

plt.plot(T, F, 'y', label = 'f(t)', lw = 2,)
plt.grid()
plt.xlabel('t')
plt.ylabel('f(t)')
plt.show(block = False)
plt.title('Функция напряжения')
plt.legend()
plt.plot(max_x, max_y, 'ro', label = 'max')

print('F(0.2) = ', f1,';', 'F(0.4) = ', f2,';', 'F(0.6) = ', f3)

