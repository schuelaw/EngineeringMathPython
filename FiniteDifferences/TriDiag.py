# -*- coding: utf-8 -*-
"""
Created on Tue May  5 18:40:07 2015

@author: Albert
"""

""" Solve the 1D heat equation using a Crank-Nicolson scheme. """

""" Assuming fixed, homog, BC's """

import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solveh_banded

N=10

A = np.zeros(N*2).reshape(2,N)
print(A)
