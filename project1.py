#Avik Malladi Project 1
#PROBLEM 1

#import math library in order to use pi
from math import pi

# assign a variable, radiusInput, which gets radius value from user. Add another variable, radius, which prints the radius till the 6th decimal point.
radiusInput = float(input('Enter the radius of the sphere: '))
radius = format(radiusInput, '.6f')

#Complete the surface area calculations (4(pi)r^2) and store them in variable surfaceAreaValue
surfaceAreaValue = 4 * pi * (radiusInput ** 2)
#round the surface area value to one decimal place
surfaceArea = round(surfaceAreaValue, 1)

# complete volume formula calculations (4/3(pi)r^3) and store in volumeValue variable
volumeValue = (4/3) * pi * (radiusInput ** 3)
#convert volume value to scientific notation using format()
volume = "{:.5e}".format(volumeValue)

#print final values to terminal
print(str(radius) + ' Is the value of your radius.')
print('In a sphere of radius ' + str(radius) + ', the surface area is ' + str(surfaceArea))
print('And its volume is ' + str(volume))

#PROBLEM 2

#initialize 2 variables (n1, n2) which are the first numbers in the Fibonacci sequence
n1, n2 = 0, 1
#also create a list of numbers that will be added to as the sequence progresses
sequence = [0, 1]
#initiate a boolean which will be used to tell if a number is the first in the sequence to reach 4000
is4000 = True

#loop until the sequence reaches above 5000
while n1 < 5000 and n2 < 5000:
    #complete the process of the fibonacci sequence by adding the previous 2 numbers and store it in a variable, newValue
    newValue = n1 + n2
    #reassign n1, n2 to the two highest values (n2, newValue)
    n1 = n2
    n2 = newValue
    #add the new number to the array of numbers in the sequence
    sequence.append(newValue)
    #if the next value is greater than 4000 AND is the first number to reach 4000
    if newValue > 4000 and is4000 == True:
        #print the answer to part A.
        print('The first Fibonacci number greater than 4000 is ' + str(newValue))
        #set is4000 to false so following values in the sequence that are greater than 4000 will not print.
        is4000 = False
            
#remove the last element in the sequence; this is because the while loop will have executed one extra time before breaking therefore containing a number above 5000
sequence.pop()

#print the answer to part B by getting the len() of the sequence array
print('There are ' + str(len(sequence)) + ' Fibonacci numbers less than 5000.')
