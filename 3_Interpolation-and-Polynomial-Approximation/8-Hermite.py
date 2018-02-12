'''
		   @file: 8-Hermite.py
   		   @date: 17th September 2017
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: 

'''

import numpy as np
import sympy
from scipy.special import binom
diff = sympy.diff

sympy.init_printing()



# The variables
t, s	= sympy.symbols('t s')

# Initial conditions
x 		= np.array((2, 3, 4, 5))
f 		= 1/t
df 		= diff(f, t)
p 		= np.array((3.3, 3.7))

# The calculations
f 		= sympy.lambdify(t, f, "numpy") # Transform the function to lambdify
df 		= sympy.lambdify(t, df, "numpy")
y 		= f(x)
dy 		= df(x)

print "The y  values:"
print y
print "The y' values:"
print dy

n 		= len(x)
Q		= []
z 		= []
for i in xrange(n):
	z.append(x[i])
	z.append(x[i])
	Q.append([y[i]])
	Q.append([y[i]])
	Q[2*i+1].append(dy[i])
	if i != 0:
		Q[2*i].append((Q[2*i][0] - Q[2*i-1][0])/(z[2*i]-z[2*i-1]))

for i in xrange(2, 2*n):
	for j in xrange(2, i+1):
			Q[i].append((Q[i][j-1] - Q[i-1][j-1])/(z[i] - z[i-j]))

a 		= []
for i in xrange(2*n):
	a.append(Q[i][i])

print "The a values:"
print a

g 		= a[2*n-1]*(t-x[n-1])
for i in xrange(n-1, 0, -1):
	g  += a[2*i]
	g  *= t-x[i-1]
	g  += a[2*i-1]
	g  *= t-x[i-1]
g 	   += a[0]



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
