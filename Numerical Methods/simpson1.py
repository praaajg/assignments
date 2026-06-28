import numpy as np
import math 

def function(x):
    f =  (1/x)
    return f

n = 5
a = 0.1 
b = (math.pi)/2

x = np.linspace(a, b, n+1)
y = np.zeros(n+1)

h = (b -a)/n

for i in range(n+1):
    y[i] = function(x[i])  

I1 = y[0] + y[n] 
I2 = 0 
I3 = 0  

for i in range(1, n):
    if i % 2 == 1:  
        I2 += y[i]
    else:  
        I3 += y[i]

I = (h/3)*(I1 + 4*I2 + 2*I3) 
print(I)