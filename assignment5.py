from scipy.interpolate import interp1d
import math
import numpy as np
import matplotlib.pyplot as plt

#create a function that takes an input, x, and returns the value f(x)
def funtion(x):
    return x**3 - ((math.e)**(-x))
    
#define x as 5 values in between .5 and 1, and y as the output of those values, f(a)
x = np.arange(.5, 1, .1)
y = funtion(x)

#create two variables, f and f2, that can calculate linear and cubic interpolation
f = interp1d(x, y, fill_value='extrapolate')
f2 = interp1d(x, y, kind='cubic', fill_value='extrapolate')

#create a new x variable with 100 numbers in between .5 and 1
xnew = np.linspace(.5, 1, 100)

#plot the original data, linear interpolation, and cubic interpolation. Also add a legend.
plt.plot(x, y, 'o', xnew, f(xnew), '-', xnew, f2(xnew), '--')
plt.legend(['data', 'linear', 'cubic'], loc='best')
plt.show()
