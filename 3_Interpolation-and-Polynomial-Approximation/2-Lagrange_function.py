'''
		   @file: 2-Lagrange_function.py
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

x 		= np.array((2, 2.75, 4))
f 		= 1/t
p 		= np.array((3, 2.9))

# The calculations

f = sympy.lambdify(t, f, "numpy") # Transform the function to lambdify
y = f(x)

print "The y values:"
print y

n = len(x)
L = []
for i in xrange(n):
	Li = 1
	for j in xrange(n):
		if i != j:
			Li *= (t-x[j])/(x[i]-x[j])
	L.append(Li)

g = 0
for i in xrange(n):
	g += L[i] * y[i]
g = sympy.expand(g)

print "The L functions:"
print L
print "The final function:"
print g
print '\n'

g 		= sympy.lambdify(t, g, "numpy") # Transform the function to lambdify

print "The correct values:"
print f(p)
print "The values calculated by interpolation:"
print g(p)