"""

Project: Solve equetion 'Ax=b' from given 'A' and 'b'
Date: March 28th 2021
Author: Amirhossein Najafizadeh

Explain:
	For this project we used numpy library to create one matrix (A)
	and one vector (B).
	Then we create the augmented matrix from A and b.
	After that we call the echelon function to convert our matrix
	to echelon form.
	And then we call reduction_echelon function to convert the given
	matrix to row reduction echelon form.
	Before we give the results, we check our system to be sure that 
	our system is consistent.
	In the end we show the equetions given by our matrix, and we 
	define each variable status ( free or not )

"""
import numpy as np


def echelon(A): # A recurtion function to convert our matrix to Echelon form
    r, c = A.shape

    if r == 0 or c == 0:
        return A

    for i in range(len(A)):
        if A[i, 0] != 0:
            break
    else:
        B = echelon(A[:, 1:])
        return np.hstack([A[:, :1], B])

    if i > 0:
        temp_row = A[i].copy()
        A[i] = A[0]
        A[0] = temp_row
    
    temp = np.array((A[0] / A[0,0]), dtype=A.dtype)
    A[1:] -= temp * A[1:, 0:1]

    B = echelon(A[1:, 1:])

    return np.vstack([A[:1], np.hstack([A[1:, :1], B])])


def reduction_echelon(A): # A recurtion function to convert our matrix to Reduction Echelon form
    r, c = A.shape
    
    if r == 0:
        return A
        
    for i in range(c):
        if A[-1, i] != 0:
            break
    else:
        B = reduction_echelon(A[:-1,:])
        return np.vstack([B, A[-1:, :]])
        
    A[-1] = A[-1] / A[-1, i]
    A[:-1, :] -= A[-1] * A[:-1, :]

    B = reduction_echelon(A[:-1,:])

    return np.vstack([B, A[-1:, :]])


def check_system(A): # A function to check the system consistent
    r, c = A.shape
    for i in range(r):
        flag = True
        for j in range(c-1):
            if A[i,j] != 0:
                flag = False
        if flag and A[i,j+1] != 0:
            return True
    return False


def solve(A): # A function to show the equetions from final matrix
    pivots = []
    r, c = A.shape
    for i in range(r):
        line = []
        flag = True
        for j in range(c-1):
            if A[i,j] != 0:
                if A[i,j] == 1:
            	    line.append("x" + str(j+1))
                else:
                    string = '({:.3f})x{}'.format(A[i,j], j+1)
                    line.append(string)
                if flag:
                    pivots.append(j)
                flag = False
        if len(line) == 0:
        	continue
        formul = " + ".join(line)
        formul += " = " + '{:.3f}'.format(A[i,c-1])
        print(formul)
    return pivots


def execute(): # Program starts
	# Getting the A matrix
	array = np.array([[0,1,-4], [2,-3,2], [5,-8,7]], dtype=float)
	print(">> A Matrix: ")
	print(array)
	print("    ----    \n")

	# Getting th b vector
	z = np.array([[8,1,1]], dtype=array.dtype).T
	print(">> b Vector: ")
	print(z)
	print("    ----    \n")

	# Create the augmented matrix
	array = np.append(array, z, axis=1)
	print(">> Augmented Matrix: ")
	print(array)
	print("    ----    \n")
	    
	# Convert to echelon form
	array = echelon(array)
	print(">> Echelon Form: ")
	print(array)
	print("    ----    \n")

	# Convert to reduction echelon
	array = reduction_echelon(array)
	print(">> Reduction Echelon Form: ")
	print(array)
	print("    ----    \n")
	        
	# Check system            
	if check_system(array):
	    print(">> System is inconsistent")
	    return

	# Find the equetions
	print(">> Equetions: ")
	pivots = solve(array)
	print("    ----    \n")

	# Showing the status of our variables
	print(">> Variable: ")
	for i in range(array.shape[1]-1):
	    if i in pivots:
	        print("    Var x" + str(i+1) + " is not free")
	    else:
	        print("    Var x" + str(i+1) + " is free")
                

if __name__ == "__main__":
	execute()