import scipy.integrate as integrate
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Generate Fourier series for function on [-L,L]

# Plot resolution, number of points in interval partition.
R=200

# Number of terms to generate.
N=100

# Set radius of interval
L=1

# Piecewise smooth function to be approximated
def f(x):
    return x
# mth Fourier cosine coefficient
def A(m):
    return (1.0/L)*integrate.quad(lambda x: \
            f(x)*np.cos(m*np.pi*x/L),-L,L)[0]

# mth Fourier sine coefficient
def B(m):
    return (1.0/L)*integrate.quad(lambda x: \
            f(x)*np.sin(m*np.pi*x/L),-L,L)[0]

# Generate first N Fourier cosine coefficients.
a = [A(0)/2]+[A(m) for m in range(1,N+1)]

# Generate first N Fourier sine coefficients.
b = [0]+[B(m) for m in range(1,N+1)]

def U(x):
    s = a[0]
    for i in range(1,N+1):
        s+=a[i]*np.cos(i*np.pi*x/L)
        s+=b[i]*np.sin(i*np.pi*x/L)
    return s

# Plot Fourier series and initial temp distribution.
t1 = np.linspace(-L,L,R)
plt.plot(t1,[U(x) for x in t1])
plt.plot(t1,[f(x) for x in t1])
plt.title(r'Fourier Series',fontsize=20)
plt.show()

