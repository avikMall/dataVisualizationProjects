#Avik Malladi Project #2: Eigenvalue of a square matrix
import numpy as np

#Initialize matrix A, vector u, and vector w
A = np.array(([3, 1], [2, 4]))
u = np.array(([1], [1]))
w = np.array(([1], [0]))

for i in range(1, 100):
    newValue = np.dot(A, u)
    #print the calculated value (uā)
    print('u{}'.format(i) + ': \n' + str(newValue))

    #calculate lambda using the formula šš»āšš+š šš»āš
    lmd = (np.dot(w.T, newValue)) / (np.dot(w.T, u))
    print('lmd approx: ' + str(lmd))
    #calculate the step5 values using the formulas š“āšš/āššā and šāšš/āššā
    AVector = (np.dot(A, u)) / ((np.linalg.norm(u)))
    lmdVector = (lmd * u) / ((np.linalg.norm(u)))
    #print the difference
    print('When n={} the difference between š“āšš/āššā and šāšš/āššā is '.format(i) + '\n' + str(AVector - lmdVector))

    #set u equal to uāāā for the next iteration
    u = newValue

#print the value that lambda converges to after all iterations using round()
print('\n' + 'After all iterations the value that lambda converges to is ' + str(round(lmd[0][0])))
