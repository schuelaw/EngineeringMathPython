# -*- coding: utf-8 -*-
"""
Created on Sun Feb  8 09:02:57 2015

@author: Albert
"""
import scipy.integrate as integrate
import numpy as np
import matplotlib.pyplot as plt

# Additional stuff for 3d plotting
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter


# Number of terms in partial sum
N=20

# Resolution in each direction
Rr = 50
Rtheta = 50


# Plot surface in first example Haberman 2.5.2, polar laplacian, radius of
# domain is a
radius=1

# BC1
def f(t):
    #return (np.pi-t)*(np.pi+t)
    return (np.sin(3*t))**2
    #if t>np.pi/2 or t<-np.pi/2:
    #    return 1
    #else:
    #    return 0


# Fourier coefficients
a=[]
b=[]
    
# mth Fourier cosine coefficient, eq 2.5.47, m=1,2,3...
def A(m):
    return integrate.quad(lambda t: f(t)*np.cos(m*t)/np.pi,-np.pi,np.pi)[0]
# mth Fourier sine coefficient, eq 2.5.47, m=1,2,3...
def B(m):
    return integrate.quad(lambda t: f(t)*np.sin(m*t)/np.pi,-np.pi,np.pi)[0]
            
# A_0 term
a = [A(0)/2]

# Generate Fourier cosine coefficients.
for m in range(1,N+1): a.append(A(m))
# Generate Fourier sine coefficients.
for m in range(1,N+1): b.append(B(m))

def U(r,theta):
    s = 0
    for n in range(N+1): s+=a[n]*r**n*np.cos(n*theta)
    for n in range(1,N+1): s+=b[n-1]*r**n*np.sin(n*theta)
    return s

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# create supporting points in polar coordinates
r = np.linspace(0,radius+0.1,Rr)
p = np.linspace(-np.pi,np.pi,Rtheta)
R,P = np.meshgrid(r,p)
# transform them to cartesian system
X,Y = R*np.cos(P),R*np.sin(P)

Z = U(R,P)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.YlGnBu_r)
#ax.set_zlim3d(0, 1)
#ax.set_xlabel(r'$\phi_\mathrm{real}$')
#ax.set_ylabel(r'$\phi_\mathrm{im}$')
#ax.set_zlabel(r'$V(\phi)$')
plt.show()

