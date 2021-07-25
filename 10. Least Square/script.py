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



VARIABLES = 1


def import_data():
	data = []
	with open("./data.txt", 'r') as file:
		lines = file.readlines()
		for line in lines:
			parts = line.split(" ")
			data.append( ( int(parts[0]), int(parts[1]) ) )
	return data


def create_XY(data):
	r = len(data)
	c = VARIABLES + 1
	A = np.zeros((r,c), dtype=int)
	B = np.zeros((r,1), dtype=int)
	for j in range(r):
		power = 1
		A[j][0] = 1
		for index in range(VARIABLES):
			A[j][index+1] = pow(data[j][index], power)
			power += 1
		B[j][0] = data[j][VARIABLES]
	return A, B



def execute():
	data = import_data()
	X, Y = create_XY(data)
	print(X)
	print(Y)


if __name__ == "__main__":
	execute()