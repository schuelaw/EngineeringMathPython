# -*- coding: utf-8 -*-
"""
Created on Tue May  5 18:40:07 2015

@author: Albert
"""

""" Solve the non-uniform 1D heat equation using a Crank-Nicolson scheme. """

""" Assuming fixed, homog, BC's """

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve_banded
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
M = 500

# Define the thermal conductivity, p(x)>0
def p(x):
    return np.sin(np.pi*x/L)

# Define the source term, q(x)
def q(x):
    if .25 <= x <= .5:
        return 10
    else:
        return 0

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
Q = []
for j in range(N-1):
    Q.append(f(dx*(j+1)))
u.append(Q)

# Convenient constant. :)
s = k*dt/2.0/dx**2

# Create banded matrix
A = np.zeros(3*(N-1)).reshape(3,N-1)

# Super diagonal
for j in range(1,N-1):
    A[0,j]=-s*p(X[j]+dx/2.0)
# Main diagonal
for j in range(0,N-1):
    A[1,j]=1+s*p(X[j]-dx/2.0) + s*p(X[j]+dx/2.0) - dt*q(X[j])
# Sub diagonal
for j in range(0,N-2):
    A[2,j]=-s*p(X[j]-dx/2.0)

# Compute successive time steps.
for m in range(M):
    d = np.zeros(N-1)
    d[0] = (1-s*p(X[0]-dx/2.0) - s*p(X[0]+dx/2.0) + dt*q(X[0]))*u[m][0] \
            + s*p(X[0]+dx/2.0)*u[m][1]
    d[N-2]=s*p(X[N-2]-dx/2.0)*u[m][N-3] + \
            (1-s*p(X[N-2]-dx/2.0) - s*p(X[N-2]+dx/2.0) + dt*q(X[N-2]))*u[m][N-2]
    for j in range(1,N-2):
        d[j]=s*p(X[j]-dx/2.0)*u[m][j-1] \
                + (1-s*p(X[j]-dx/2.0) - s*p(X[j]+dx/2.0) + dt*q(X[j]))*u[m][j] \
                + s*p(X[j]+dx/2.0)*u[m][j+1]
    Q = solve_banded((1,1),A,d)
    u.append(Q)

fig, ax = plt.subplots()
line, = ax.plot(X,u[0])
def animate(i):
    line.set_ydata(u[i])
    return line,

ani = animation.FuncAnimation(fig,animate,np.arange(1,M),interval=50)

plt.show()
print("time step:", dt)
print("final time:",dt*(M-1))

        
    
    



