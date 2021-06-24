"""

Project: Google Page Ranking
Date: June 24th 2021
Author: Amirhossein Najafizadeh

Explain:
	Given an input Graph that shows the 
	edges between two vertices.
	If i has edge to j then we say i links j.

	First we get an input file to get the graph
	data and we set a LIMIT.

	After that we calculate the nodes degree based on the
	sum of nodes that it links.

	Then we create the Adj matrix of our nodes.

	After that we start multipling the Adj matrix into base
	vector by the times of LIMIT.

	Result is our webpages rank that is Vector.
"""
import numpy as np


FILE_PATH = "./graph.txt"
LIMIT = 7

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

def createRvector(size):  # This function creates the R vetor
	vector = np.zeros((size, 1), dtype=float)
	for i in range(size):
		vector[i][0] = 1 / size;
	return vector


if __name__ == "__main__":
	# Reading the text file to find the nodes
	nodes = readFromFile()
	# Calculating the degree of each node
	findDegree(nodes)
	# Create an NxN matrix from our nodes
	matrix = createMatrix(nodes)
	print("> Adj Matrix: ")
	print(matrix)
	print("==============")
	# Create the R vector
	r = createRvector(len(nodes))
	print("> R Vector: ")
	print(r)
	print("==============")

	# Calculate the ranks
	for i in range(LIMIT):
		r = matrix.dot(r)

	# Results
	print("> Rank results: ")
	print(r)
	print("==============")
