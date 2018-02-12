'''
		   @file: 1-Lagrange_points.py
   		   @date: 17th September 2017
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: 

'''

import numpy as np
import sympy

sympy.init_printing()



# The variables
t 		= sympy.symbols('t')


# Initial conditions
# If the points are given

x 		= np.array((2, 2.75, 4))
y 		= np.array((1.0/2, 1.0/2.75, 1.0/4))
p 		= np.array((3, 2.9))

# The calculations

n = len(x)
L = []
for i in xrange(n):
	Li = 1
	for j in xrange(n):
		if i != j:
			Li *= (t-x[j])/(x[i]-x[j])
	L.append(Li)

f = 0
for i in xrange(n):
	f += L[i] * y[i]
f = sympy.simplify(f)

print "The L functions:"
print L
print "The final function:"
print f
print '\n'

f 		= sympy.lambdify(t, f, "numpy") # Transform the function to lambdify
f 		= f(p)

print "The correct values:"
print 1/p
print "The values calculated by interpolation:"
print f