"""

Project: Finding Eigenvalues and Eigenvectors 
Date: June 25th 2021
Author: Amirhossein Najafizadeh

Explain:
	Given a matrix, an algorithem to find the
	eigenvalues and eigenvectors of that matrix.

	First we solve the equetion: | A - LI | = 0
	After finding the eigenvalues from abow equetion, we
	solve the linear system : Ax = Lx

		1. Convert to (1/L) Ax = x
		2. Then to ( (1/L)A - I ) x = 0
		3. Then we solve the linear system above by converting to RREF 
		4. Then we find the vectors of that space
"""
import sympy as sy 
import numpy as np
from sympy.solvers import solve
from sympy.abc import x, y, z, t


SIZE = 4
FILE_PATH = "./graph.txt"
L = sy.symbols('L')  # This is Lambda

def readFromFile():  # This function reads the data from the file and creates the list of nodes with their edges
	nodes = {}
	with open(FILE_PATH, 'r') as file :
		lines = file.readlines()
		for line in lines:
			parts = line.split(" ")

			if parts[0][1] in nodes:
				nodes[parts[0][1]]['to'].append(parts[1][1])
			else:
				nodes[parts[0][1]] = {}
				nodes[parts[0][1]]['to'] = []
				nodes[parts[0][1]]['from'] = []
				nodes[parts[0][1]]['to'].append(parts[1][1])

			if parts[1][1] in nodes:
				nodes[parts[1][1]]['from'].append(parts[0][1])
			else:
				nodes[parts[1][1]] = {}
				nodes[parts[1][1]]['to'] = []
				nodes[parts[1][1]]['from'] = []
				nodes[parts[1][1]]['from'].append(parts[0][1])
	SIZE = len(nodes)
	return nodes

def findDegree(nodes):  # This function defines the degre for each node
	for node in nodes:
		nodes[node]['degree'] = len(nodes[node]['to'])

def createMatrix(nodes):  # This function creates a matrix based on the nodes we have
	size = len(nodes)
	matrix = np.zeros((size, size), dtype=float)
	for node in nodes:
		for dis in nodes[node]['to']:
			matrix[int(dis)-1][int(node)-1] = 1 / nodes[node]['degree']
	return matrix

def createParametricMatrix(matrix):  # This function creates A - LI matrix ( Parametric matrix )
	matrix_sy = sy.Matrix(matrix)
	for i in range(SIZE):
		for j in range(SIZE):
			if i == j:
				index = i * SIZE + j
				matrix_sy[index] = matrix_sy[index] - L
	return matrix_sy

def getDeterminant(matrix_sy):  # This function calculates the parametric matrix determinant
	return matrix_sy.det()

def solveEquetion(equetion):  # This function gets an equetion based on Lambda and solves it
	return solve(equetion, L)

def solving(A, free_vars, non_free_vars):  # A function to show the equetions from final matrix
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


if __name__ == "__main__":
	# Reading the text file to find the nodes
	nodes = readFromFile()
	# Calculating the degree of each node
	findDegree(nodes)
	# Create an NxN matrix from our nodes
	matrix = createMatrix(nodes)

	print("> Matrix :")
	print(matrix)
	print("=======================")
	print("=======================")

	# Make a copy of our first matrix
	first_matrix = matrix

	# Create  A - LI
	matrix = createParametricMatrix(matrix)

	# Create | A - LI |
	determinant = getDeterminant(matrix)

	# Solve the equetion | A - LI | = 0
	eigenvalues = solveEquetion(determinant)

	# Finding the eigenvectors based on the eigenvalues
	for eigenvalue in eigenvalues:
		if not eigenvalue.is_real:
			continue
		a, b, c, d = sy.symbols('a, b, c, d')
		print("> Eigenvalue : ")
		print(eigenvalue)
		A = sy.Matrix(first_matrix)
		A = A / eigenvalue
		for i in range(SIZE):
			for j in range(SIZE):
				if i == j:
					index = i * SIZE + j
					A[index] = A[index] - 1
		A = A.col_insert(SIZE, sy.zeros(SIZE, 1))
		free_vars = []
		non_free_vars = []
		convert_matrix = np.array(A).astype(np.float64)
		convert_matrix = reduction_echelon(np.round(echelon(convert_matrix), decimals=2))
		pivots = solving(convert_matrix, free_vars, non_free_vars)
		print("    ----    \n")
		null_space = get_null_space(free_vars, convert_matrix)
		print("> Eigenvector : ")
		for basis in null_space:
			print(null_space[basis])
		print("=======================")
