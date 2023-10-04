from matrix import *
import matplotlib.pyplot as plt
import sys



X = transpose(loadtxt(sys.argv[1]))[0]
Y = transpose(loadtxt(sys.argv[1]))[1]

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
