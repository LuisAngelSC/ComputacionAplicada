import numpy as np
import sys
import math

print('-------------')
n=0 #Variable del tamaño de la matriz
n=int(input("Introduzca la dimención de la Matriz M:"))

#Aseguro que el dato ingresado es correcto, si no lo vuelvo a pedir
while n<3:
    print('\nERROR La Matriz debe de ser mínimo de 3 \n')
    n=int(input("Introduzca la dimención de la Matriz M:"))


m=n**2 ##cantidad de números primos que se requieren
M = np.zeros((1,m)) #vector donde se generaran la cantidad de números primos
A = np.zeros((n,n)) #Matriz con la que se va a trabajar

num=0 #variable donde se identificara si el valor es primo o no
primo=False

for i in range (0,m): 
    primo=False
    while primo==False:
        
        if num<2:
            primo=False
            
        elif num==2:
            primo=True
            M[0][i]=num
            
        else:
            for j in range(2,num):
                if num % j==0:
                    primo=False
                    break
                primo=True
                M[0][i]=num
        num+=1           
                    
c=0;

#Los valores de la lista se pasan a una matriz con la que trabajar
for i in range (n):
    for j in range (n):
        A[i][j]=M[0][c]
        c+=1

#se Calculan la suma de los valores en y por encima de la diagonal
suma=0;
for i in range (n):
    for j in range (n):
        if j>= i:
            suma=suma+A[i][j]



print('La matriz A de números primos es: \n',A)
print('La suma de los elementos en la matriz diagonal superior es:',suma)