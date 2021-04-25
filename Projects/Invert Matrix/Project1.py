"""

Project: Find the invert matrix of A matrix
Date: April 25th 2021
Author: Amirhossein Najafizadeh

Explain:
	Given a matrix A, I used the echelon and reduction echelon
	functions to convert our matrix to RRE form. Then we check
	if the matrix is invertable or not.
	If invertable we give the invert matrix, by creating the [A | I] and 
	do the same row reduction operations on I.

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
        if A[i,i] != 1:
        	return False
    return True

def find_matrix_invert(A):
	r, c = A.shape
	return A[:, r:]


def execute(): # Program starts
	# Getting the A matrix
	array = np.array([[3, -2, 4], [1, 0, 2], [0, 1, 0]], dtype=float)
	print(">> A Matrix: ")
	print(array)
	print("    ----    \n")

	# Creating the In
	i = np.identity(3, dtype=float)
	idnty = np.append(array, i, axis=1)
	print(">> Identity Matrix: ")
	print(idnty)
	print("    ----    \n")
	
	idnty = echelon(idnty)
	idnty = reduction_echelon(idnty)

	print(">> RRE Identity Matrix: ")
	print(idnty)
	print("    ----    \n")

	if check_system(idnty):
		print(">> Invert Matrix: ")
		print(find_matrix_invert(idnty))
		print("    ----    \n")
	else:
		print(">> Matrix not invertable")
                

if __name__ == "__main__":
	execute()