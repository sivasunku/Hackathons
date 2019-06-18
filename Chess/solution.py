# -*- coding: utf-8 -*-
"""

"""


def print_matrix(matrix):
    print("=========================================")
    for x in matrix:
        print(*x, sep=" ")


# i,j is King's position
# res is current state of chess board
def check_king(i, j, res):
    # Check all 8 positions
    kp = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j),
          (i + 1, j + 1)]
    for x, y in kp:
        if res[x][y] in blocks:
            pass
        else:
            res[x][y] = 'x'
    return res


# Check Knight
def check_knight(i, j, res):
    # check all 8 knight positions
    kp = [(i - 1, j + 2), (i + 1, j + 2), (i - 1, j - 2), (i + 1, j - 2), (i - 2, j - 1), (i - 2, j + 1),
          (i + 2, j - 1), (i + 2, j + 1)]
    for x, y in kp:
        if (res[x][y] in blocks):
            pass
        else:
            res[x][y] = 'x'
    return res


# check Bishop
# Bishop travels diagonolly. If bishop is in position 2,3 all positions whose sum is 5 are blocked
def check_bishop(input_i, input_j, res):
    # NorthEast
    i, j = input_i - 1, input_j + 1
    while (i >= 0) and (j < Nn):
        if res[i][j] in blocks:
            break
        else:
            res[i][j] = 'x'
        i, j = i - 1, j + 1
        # NorthWest
    i, j = I - 1, J - 1
    while (i >= 0) and (j >= 0):
        if res[i][j] in blocks:
            break
        else:
            res[i][j] = 'x'
        i, j = i - 1, j - 1
    # SouthEast
    i, j = I + 1, J + 1
    while (i < Nn) and (j < Nn):
        if res[i][j] in blocks:
            break
        else:
            res[i][j] = 'x'
        i, j = i + 1, j + 1
    # SouthWest
    i, j = I + 1, J - 1
    while (i < Nn) and (j >= 0):
        if res[i][j] in blocks:
            break
        else:
            res[i][j] = 'x'
        i, j = i + 1, j - 1
    return res


# Rook can attack horizontally/vertically
def check_rook(input_i, input_j, res):
    # North
    i, j = input_i - 1, input_j
    while i >= 0:
        if res[i][j] in blocks:
            break
        else:
            res[i][j] = 'x'
        i -= 1
    # South
    i, j = input_i + 1, input_j
    while i < Nn:
        if res[i][j] in blocks:
            break
        else:
            res[i][j] = 'x'
        i += 1

    # East
    i, j = input_i, input_j + 1
    while j < Nn:
        if res[i][j] in blocks:
            break
        else:
            res[i][j] = 'x'
        j += 1
    # West
    i, j = input_i, input_j - 1
    while j >= 0:
        if res[i][j] in blocks:
            break
        else:
            res[i][j] = 'x'
        j -= 1
    return res


# Start of program
# N - Chess Size
# m - No. of pieces
N, m = map(int, input().rstrip().split())
Nn = N + 4
blocks = ['K', 'R', 'B', 'N', 'Q']

# Create a (N+4) * (N+4) blank matrix, to avoid dimension boundary checks
# Strip the top two rows, bottom two rows, left two cols & right two cols before presenting the result
# Add two rows & two cols for each of piece position
res = [["-"] * (Nn) for i in range(Nn)]
pieces = []
# Read all pieces
for _ in range(m):
    i, j, p = input().rstrip().split(",")
    i, j = map(int, [i, j])
    # print(i,j,p)
    res[i + 1][j + 1] = p
    pieces.append([i + 1, j + 1, p])

# print_matrix(res)
for x in pieces:
    i, j, p = x
    if p == 'K':
        check_king(i, j, res)
    if p == 'R':
        check_rook(i, j, res)
    if p == 'B':
        check_bishop(i, j, res)
    if p == 'Q':
        check_bishop(i, j, res)
        check_rook(i, j, res)
    if p == 'N':
        check_knight(i, j, res)

counter = 0
# print_matrix(res)
# Strip the extra rows & columns
Nres = [x[2:Nn - 2] for x in res[2:Nn - 2]]
# print_matrix(Nres)
for x in Nres:
    counter += x.count('-')
print(counter)

