"""

Project: Convert an image from 'RGB format' to 'Black & White format'
Date: March 29th 2021
Author: Amirhossein Najafizadeh

Explain:
	We use the matplotlibs image class to read a give image and convert
	it into an matrix. The matrix is an 3D matrix (Row, Column, (r,g,b))

	Then we use numpy to create a new 2D matrix.
	Then we multiply each element in our 3D matrix with the 'Transformation Matrix',
	and we save it into the 2D matrix.
	In the end we used the imsave method in image class to save our matrix into a picture.

"""
import matplotlib.image as plotim
import numpy as np  


def multiplay_vectors(A, B): # This function multiplies two vectors give to it
	C = np.zeros(1, dtype=A.dtype)
	C[0] = A[0] * B[0] + A[1] * B[1] + A[2] * B[2]
	return C


def execute(): # Program starts
	IMAGE_ADDRESS = "sample.jpg"
	OUTPUT_ADDRESS = "result.jpg"

	# Reading the image and save it into an array
	IMAGE = plotim.imread(IMAGE_ADDRESS)

	# Get image sizes
	r, c, e = IMAGE.shape

	# Defining our transform matrix
	transform_matrix = np.array([0.2989, 0.5870, 0.1140])

	# Create a new 2D array
	new_image = np.zeros([r,c], dtype=IMAGE.dtype)

	# Convert each pixle into new pixle
	for i in range(r):
		for j in range(c):
			temp = IMAGE[i, j]
			new_image[i, j] = multiplay_vectors(transform_matrix, temp)

	# Save into output file
	plotim.imsave(OUTPUT_ADDRESS, new_image, cmap='gray')


if __name__ == "__main__":
	execute()