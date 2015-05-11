#import scipy.constants as sc
#import scipy.integrate as integrate
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Follows example 1.4.1.f in Haberman 5th.
L = 1
T = 0

# Steady state function to plot
def u(x):
    return -x**4/12 + L**3*x/3 + T

t1 = np.linspace(0,L,100)
# Function plot
plt.plot(t1,u(t1))
plt.text(0,.3,r'LTS: $u(x) = -\frac{x^4}{12} + \frac{L^3}{3} x + T$',fontsize=20)
plt.text(0,.25,r'$u(0)=T,\ u_x(L)=0$',fontsize=20)
plt.xlim(-0.1,L+0.1)
plt.ylim(-0.1,0.5)
# Bar representation
plt.plot([0,1],[0,0],linewidth=2.0,color='k')
plt.show()

