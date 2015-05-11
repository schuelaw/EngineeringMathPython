import scipy.integrate as integrate
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Test function
def u(x):
    return np.sin(np.pi*x)
def du(x):
    return np.cos(np.pi*x)*np.pi

RQ = integrate.quad(lambda x: du(x)**2,0,1)[0]/integrate.quad(lambda x: u(x)**2,0,1)[0]

exact = np.pi**2

print(RQ,exact)
