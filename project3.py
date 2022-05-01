import math
import matplotlib.pyplot as plt
import numpy as np

#Create 2 functions, one that takes an input, a, and returns the output of the function, f(a). Another that does the same for the derivative of the function, f'(a)
def equation(a):
    answer = math.sin(a) - (math.e ** (-a))
    return answer

def derivativeEquation(a):
    answer = math.cos(a) + (math.e ** a)
    return answer

#bisection method
#declare variables xl and xu - the starting boundaries, and xmOld which is the first root estimate in the method. Then store variables to track the number of iterations and the points on the table/graph.
xl = 0
xu = math.pi / 2
xmold = (xl + xu) / 2
bisIterations = 0
biXValues = []
biYValues = []

#loop until tolerance level is met
while True:
    #using eqResult determine the new boundaries for the next iteration
    eqResult = equation(xl) * equation(xmold)
    if eqResult < 0:
        xu = xmold
    elif eqResult > 0:
        xl = xmold
    elif eqResult == 0:
        break
    
    #calculate the new root estimate using the midpoint formula
    xmnew = (xl + xu) / 2

    #calculate |epsilon| and check if the target tolerance is met
    bisEpsilon = abs((xmnew - xmold) / xmnew)
    if bisEpsilon < .000001:
        break
    
    #redefine xm and increment the iterations needed
    xmold = xmnew
    bisIterations += 1
    biXValues.append(bisIterations)
    biYValues.append(xmnew)




#newton's method
#declare variables xi, starting estimate, and variable to track number of iterations, and points on the table/graph
xi = 0
newtIteration = 0
newtxValues = []
newtyValues = []

#loop until tolerance is met
while True:
    #calculate the new estimate using xi - f(xi)/f'(xi)
    xiNew = xi - (equation(xi) / derivativeEquation(xi))
    
    #calculate |epsilon| and check if it meets tolerance level
    newtEpsilon = abs((xiNew - xi) / xiNew) * 100
    if newtEpsilon < .000001:
        break

    #redefine xi and increment the iterations counter. Also add points to the list for graphing.
    xi = xiNew
    newtIteration += 1
    newtxValues.append(newtIteration)
    newtyValues.append(xi)




#secant method
#declare the first estimate as pi/2 and variables to store the number of iterations done.
xi = math.pi / 2
prevxi = 0
iteration = 0
secxValues = []
secyValues = []

#loop untile tolerance is met.
while True:
    #calculate the new estimate using xi - (f(xi)(xi-xi-1) / (f(xi) - f(xi-1)))
    newxi = xi - ((equation(xi) * (xi - prevxi)) / (equation(xi) - equation(prevxi)))
    #calculate |epsilon| and check if it meets tolerance level
    epsilon = abs((newxi - xi) / newxi) * 100
    if epsilon < .000001:
        break
    
    #redefine values from iteration and increment iterations counter. Also ad points to array.
    prevxi = xi
    xi = newxi
    iteration += 1
    secxValues.append(iteration)
    secyValues.append(xi)


#plot and label all points from all three methods.
plt.plot(biXValues, biYValues, label="Bisection method")
plt.plot(newtxValues, newtyValues, label="Newton's method")
plt.plot(secxValues, secyValues, label="Secant method")
plt.legend()
plt.show()

