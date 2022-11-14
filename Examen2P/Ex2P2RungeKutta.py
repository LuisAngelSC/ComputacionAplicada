import math

def f(x,y):
    f=x**2+y**2 #función a evaluar
    return f


def k(x,y,h): #Funcion para obtener las k
    k1=h*f(x,y)
    k2=h*f((x+h/2),(y+k1/2))
    k3=h*f((x+h/2),(y+k2/2))
    k4=h*f(x+h,y+k3)
    k=(1/6)*(k1+2*k2+2*k3+k4)
    return k
    


def main():
    
    xf = 0.8
    h = 0.01
    x = 0
    y = 1
    
    while x<=xf:
        
        print('x:\t','%.2f'%x)
        print('y('+'%.2f'%x+'):','%.6f'%y)
        print('-----------------')
        y += k(x,y,h)
        x += h
    print('x:\t','%.2f'%x)
    print('y('+'%.2f'%x+'):','%.6f'%y)

main()