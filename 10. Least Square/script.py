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


def import_data():
	data = []
	with open("./data.txt", 'r') as file:
		lines = file.readlines()
		for line in lines:
			parts = line.split(" ")
			data.append( ( int(parts[0]), int(parts[1]) ) )
	return data


def execute():
	data = import_data()


if __name__ == "__main__":
	execute()