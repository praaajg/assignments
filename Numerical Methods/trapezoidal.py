import math
import numpy as np

def function(x):
    f = math.sqrt(math.sin(x))
    return f

n = 20
a = 0 
b = (math.pi)/2

x = np.linspace(a, b, n+1)
y = np.zeros(n+1)
for i in range(n+1):
    y[i] = function(x[i])

I1 = y[0] + y[n]
I2 = 0

for i in range(1, n):
    I2 = I2 + y[i]

h = (b-a)/n

I_trap = (h/2)*(I1 + 2*I2)
print(I_trap)