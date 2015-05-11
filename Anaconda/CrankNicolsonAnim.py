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
from scipy.linalg import solveh_banded
import matplotlib.animation as animation

# Length of interval.
L = 1
# Thermal conductivity.
k = 1

# Mesh size in x direction
N = 100
dx = L/float(N)
# Step size in time, no stability condition needed.
dt = dx/10
# Number of time steps to compute
M = 100

# Define the initial condition    
def f(x):
    """ Initial temperature. """
    return (np.sin(2*np.pi*x))**2
    #if .25 <= x <=.5:
    #    return 1
    #else:
    #    return 0

# Generate mesh of x values
X = [(j+1)*dx for j in range(N-1)]

# Solution will be a list of lists, one list for each time step.
u = []

# Compute the t=0 list from initial condition, add to list of time steps
q = []
for j in range(N-1):
    q.append(f(dx*(j+1)))
u.append(q)

# Compute subsequent timesteps
s = k*dt/dx**2

# Create banded matrix
A = np.zeros(2*(N-1)).reshape(2,N-1)
for i in range(1,N-1):
    A[0,i]=-s
for i in range(0,N-1):
    A[1,i]=1+2*s

# Compute successive time steps.
for m in range(M):
    d = np.zeros(N-1)
    d[0] = (1-2*s)*u[m][0] + s*u[m][1]
    d[N-2]=s*u[m][N-3] + (1-2*s)*u[m][N-2]
    for j in range(1,N-2):
        d[j]=(s*u[m][j-1] + (1-2*s)*u[m][j] + s*u[m][j+1])
    q = solveh_banded(A,d)
    u.append(q)

fig, ax = plt.subplots()
line, = ax.plot(X,u[0])
def animate(i):
    line.set_ydata(u[i])
    return line,

ani = animation.FuncAnimation(fig,animate,np.arange(1,M),interval=50)

plt.show()
print("time step:", dt)
print("final time:",dt*(M-1))

        
    
    



