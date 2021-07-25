"""

Project: Find the Least Square Line of some data
Date: July 25th 2021
Author: Amirhossein Najafizadeh

Explain:
	Given a pack of data.
	This data is like, variable variable ..... result
	The point is to find a line that is the least square line of
	the imported data.

	After that we can use some undefined result data to find their
	result based of the given data.
"""
import sympy as sy 
import numpy as np
from sympy.solvers import solve



VARIABLES = 1  # Number of variables in our system
FILE = './data_1.txt'  # The file data address


def import_data():  # This method imports the given data into the program
	global VARIABLES
	data = []
	with open(FILE, 'r') as file:
		lines = file.readlines()
		for line in lines:
			parts = line.split(" ")
			new_parts = []
			for part in parts:
				new_parts.append(int(part))
			data.append( tuple(new_parts) )
	if len(data) > 0:
		VARIABLES = len(data[0]) - 1
	return data


def create_XY(data):  # This method generates the X and Y matrix from our data
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


def find_transpose(A):  # This method gets a matrix and returns its transpose
	return A.transpose()


def multiply(A, B):  # This method multiplies A in B (returns A*B)
	return A.dot(B)


def solve_equation(A, B):  # This method solves the equetion Ax = B
	return np.linalg.solve(A, B)


def display_line(V):  # This method gets a vector and displays the line of that vector
	r, c = V.shape
	string = "y = "
	power = -1
	for i in range(r):
		power += 1
		if V[i][0] == 0:
			continue
		if power == 0:
			string += f'{str(V[i][0])} '
		else:
			if power == 1:
				string += f' + ({V[i][0]})x '
			else:
				string += f' + ({V[i][0]})x^{power} '
	return string


def execute():  # Program starts
	data = import_data()
	X, Y = create_XY(data)
	XT = find_transpose(X)
	X = multiply(XT, X)
	Y = multiply(XT, Y)
	result = solve_equation(X, Y)
	print(display_line(result))


if __name__ == "__main__":
	execute()