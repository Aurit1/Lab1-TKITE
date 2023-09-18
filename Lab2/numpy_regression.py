from matrix import *
import matplotlib.pyplot as plt
import numpy as np

X = transpose(loadtxt('chirps.txt'))[0]
Y = transpose(loadtxt('chirps.txt'))[1]

Xp  = powers(X,0,1)
Yp  = powers(Y,1,1)
Xpt = transpose(Xp)

[[b],[c]] = matmul(invert(matmul(Xpt,Xp)),matmul(Xpt,Yp))

Y2 = []
for e in X:
    Y2.append(b+e*c)

plt.plot(X,Y,'ro')
plt.plot(X,Y2)
plt.show()