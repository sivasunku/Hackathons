# -*- coding: utf-8 -*-
"""
Creates the test Cases for Treasure Trove.
Change the below parameters.
  no_of_testcases - No. Of Test Cases to be presented
  max_matrix_size - maximum size of the matrix
"""
# Create test cases for input Matrix
# select Size
#   - random number between (1-49)
#   - m = rand * 2 + 1 (m limits are 3 - 99)
# create a list of alphabets of size - m * m
#   Remove all X & T in this set
# matrix  = reshape the alphabets to size m * m
# Make the center co-ordinates as 'T'
# Prepare layer co-ordinates of the size m
# for each of the layer
#   pick a random variable from (1 - len(m))
#   mark 'X' there

# Write the output no_of_testcases
# For  each TESTCASE
#  m
#  pd.DataFrame(matrix)

import random
import numpy as np
import pandas as pd
import string

max_matrix_size = 49
folder = "C:/Users/sivas/Documents/Data Analytics & Certification/Python Projects/Hackathons/Trove/"

# Prepare layers
def make_layers(m):
    # Layers for m=5, 2,1,0
    no_of_layers = m // 2
    layers = []
    for x in range(0, no_of_layers):
        tmp = []
        # Move East
        i = x
        for j in range(x, m - x):
            tmp.append((i, j))
        # Move South
        j = m - 1 - x
        for i in range(x + 1, m - x):
            tmp.append((i, j))
        # Move West
        i = m - 1 - x
        for j in range(m - x - 2, x - 1, -1):
            tmp.append((i, j))
        # Move North
        j = x
        for i in range(m - x - 2, x, -1):
            tmp.append((i, j))

        layers.append(tmp)
    return layers


# Prepare matrix of size n
def prep_matrix(m):
    tmp = ''.join(random.choice(string.ascii_uppercase) for _ in range(m * m))
    tmp = tmp.replace('T', 'M')
    tmp = tmp.replace('X', 'Z')
    matrix = np.array(list(tmp)).reshape(m, m)
    matrix[m // 2][m // 2] = 'T'
    layers = make_layers(m)

    # Generate m//2 random numbers between 1 - m * m
    rands = random.sample(range(1, m * m), m // 2)
    for i in range(0, m // 2):
        t = rands[i] % len(layers[i])
        p, q = layers[i][t]
        matrix[p][q] = 'X'
    return matrix


for i in range(2, 15):
    fname = folder + "test_gen" + str(i) + ".txt"
    file_pointer = open(fname, "w")
    m = (int(random.random() * 100) % (max_matrix_size // 2)) * 2 + 1
    file_pointer.write(str(m) + "\n")
    mat = prep_matrix(m)
    matPrint = pd.DataFrame(mat).to_string(index=False, header=False)
    file_pointer.write(matPrint)
