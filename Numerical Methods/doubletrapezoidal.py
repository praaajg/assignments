import math
import numpy as np

print("Examples: 'x+y', 'x*y', 'x**2 + y**2', 'math.exp(x+y)', 'math.sin(x)*math.cos(y)'")
func_input = input('Enter a function of x and y: ')

def func(x, y):
    try:
        return eval(func_input)
    except:
        print("Error: Invalid function. Using default function x+y")
        return x + y

n = 20

a = 0
b = 2
c = 0
d = 1

x = np.linspace(a, b, n+1)
y = np.linspace(c, d, n+1)

z = np.zeros((n+1, n+1))

for i in range(n+1):
    for j in range(n+1):
        z[j, i] = func(x[i], y[j])  

row = np.zeros(n+1, dtype=int)
column = np.zeros(n+1, dtype=int)

mul_table = np.zeros((n+1, n+1), dtype=int)

def fill(array):
    array[0] = 1
    last_index = len(array) - 1
    array[last_index] = 1
    for i in range(1, last_index):
        array[i] = 2
    return array

row = fill(row)
column = fill(column)

for i in range(n+1):
    for j in range(n+1):
        mul_table[j, i] = row[i] * column[j]

I1 = 0
for i in range(n+1):
    for j in range(n+1):
        I1 += mul_table[j, i] * z[j, i] 

h = (b-a)/n 
k = (d-c)/n  
I = (h/2) * (k/2) * I1
print(f"Result of double integration: {I}")
print(f"Step sizes: h = {h}, k = {k}")