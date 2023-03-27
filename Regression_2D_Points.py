# Programmer: 	Raza Bhatti
# Company:	Softgalaxy Technologies Inc.
# Website:	https://www.linkedin.com/in/softgalaxy
#
# Observation or Principle to proposed solutions: There are mostly or always multiple ways to achieve same objective.
#
# Python 3.x AI_ML Program Function: 
# 1. Regression of 2D points.
#
# References:
# 1. https://www.youtube.com/watch?v=J8Eh7RqggsU&list=PLoROMvodv4rO1NB9TD4iUZ3qghGEGtqNX
#

import sys
import time
import numpy as np                          # For numerous floating point numeric use, must install the package as "$ pip install numpy "                                              

#Points=[(2,4), (4,2)]
Points=[(-20,40)] #, (4,2)]                       # 2D Points for which we have a desire to find the optimum path to the least error near the function.

#####################
# Program Functions #
#####################
def find_Error(w):                          # Difference squared, y1=w*x, y2=>actual value of y at a function. Difference => (y1-y2), squared
  return sum( (w*x-y)**2 for x,y in Points)

def derivative_Of_Error(w):            # d [ (x+y) ^ n ] / dx => n(x+y)^(n-1) * (n-1)(x+y) * (n-2)(x+y) ..... till (n-m)=1
  return sum( 2*(w*x-y)*x for x,y in Points)

#--------------------------------------------#
#----Program Starting Point and Main Body----#
#--------------------------------------------#

# Gradient descent

w=0                                             # Starting point for the function F(w)
stepIncrement=0.01                              # Incremental steps towards the solution
#for k in np.arange(0.1, 10, stepIncrement):
print('\n\nBefore Entering Iterative Loop,\t\t')
print('\n\t\t\t w={}\n\n'.format(w))

for k in range(100):                            # Normally some kind of a condition inside an infinite loop to exit once the objective is found.
  #print k
  v =   find_Error(w)
  gradient =   derivative_Of_Error(w)
  w = w - stepIncrement*gradient                # gradient means rate of change and multipying with stepIncrement moves it in reverse direction.
  
  print('iteration:{},\t\t w={},\t\t find_Error(w)={}'.format(k,w,v))
  
  
