# -*- coding: utf-8 -*-
"""
Created on Tue May  5 18:40:07 2015

@author: Albert
"""

""" Solve the 1D heat equation using a Crank-Nicolson scheme. """

""" Assuming fixed, homog, BC's """

import sys
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
# Step size in time, no stability condition needed.
dt = dx
# Number of time steps to compute
M = 10

# Define the initial condition    
def f(x):
    """ Initial temperature. """
    #return np.sin(np.pi*x)
    if x<=L/2.0:
        return x
    else:
        return L-x

# Solution will be a list of lists, one list for each time step.
u = []

# Compute the t=0 list from initial condition, add to list of time steps
q = []
for j in range(N+1):
    q.append(f(X[j]))
u.append(q)

# Compute subsequent timesteps
s = k*dt/dx**2

A = np.zeros((N-1,N-1))
# Main diagonal
for i in range(N-1):
    A[i][i] = 1 + 2*s

# Super- and sub-diagonals
for i in range(1,N-1):
    A[i-1][i] = -s
    A[i][i-1] = -s


   
# Compute successive time steps.
for m in range(M):
    # Build the right-hand side vector
    d=[0 for i in range(N+1)]
    q=[0 for i in range(N+1)]
    for j in range(1,N):
        d[j]=(s*u[m][j-1] + (1-2*s)*u[m][j] + s*u[m][j+1])
    soln = np.linalg.solve(A,d[1:len(d)-1])
    for j in range(1,N):
        q[j] = soln[j-1]
    u.append(q)

plt.ylim(0,1.5)
for m in range(M):
    plt.plot(X,u[m])
plt.show()
print("time step:", dt)
print("final time:",dt*(M-1))

        
    
    



