import numpy as np

#1
A = np.arange(0.0, 1.1, 0.1)
B = np.zeros((5,6), dtype=np.int16)
x = complex(0,1)
lst = [x**i for i in range(9)]
C = np.array(lst)
print(A)
print(B)
print(C)

#2
v1 = np.arange(0, 11, 1)
v2 = v1[1::2]
v3 = v1[::-1]
print(v1)
print(v2)
print(v3)

#3
m1 = np.linspace(0, 20, num=20, dtype=np.int16)
m1 = m1.reshape(4,5)
m2 = m1[::,::-1]
m3 = m1[::-1,::]
temp = np.delete(m1, np.s_[0:4:3], 0)
m4 = np.delete(temp, np.s_[0:5:4], 1)
print(m1)
print(m2)
print(m3)
print(m4)
