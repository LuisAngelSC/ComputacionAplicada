import numpy as np
import sys

n=3
#a = np.zeros((n,n+1))
a=np.array([[0.25,0.15,0.0,1.5],[0.45,0.5,0.75,5.0],[0.3,0.35,0.25,3.0]])
print(a)

D = np.zeros((n,n))
for i in range(n):
    for j in range(n):
       D[i][j] = a[i][j]
delta = np.linalg.det(D)
print("Det(A): \n",round(delta,3))

for k in range(n):
    Dk = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if j==k:
                Dk[i][j] = a[i][n]
            else:
                Dk[i][j] = a[i][j]           
    #print("D"+str(k)+":\n",Dk)
    x = np.linalg.det(Dk)/delta
    print("x"+str(k+1)+":\n",round(x,3))