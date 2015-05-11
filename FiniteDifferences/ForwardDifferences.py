# -*- coding: utf-8 -*-
"""
Created on Tue May  5 18:40:07 2015

@author: Albert
"""

""" Solve the 1D heat equation using a forward difference scheme. """

""" Assuming fixed, homog, BC's """

import numpy as np
import matplotlib.pyplot as plt
# Length of interval.
L = 1
# Thermal conductivity.
k = 1

# Mesh size in x direction
N = 100
dx = L/float(N)
X = [j*dx for j in range(N+1)]
# Step size in time, satisfies stability cond dt<=h*h/(2k)
dt = dx*dx/(3.0*k)
# Number of time steps to compute
M = 600

# Define the initial condition    
def f(x):
    """ Initial temperature. """
    #return np.sin(np.pi*x)
    if np.abs(x-.5)<.25:
        return 1
    else:
        return 0
# Solution will be a list of lists, one list for each time step.
V = []

# Compute the t=0 list from initial condition, add to list of time steps
L = []
for j in range(N+1):
    L.append(f(X[j]))
V.append(L)

# Compute subsequent timesteps
s = k*dt/dx**2
for m in range(M):
    # Left BC zero.
    L = [0]
    # Interior points.
    for j in range(1,N):
        L.append(s*V[m][j-1] + (1-2*s)*V[m][j] + s*V[m][j+1])
    # Right BC zero.
    L.append(0)
    V.append(L)

plt.ylim(0,1.5)
for m in range(M):
    plt.plot(X,V[m])
plt.show()
print("time step:", dt)
print("final time:",dt*(M-1))

        
    
    



