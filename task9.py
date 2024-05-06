import numpy as np
import matplotlib.pyplot as plt

#1
x = np.linspace(0, 10, 1000)
f_1 = np.sin(x)
f_2 = np.cos(x)
f_3 = np.exp(-x)
plt.plot(x, f_1, c='r', ls='solid')
plt.plot(x, f_2, c='g', ls='dashed')
plt.plot(x, f_3, c='b', ls='dotted')
plt.legend(["sin(x)", "cos(x)", "exp(-x)"], loc="lower right")
plt.show()

#2
A = np.random.random((100,2))
col = np.where(A[0:100,0]**2 + A[0:100,1]**2 < 1,'g','r')
area = (np.abs(A[0:100,0]) + np.abs(A[0:100,1]))
plt.scatter(A[0:100,0], A[0:100,1], c=col, s=area)
plt.show()
