from sympy import *
from sympy import *

# Symbolic solution of a 2x2 linear system of equations.  Actually solves
# 1.5.9.a Haberman 5th.  Needs python2 since sympy doesn't work with
# python3 in linux.

# Good simple examples: https://github.com/sympy/sympy/wiki/Quick-examples

# Declare the symbols in the problem
T1, T2, r1, r2, c1, c2 = symbols('T1 T2 r1 r2 c1 c2')

# Setup and solve the system of equations.
s=solve([Eq(T1,c1*log(r1)+c2),Eq(T2,c1*log(r2)+c2)],[c1,c2])

# Show the solution.
print s
