###############################################################################
###############################################################################
# Trapezion
#
# Implementation of Trapezioz method to integrate functions
#
#
###############################################################################
###############################################################################

###############################################################################
################################## Modules ####################################
###############################################################################

# Importing Complete Modules

import plotly.graph_objects as go
import math



###############################################################################
########################### Constants and Macros ##############################
###############################################################################


# The extrems of the interval [a,b] of integration
AINIT = 0
BINIT = 1

# The number of subdivisions.
Num_parts = 8

# The number of decimal digits to considering for approximations
CASAS = 7

###############################################################################
# Functions
###############################################################################

# Some examples of functions to be integrate

#def func_x(r): return r
#def func_x(r): return r/(1+r*r)
#def func_x(r): return 1/r
def func_x(r): return math.exp(-r*r)

###############################################################################
# Main
###############################################################################

# Create the parameter vectors
x = []
y = []
n = []

###############################################################################
# Implementation of the method

A = 0 # This variable represents the area, or the approximate value of the integral
h = (BINIT - AINIT)/Num_parts


x.append(round(AINIT,CASAS))
y.append(round(func_x(x[0]),CASAS))
n.append(0)

for j in range(1,Num_parts+1):
    n.append(j)
    x.append(round(AINIT+j*h,CASAS))
    y.append(round(func_x(x[j]),CASAS))

A = h/2*(y[0]+y[Num_parts])
for j in range(1,Num_parts):
    A = A+h*y[j]

# Truncation
A = round(A,CASAS)

n.append('Area')
x.append('=')
y.append(A)

# Table with the values (you can use it, for example, as solution of exercises)
fig = go.Figure(data=[go.Table(header=dict(values=['i', 'x_i','y_i']),
                 cells=dict(values=[n,x,y]))
                     ])
fig.show()








