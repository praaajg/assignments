import numpy as np
import math

print("Examples: 'x+y', 'x*y', 'x**2 + y**2', 'math.exp(x+y)', 'math.sin(x)*math.cos(y)'")
func_input = input('Enter a function of x and y: ')

def func(x, y):
    try:
        return eval(func_input)
    except:
        print("Error: Invalid function. Using default function x+y")
        return x + y

n = 4  
m = 4  

a = 0    
b = 2    
c = 0    
d = 1    

x = np.linspace(a, b, n+1)
y = np.linspace(c, d, m+1)

h = (b - a) / n
k = (d - c) / m

z = np.zeros((m+1, n+1))

for i in range(n+1):
    for j in range(m+1):
        z[j, i] = func(x[i], y[j])

def get_simpson_weights(size):
    weights = np.zeros(size)
    weights[0] = 1      
    weights[-1] = 1     
    
    for i in range(1, size-1):
        if i % 2 == 1:  
            weights[i] = 4
        else:           
            weights[i] = 2
    return weights

x_weights = get_simpson_weights(n+1)
y_weights = get_simpson_weights(m+1)

weight_matrix = np.outer(y_weights, x_weights)

print("\nFunction values matrix:")
print(z)
print("\nWeight matrix:")
print(weight_matrix)

I1 = 0
for i in range(n+1):
    for j in range(m+1):
        I1 += weight_matrix[j, i] * z[j, i]

I = (h/3) * (k/3) * I1

print(f"\nStep sizes: h = {h}, k = {k}")
print(f"Result of double Simpson integration: {I}")

if func_input == "1":
    analytical = (b-a) * (d-c)
    print(f"Analytical result for f(x,y)=1: {analytical}")
    print(f"Error: {abs(I - analytical)}")
elif func_input == "x+y":
    analytical = (b**2 - a**2)/2 * (d-c) + (b-a) * (d**2 - c**2)/2
    print(f"Analytical result for f(x,y)=x+y: {analytical}")
    print(f"Error: {abs(I - analytical)}")
