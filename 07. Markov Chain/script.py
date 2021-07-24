"""

Project: Markov Chain
Date: May 30th 2021
Author: Amirhossein Najafizadeh

Explain:
	Given a matrix 'A', we want to find its Null space
	and find the Markov Chain of the given matrix.

	Functions:
		1. Echelon => Gets a matrix and returns the echelon format of that matrix
		2. Reduction Echelon => Gets a echelon matrix and returns reduction echelon format
		   of that matrix.
		3. Slove => Gets a reduction echelon format matrix and finds the free and non free
		   variables, among the equetions generated from solving the system.
		4. Get null space => Gets a solved matrix and creates the null space of that matrix.

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


def solve(A, free_vars, non_free_vars): # A function to show the equetions from final matrix
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
					non_free_vars.append(j)
				else:
					free_vars.append(j)
				flag = False
		if len(line) == 0:
			continue
		formul = " + ".join(line)
		formul += " = " + '{:.3f}'.format(A[i,c-1])
		print(formul)
	return pivots


def get_null_space(free_vars, array): # This function creates the null space of give solved matrix
	null_space = {}
	for free_var in free_vars:
		null_space[free_var + 1] = np.zeros((array.shape[0], 1), dtype=array.dtype)
		for i in range(array.shape[0]):
			null_space[free_var + 1][i][0] = -1 * array[i][free_var]
		null_space[free_var + 1][free_var][0] = 1
	return null_space


def execute(): # Program starts

	# Getting the A matrix
	array = np.array([[0.7, 0.4, 0.1], [0.1, 0.8, 0.1], [0.1, 0.2, 0.7]], dtype=float)
	print(">> A Matrix: ")
	print(array)
	print("    ----    \n")

	# Identity matrix
	I = np.identity(array.shape[0], dtype=float)
	print(">> I Matrix: ")
	print(I)
	print("    ----    \n")

	# (A-I)
	array = array - I

	# (A-I)x = 0
	z = np.zeros((array.shape[0], 1), dtype=array.dtype)
	print(">> Zero Vector: ")
	print(z)
	print("    ----    \n")

	array = np.append(array, z, axis=1)
	print(">> Augmented Matrix: ")
	print(array)
	print("    ----    \n")
	    
	# Convert to echelon form
	array = reduction_echelon(np.round(echelon(array), decimals=2))
	print(">> Echelon Form: ")
	print(array)
	print("    ----    \n")

	# Find the equetions
	free_vars = []
	non_free_vars = []
	print(">> Equetions: ")
	pivots = solve(array, free_vars, non_free_vars)
	print("    ----    \n")

	# Showing the status of our variables
	print(">> Variable: ")
	print("Free:")
	for free_var in free_vars:
		print(f'	X{free_var+1} is free.')
	print("Non Free:")
	for non_free_var in non_free_vars:
		print(f'	X{non_free_var+1} is not free.')
	print("    ----    \n")

	# Check if there are any free variables to see if null space is empty or not
	if len(free_vars) == 0:
		print(">> Null space is empty")
		return

	# Finding the null space basis
	null_space = get_null_space(free_vars, array)

	# Showing the basis of null space
	linear_equetion = np.zeros((array.shape[0], 1)) # This is for sum of the null space vectors
	print(">> Null space basis: ")
	for basis in null_space.keys():
		linear_equetion = linear_equetion + null_space[basis]
		print(null_space[basis])
	print("    ----    \n")

	# Showing sumation of null space basis
	print(">> A linear equetion: (Sum)")
	print(linear_equetion)
	print("    ----    \n")

	# Normalization
	total_value = 0.0
	for i in range(array.shape[0]):
		total_value += linear_equetion[i][0];

	linear_equetion = linear_equetion / total_value;

	print(">> A linear normalized:")
	print(linear_equetion)
	print("    ----    \n")
				

if __name__ == "__main__":
	execute()