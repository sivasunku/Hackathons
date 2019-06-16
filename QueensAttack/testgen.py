# -*- coding: utf-8 -*-
"""
Created on Sun May  5 17:29:02 2019

@author: siva
"""

import random
import subprocess

# Read n - size of board, m -pieces to be generated
N = 8
folder = "C:/Users/sivas/Documents/Data Analytics & Certification/Python Projects/Hackathons/QueensAttack/"


def create_test(the_file):
    n = random.randint(5, 100)
    m = random.randint(4, 20)
    print(n, m)
    pieces = []
    co_ords = []
    count = 1

    while count <= m:
        i = random.randint(1, N)
        j = random.randint(1, N)
        if [i, j] in co_ords:
            pass
        else:
            tmp = "Q" + str(count)
            pieces.append([i, j, tmp])
            co_ords.append([i, j])
            count += 1
    the_file.write(str(n) + "," + str(m) + "\n")
    for x in pieces:
        the_file.write(str(x[0]) + "," + str(x[1]) + "," + x[2] + "\n")


if __name__ == "__main__":
    for i in range(8):
        fname = folder + "test_gen" + str(i) + ".txt"
        file_pointer = open(fname, "w")
        create_test(file_pointer)
        file_pointer.close()



