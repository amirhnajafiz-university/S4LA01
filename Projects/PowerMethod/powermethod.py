"""

Project: Power method implemintation
Date: June 25th 2021
Author: Amirhossein Najafizadeh

Explain:
	We have a matrix and a vector.
	We are going to find the Highest Eigenvalue and its Vector
	by the power method.

	We also find the the best K of A^k x that gives us the Eigenvalue.
"""
import numpy as np
from numpy import linalg as LA


def getMax(V):  # This function returns the maximum element in a vector
	r, c = V.shape
	maximum = V[0][0]
	for i in range(r):
		if V[i][0] > maximum:
			maximum = V[i][0]
	return maximum

def checkEqual(V):  # This function checks if all of a vector elements are equal
	r, c = V.shape
	for i in range(r):
		if V[0][0] != V[i][0]:
			return False
	return True

if __name__ == "__main__":
	A = np.matrix([[6, 5] , [1, 2]])  # A matrix
	X0 = np.matrix([0, 1]).T  # B vector
	OX0 = X0  # Create a temp Old B vector to have A^(k-1) x in each step

	print("> Matrix A :")
	print(A)
	print("============")

	print("> t vector :")
	print(X0)
	print("============\n")

	iterate = 0

	while True:
		iterate += 1
		X0 = X0 / getMax(X0)  # Divide by the highest value in vector
		X0 = A.dot(X0)  # Calculate Ax
		temp = np.around((OX0 / X0), decimals=2)  # If temp is an Equal Vector, it means that we reached to a good K
		if checkEqual(temp):
			break
		OX0 = X0

	print("Best K : ")
	print(iterate)
	print("\nMaximum Eigenvalue : ")
	print(getMax(X0)[0][0])
	print("\nEigenvector : ")
	print(X0 / getMax(X0))
