'''
		   @file: 7-centered_differences.py
   		   @date: 17th September 2017
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: 

'''

import numpy as np
import sympy
from scipy.special import binom

sympy.init_printing()



# The variables
t, s	= sympy.symbols('t s')

# Initial conditions
x 		= np.array((2, 3, 4))
f 		= 1/t
p 		= np.array((3.1, 2.9))

# The calculations
f 		= sympy.lambdify(t, f, "numpy") # Transform the function to lambdify
y 		= f(x)

print "The y values:"
print y

n 		= len(x)
F		= []
for i in xrange(n):
	F.append([y[i]])
	for j in xrange(1, i+1):
		F[i].append(F[i][j-1] - F[i-1][j-1])

'''
a 		= []
for i in xrange(n):
	a.append(F[i][i]/)

print "The a values:"
print a

g 		= a[n-1] 
for i in xrange(n-1, 0, -1):
	g  *= (t-x[i-1])
	g  += a[i-1]

print "The function:"
print g
g = sympy.expand(g)
print "Expanded:"
print g

g = sympy.lambdify(t, g, "numpy")

print "The correct values:"
print f(p)
print "The values calculated by interpolation:"
print g(p)
'''