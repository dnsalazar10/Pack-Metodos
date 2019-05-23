import numpy as np
import matplotlib.pyplot as plt
import sympy

#Funcion devulve la integral numérica de cos(x)

x=np.linspace(0,np.pi,100)
def f(x):
    return np.sin(x)

def f_p(x):
    return np.cos(x)

plt.plot(x,f_p(x), label="f_prima")
plt.plot(x,f(x), label="f(x)")
plt.legend()

#Foward Diference
def FD(f , x):
    h=x[1]-[0]
    f1=f[1:] #f(x)
    f2=f[0:-1]
    fd= (f1 - f2) / h
    return (fd)

y=FD(f(x),x)
len(y)
x1=x[0:-1]
plt.plot(x1,y)
