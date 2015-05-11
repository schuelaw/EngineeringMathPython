from scipy.optimize import fsolve
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Plot Fourier series and initial temp distribution.
h=1
L=1
xmax = 4*np.pi
t1 = np.linspace(0,xmax,200)
plt.ylim(-10,10)
plt.plot(t1,[np.tan(L*x) for x in t1])
plt.plot(t1,[0 for x in t1],color='black')
plt.plot(t1,[-x/h for x in t1],color='red')
plt.title(r'BCs of 3rd Kind',fontsize=20)
#plt.show()

# Solve numerically using Newton's method.
eigenvalCond = lambda l : np.tan(L*l) + l/h
initialGuess = 2
for i in range(5):
    print("(h={0})".format(h),fsolve(eigenvalCond,initialGuess),
            "(h=0): ", str((i+0.5)*np.pi))
    initialGuess = initialGuess + np.pi
