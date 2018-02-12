'''
		   @file: 3-Neville's_iterated.py
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

f 		= sympy.lambdify(t, f, "numpy") # Transform the function to lambdify
y 		= f(x)

print "The y values:"
print y

n 		= len(x)
Q		= []
for i in xrange(n):
	Q.append([y[i]])
	for j in xrange(1, i+1):
		Q[i].append(sympy.simplify(((t-x[i-j])*Q[i][j-1] - (t-x[i])*Q[i-1][j-1])/(x[i]-x[i-j])))

q 		= []
for i in xrange(n):
	q.append(sympy.simplify(Q[i][i]))
	q[i] = sympy.lambdify(t, q[i], "numpy")

print "The Q functions:"
for i in Q:
	print i


print "The correct values:"
print f(p)
print "The values calculated by interpolation:"
for i in xrange(n):
	print "q[" + str(i) + "] = " + str(q[i](p))