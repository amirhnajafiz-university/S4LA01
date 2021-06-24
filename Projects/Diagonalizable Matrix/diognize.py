"""

Project: Diagonalizable check
Date: June 25th 2021
Author: Amirhossein Najafizadeh

Explain:
	Given a matrix, an algorithem to check if
	matrix is diagonalizable or not.

	We use the Eigenvalues of that matrix.
	If the matrix SIZE N columns, has N unique 
	eigenvalues, then it is diagonalizable.
"""
import sympy as sy 
import numpy as np
from sympy.solvers import solve
from sympy.abc import x, y, z, t


SIZE = 4
FILE_PATH = "./graph.txt"
L = sy.symbols('L')  # This is lambda

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

def createMatrix(nodes):  # This  function creates a matrix based on the nodes we have
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

	print(">> Determinant")
	print(determinant)

	# Solve the equetion | A - LI | = 0
	eigenvalues = solveEquetion(determinant)

	unique = []

	# Check if we have N unique eigenvalues
	for eigenvalue in eigenvalues:
		if eigenvalue not in unique:
			unique.append(eigenvalue)

	print(">> Eigenvalues :")
	print(eigenvalues)

	print(">> Diagonalizable :")
	if len(unique) == SIZE:
		print("YES")
	else:
		print("NO")
		