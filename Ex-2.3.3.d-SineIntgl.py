from sympy import *
from sympy import *

# Good simple examples: https://github.com/sympy/sympy/wiki/Quick-examples

# Declare the symbols in the problem
L, n, x = symbols('L n x')

Q.integer(n)
Q.positive(n)

# Setup and solve the system of equations.
s1=integrate((sin((2*n-1)*x/2))**2,(x,0,pi))



# Show the solution.
print s1
