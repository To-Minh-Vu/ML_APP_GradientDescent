#Gradient Descent
import numpy as np
import math

def grad(x):
    return 6*x + 2 + 4*np.cos(x)
def cost(x):
    return 3*x*x + 2*x + 4*np.sin(x)
def my_Grad_Des(anpha, x0):
    x = [x0]
    for i in range(100):
        x_new = x[-1] - anpha*grad(x[-1])
        if abs(grad(x_new)) < 1e-3:
            break
        x.append(x_new)
    return x, i

x1, i1 = my_Grad_Des(0.1, -5)
print('x_min = %f,  cost(x) = %f,  so lan lap %d'%(x1[-1], cost(x1[-1]), i1))

x2, i2 = my_Grad_Des(0.1, 5)
print('x_min = %f,  cost(x) = %f,  so lan lap %d'  %(x2[-1], cost(x2[-1]), i2))

x3, i3 = my_Grad_Des(0.01, -1)
print('x_min = %f,  cost(x) = %f,  so lan lap %d' %(x3[-1], cost(x3[-1]), i3))