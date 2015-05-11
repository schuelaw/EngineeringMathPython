from sympy import *
import scipy.integrate as integrate
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

x = Symbol('x')
f = lambdify(x,-abs(x-1/2)+1)
pprint(f(3/4))
pprint(integrate(f(x),(x,0,1)))

#X = np.linspace(0,1,100)
#plt.plot(X,-abs(X-1/2)+1)
#plt.show()
"""
a,b,c,x = symbols('a b c x')

f = lambdify(x,a*x**2 + b*x + c)
df = lambdify(x,diff(f(x),x))

pprint(solve([Eq(df(0),0),Eq(f(1),0)],[a,b,c]))

phi = lambdify(x,1-x**2)
#X = np.linspace(0,1,100)
#plt.plot(X,phi(X))
#plt.show()

RQ = integrate(diff(phi(x),x)**2+x**2*phi(x)**2,
        (x,0,1))/integrate(phi(x)**2,(x,0,1))
pprint(RQ.evalf(16))
"""
