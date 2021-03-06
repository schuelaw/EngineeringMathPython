import scipy.integrate as integrate
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from cmath import *

tempData = open("rollingTemperatures.txt","r")

# Read temperature data, first line
line = tempData.readline()
L = line.split()
times = [0]
temps = [float(L[1])]

# Remaining lines
startTime = L[0]
while True:
    # Get next line
    line = tempData.readline()
    if len(line)==0: break
    L = line.split()
    t = int(L[0]) - int(startTime)
    times.append(t)
    temps.append(float(L[1]))

tempData.close()

# nth complex discrete Fourier coefficient
def c(n,t,s):
    N = len(times)
    C = complex(0,0)
    for k in range(1,N):
        C+=complex(temps[k],0)* exp(complex(0,n*2*pi*k/(N-1)))
    C /= (N-1) 
    return C
    

N=30
freq=[k for k in range(1,N)]
coeffs=[abs(c(k,times,temps)) for k in range(1,N)]

# Plot Fourier series and initial temp distribution.
plt.plot(freq,coeffs)
plt.title(r'Discrete Fourier Coeffs',fontsize=20)
plt.show()

