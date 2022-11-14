import math

#Función a Integrar 
def f(x):
    f=1/math.sqrt(x)
    return f


#Función para resolver la integral
def simpson13(a,b,n):
    cuenta=1
    h=(b-a)/n #subintervalos
    s=f(a)+f(b)
    for k in range (1,n):
        if cuenta<3:
            s+=3*f(a+k*h)
            cuenta+=1
        else:
            s+=2*f(a+k*h)
            cuenta=1
        
    s *=(3*h/8)
                
    return s



def main():
    a=float(input('límite inferior de la integración: \t'))
    b=float(input('límite superior de la integración: \t'))
    n=int(input('Introduzca subdivisiones: \t\t'))
    print('--------------------------------------------------------')
    s=simpson38(a,b,n)
    print("Valor de la integración numérica de simpson3/8: \t\t",s)
    

main()
