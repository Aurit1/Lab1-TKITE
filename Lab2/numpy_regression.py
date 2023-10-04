from numpy import *
import matplotlib.pyplot as plt
import sys

def powers(nums: list, start:int, end:int) -> list: #Returns a matrix with incremental powers
    lis = []
    for e in nums:
        elist = []
        for pow in range(start,end+1):
            elist.append(e**pow)
        lis.append(elist)
    return array(lis)

def poly(a:list, x: list) -> list:  #Computes a list from the koefficients in a and the values in x
    lis = []
    for val in x:
        sum = 0
        for i in range(len(a)):
            sum += (val**i)*a[i]    #Adds the current polynomial term to the sum
        lis.append(sum)
    return lis

X = transpose(loadtxt(sys.argv[1]))[0]
Y = transpose(loadtxt(sys.argv[1]))[1]
n = sys.argv[2]
Xp  = powers(X,0,int(n))
Yp  = powers(Y,1,1)
Xpt = transpose(Xp)

a = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))
a = a[:,0]


X2 = linspace(X[0],X[len(X)- 1],
              (int((X[len(X)-1]- X[0])*5))).tolist() #Difference between the largest and smallest numbers
Y2 = poly(a, X2)                                     #and multiplies it by the step

plt.plot(X,Y,'ro')
plt.plot(X2,Y2)
plt.show()




