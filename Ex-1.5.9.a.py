#import scipy.constants as sc
#import scipy.integrate as integrate
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Follows example 1.5.9 in Haberman 5th.
T1=1; T2=0; r1=1; r2=3;

# Steady state function to plot
def u(r):
    return np.log(r)*(T1-T2)/np.log(r1/r2) \
            + T1 - np.log(r1)*(T1-T2)/np.log(r1/r2)

t1 = np.linspace(r1,r2,100)
# Function plot
plt.plot(t1,u(t1))
plt.title(r'LTS, Radially Symmetric',fontsize=20)
plt.show()

