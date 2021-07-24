"""

Project: LU Decomposition
Date: July 24th 2021
Author: Amirhossein Najafizadeh

Explain:
	Given a matrix called A.

	We want to decompose this matrix in an L*U format.
	We use the modify_format and echelon to check if 
	our matrix is actually decomposable, after that we
	create the L and U by calling the lu method.
"""
import numpy as np


def modify_format(A):  # This method replaces the rows that have 0 in our main digon
	r, c = A.shape
	for i in range(r):
		if A[i][i] == 0:
			for j in range(i+1, r):
				if A[j][i] != 0:
					A[[i, j]] = A[[j , i]]
	return A


def echelon(A):  # A recurtion function to convert our matrix to Echelon form
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


def simple_check(A):  # This function checks the base rule of LU decompose
	r, c = A.shape
	return r == c


def hardcore_check(A):  # This function checks the second rule of LU decompose
	r, c = A.shape
	for i in range(r):
		if A[i][i] == 0:
			return False
	return True

def lu(A):  # This function creates the LU factorization
    n = A.shape[0]
    U = A.copy()
    L = np.eye(n, dtype=float)
    for i in range(n):
        factor = U[i+1:, i] / U[i, i]
        L[i+1:, i] = factor
        U[i+1:] -= factor[:, np.newaxis] * U[i]  
    return L, U


def execute(): # Program starts
	# Getting the A matrix
	array = np.array([[0,1,-4], [2,-3,2], [5,-8,10]], dtype=float)
	array = modify_format(array)
	A = np.array(array)
	print(">> A Matrix: ")
	print(A)
	print("    ----    \n")

	if not simple_check(array):
		print("> Not decomposeable.")
		return
	    
	# Convert to echelon form
	array = echelon(array)
	print(">> Echelon Form: ")
	print(array)
	print("    ----    \n")

	if not hardcore_check(array):
		print("> Not decomposeable.")
		return

	# Create the U matrix
	L, U = lu(A)
	print(">> The decomposition: ")
	print("> A:")
	print(A)
	print("> L:")
	print(L)
	print("> U:")
	print(array)
	print("> L * U")
	print(L.dot(array))
                

if __name__ == "__main__":
	execute()