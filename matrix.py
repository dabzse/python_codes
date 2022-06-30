## REQUIREMENTS
# pip install numpy
# pip install matplotlib
import numpy as np
import matplotlib.pyplot as plt

## constant(s)
LF = '\n\n'

## creating a random * random size matrix and displaying it in the terminal
row = np.random.randint(10,100)
col = np.random.randint(10,100)
array = np.random.randint(2, size=(row, col))
print("here is your matrix in \"binary\" format")
print(array)

## saving the generated and already displayed
## random * random size matrix to work with it
np.savetxt("matrix.txt", array, fmt='%d')
print(LF)

## loading the matrix's data and displays some details
matrix = np.loadtxt("matrix.txt")
print("the dimension of this matrix is: " + str(matrix.shape))
print(LF)

## creating an image without save, and opens in an external window
plt.matshow(matrix)
plt.show()
