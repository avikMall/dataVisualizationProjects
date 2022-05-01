import math

#define the initial xl and xu variables as the starting interval
xl = -1
xu = 2

#create a function - equation() - that given a value, x, computes the value f(x) 
def equation(x):
    answer = 2 - ((x ** 2) * math.sin(x))
    return answer

#loop for 3 iterations
for i in range(3):
    #compute xm, the midpoint of xl and xu
    xm = (xl + xu) / 2
    #calculate the eqResult, or f(m)*f(l)
    eqResult = equation(xm) * equation(xl)

    #redefine xl and xu based on whether eqResult is positive or negative
    if eqResult > 0:
        xl = xm
    elif eqResult < 0:
        xu = xm
    elif eqResult == 0:
        break

#print the results
print(xl, xu, xm)
