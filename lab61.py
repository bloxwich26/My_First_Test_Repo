# Задания 1, 2
import matplotlib.pyplot as plt
import numpy as np

x0 = [100, 400, 400, 500, 500, 200, 200, 100, 100]
y0 = [400, 400, 500, 500, 550, 550, 500, 500, 400]
plt.figure(1)
plt.plot(x0, y0)
plt.grid(1)
plt.xlim([0, 1000])
plt.ylim([0, 1000])
plt.show(block=False)

N=65*40
P=0

for k in range(N):
    X = np.random.rand()*1000
    Y = np.random.rand()*1000
    if (X >= 100 and X <= 400 and Y >= 400 and Y <= 500) or (X >= 200 and X <= 500 and Y >= 500 and Y <= 550):
        P = P + 1
        plt.plot(X, Y, 'r+')
    else:
        plt.plot(X, Y, 'g+')
print('Среднее число попаданий в год:', P/40)

# Задание 3
Ndop = 6
I = 0
for i in range(1, 1000):
    p = 0
    No = 0
    while (p < Ndop):
        X = np.random.rand()*1000
        Y = np.random.rand()*1000
        No += 1
        if (X >= 100 and X <= 400 and Y >= 400 and Y <= 500) or (X >= 200 and X <= 500 and Y >= 500 and Y <= 550):
            p += 1
    I += No
print(I/1000)
        
    

        


