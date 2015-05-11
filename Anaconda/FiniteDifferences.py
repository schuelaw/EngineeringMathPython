# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt

# Function whose derivative we are approximating
def f(x):
    return np.sin(x)

def df(x):
    return np.cos(x)

# Define the domain interval [a,b]
a=0
b=2*np.pi

# Number of subintervals
N = 50
# Mesh size, Delta x
h = (b-a)/N
# Create a mesh with N subintervals
X = [a+h*i for i in range(0,N+1)]

# Apply f(x) to every mesh point, put result in list F
F = f(X)

# Approximate the derivative at left endpoint, O(h)
dF = [(F[1]-F[0])/h]
# Approximate the derivative at interior points, O(h^2)
for i in range(1,N):
    dF.append((F[i+1]-F[i-1])/(2*h))
# Approximate the derivative at right endpoint, O(h)
dF.append((F[N]-F[N-1])/h)

#print(F)

# Set the range along vertical.
plt.axes(ylim=(-1.5,1.5))
# Plot f(x)
plt.plot(X,F, color="red")
# Plot finite difference f'(x)
plt.plot(X,dF, color="blue")
# Plot actual f'(x)
plt.plot(X,df(X),color="green")
plt.show()
