"""

"""
import numpy as np


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


def create_I(k):  # This function create the indentify matrix
	return np.identity(k, dtype = float)


def create_L(A):
	r, c = A.shape
	L = create_I(r)
	index = 0
	for i in range(c):
		factor = A[i][index]
		for j in range(index + 1, r):
			L[j][i] = A[j][i] / factor
		index += 1
	return L


def execute(): # Program starts
	# Getting the A matrix
	array = np.array([[0,1,-4], [2,-3,2], [5,-8,10]], dtype=float)
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
	L = create_L(A)
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