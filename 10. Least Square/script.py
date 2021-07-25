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


def find_transpose(A):
	return A.transpose()


def multiply(A, B):
	return A.dot(B)


def solve_equation(A, B):
	return np.linalg.solve(A, B)


def display_line(A):
	r, c = A.shape
	string = "y = "
	power = -1
	for i in range(r):
		power += 1
		if A[i][0] == 0:
			continue
		if power == 0:
			string += f'{str(A[i][0])} '
		else:
			if power == 1:
				string += f' + ({A[i][0]})x '
			else:
				string += f' + ({A[i][0]})x^{power} '
	return string



def execute():
	data = import_data()
	X, Y = create_XY(data)
	XT = find_transpose(X)
	print(X)
	print(Y)
	print(XT)
	X = multiply(XT, X)
	Y = multiply(XT, Y)
	print(X)
	print(Y)
	result = solve_equation(X, Y)
	print(result)
	print(display_line(result))


if __name__ == "__main__":
	execute()