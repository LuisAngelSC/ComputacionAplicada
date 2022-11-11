import numpy as np
import math
from random import random
from random import gauss
from matplotlib import pyplot as plt
from matplotlib import cm

def f(x1,x2,x3):
    f = x1+2*x2+x2*x3-x1**2-x2**2-x3**2
    return f


def evol(u,v,w):
    plt.figure(1)
    plt.plot(u)
    plt.plot(v)
    plt.plot(w)
    plt.legend(('x1','x2','x3'))
    plt.ylim([-2, 2])
    
    plt.show()

def mutation(x,s):
    xn = x+s*gauss(0,1)
    while xn < -2 or xn > 2:
        xn = x+s*gauss(0,1)
    return xn

def sigma(s,g,m):
    ps = m/g
    c = 0.817
    if g%20 == 0:
    #if True:
        if ps > 0.2:
            s = s/c
        elif ps < 0.2:
            s = s*c
        else:
            s = s
    else:
        s = s
    return s
    
def main():

    x1min, x1max, x2min, x2max, x3min, x3max  = [-2, 2, -2, 2, -2, 2]
    gmax = 500;           #máximo número de iteraciones
    m = 0;                 #número de mutaciones exitosas
    c = 0.817;
    x1 = 4 * random() + x1min
    x2 = 4 * random() + x2min
    x3 = 4 * random() + x3min
    x10x20x30 = [round(x1, 6), round(x2, 6), round(x3, 6)]
    print("x10,x20,x30: ", x10x20x30)
    padre = f(x1, x2, x3)
    s = 1
    u = [x1]
    v = [x2]
    w = [x3]
    
    for g in range(1,gmax):
        x1n = mutation(x1, s)
        x2n = mutation(x2, s)
        x3n = mutation(x3, s)
        hijo = f(x1n, x2n, x3n)
        if hijo > padre:
            x1 = x1n
            x2 = x2n
            x3 = x3n
            m += 1               #mutación exitosa
            padre = f(x1, x2, x3)
        else:
            x1 = x1
            x2 = x2
            x3 = x3
            m = m
        s = sigma(s,g,m)
        u.append(x1)
        v.append(x2)
        w.append(x3)
        
    x1fx2fx3f = [round(x1, 6), round(x2, 6), round(x3, 6)]
    print("x1f,x2f,x3 : ", x1fx2fx3f)
    #print("u: ",u)
    #print("v: ",v)

    evol(u,v,w)
    
main()