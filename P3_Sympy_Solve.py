# library needed to run sympy
import scipy
# importing library sympy to solve equations 
import sympy

## this program solves system of equations

# creating new symbols x and x that can be used in further equation
x = sympy.symbols('x')
y = sympy.symbols('y')
# assigning numners to letters A, B and C
A = 1
B = 3
C = 6

# creating an equation xeq that will solve based on value x 
xeq = sympy.solve(A*(1-x-y) + B*x + C*y - 4,x)[0]
print ('x = %s' % xeq)

# creating an equation yeq that will solved based on value y 
yeq = sympy.solve(A*(1-x-y) + B*x - (8-C)*y,y)[0]
print ('y = %s' % yeq)

# solving system of equations using ysolve
ysolve = 0.5

# solving to get teh x value
xval = xeq.subs(y, ysolve)
print ('If y = %f, x = %f' % (ysolve, xval))

# solving for the y value
yval = yeq.subs(x, xval)
print ('If x = %f, y = %f' % (xval, yval))



