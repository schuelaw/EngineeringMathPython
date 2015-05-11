import scipy.constants as sc
import scipy.integrate as integrate
import numpy
from matplotlib import *
import math

# Follows example 2.3.7 in Haberman 5th, homog. BC's, Fourier sine series.


# Set the initial temperature profile here.
def f(x):
    return x*(1-x)

# Length of rod
L = 1
# Thermal properties
k = 1

# Space: sine functions
def phi(x,n):
    return math.sin(n*sc.pi*x/L)

# Time: exp functions
def psi(t,n):
    return math.exp(-k*pow(n*sc.pi/L,2)*t)

# Fourier sine coefficients
def B(n):
    return (integrate.quad(lambda x: phi(x,n)*f(x),0,L))[0]

# Number of terms in series
N = 10


# Truncated solution
def U(x,t):
    s = 0
    for n in range(N+1):
        s += B(n)*phi(x,n)*psi(t,n)

t = arange(0,2,0.01)
plot(t,phi(t,1))
show()
