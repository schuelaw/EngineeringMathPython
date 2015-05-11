import scipy.integrate as integrate
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Follows example in Section 2.3 in Haberman 5th.  Heat equation,
# u(x,0)=f(x), u(0,t)=u(L,t)=0

# Plot resolution, number of points in interval partition.
R=200

# Number of terms to generate.
N=100

# Length of rod
L=1

# Initial temperature distribution.
def f(x):
    return x
    
# mth Fourier cosine coefficient, eq 2.3.35
def B(m):
    return (2.0/L)*integrate.quad(lambda x: \
            f(x)*np.cos(m*np.pi*x/L),0,L)[0]

# Generate the 0th coeff:
b=[B(0)/2.0]

# Generate remaining N Fourier cosine coefficients.
for m in range(1,N+1): b.append(B(m))

def U(x):
    s = 0
    for i in range(N+1):
        s+=b[i]*np.cos(i*np.pi*x/L)
    return s

# Plot Fourier series and initial temp distribution.
t1 = np.linspace(-2*L,2*L,4*R)
plt.plot(t1,[U(x) for x in t1])
plt.plot(t1,[f(x) for x in t1])
plt.title(r'Cosine Series',fontsize=20)
plt.show()

