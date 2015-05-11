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
N=50

# Resolution in each direction
Rx = 200
Ry = 200


# Plot surface in first example Haberman 2.5.1
H=1
L=1

# BC1
def g(y):
    if y>H/2 and y<3*H/4: return 1
    else: return 0 
    
# mth Fourier sine coefficient, eq 2.3.35
def A(m):
    return (2.0/(H*np.sinh(-m*np.pi*L/H)))*integrate.quad(lambda y: \
            g(y)*np.sin(m*np.pi*y/H),0,H)[0]
            
# Generate Fourier coefficients.
a=[]
for m in range(1,N+1): a.append(A(m))

def U(x,y):
    s = 0
    for i in range(1,N+1):
        s+=a[i-1]*np.sin(i*np.pi*y/H)*np.sinh(i*np.pi*(x-L)/H)
    return s

# Plot Fourier series and initial temp distribution.
"""
t1 = np.linspace(0,H,Ry)
plt.plot(t1,[U(0,y) for y in t1])
plt.plot(t1,[g(y) for y in t1])
plt.title(r'Fourier Series',fontsize=20)
plt.show()
"""

# 3d plot stuff
fig = plt.figure()
ax = fig.gca(projection='3d')
X = np.linspace(0,L, 30)
Y = np.linspace(0,H, 30)
X, Y = np.meshgrid(X, Y)
R = U(X,Y)
surf = ax.plot_surface(X, Y, R, rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0, antialiased=False)
#ax.set_zlim(-1.01, 1.01)

#ax.zaxis.set_major_locator(LinearLocator(10))
#ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()