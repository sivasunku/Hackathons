# -*- coding: utf-8 -*-
"""
  
"""

def printMatrix(matrix):
  print("=========================================")
  for x in matrix:
    print(*x,sep=" ")

# i,j is King's position
# res is current state of chess board
def checkKing(i,j,res):
  #Check all 8 positions
  kp = [ (i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1) ]
  for x,y in kp:
    if (res[x][y] in blocks):
      pass
    else:
      res[x][y] = 'x'
  return res

#Check Knight
def checkKnight(I,J,res):
  #check all 8 knight positions
  kp = [ (i-1,j+2),(i+1,j+2),(i-1,j-2),(i+1,j-2),(i-2,j-1),(i-2,j+1),(i+2,j-1),(i+2,j+1)]
  for x,y in kp:
    if (res[x][y] in blocks):
      pass
    else:
      res[x][y] = 'x'
  return res

#check Bishop
#Bishop travels diagonolly. If bishop is in position 2,3 all positions whose sum is 5 are blocked
def checkBishop(I,J,res):
  #NorthEast
  i,j = I - 1,J + 1
  while ( (i >= 0) and (j < Nn) ):
    if (res[i][j] in blocks):
       break
    else:
       res[i][j] = 'x'
    i,j = i-1,j+1 
  #NorthWest
  i,j = I - 1,J - 1
  while ( (i >= 0) and (j >= 0) ):
    if (res[i][j] in blocks):
       break
    else:
       res[i][j] = 'x'
    i,j = i-1,j-1
  #SouthEast
  i,j = I + 1,J + 1
  while ( (i < Nn ) and (j < Nn) ):
    if (res[i][j] in blocks):
       break
    else:
       res[i][j] = 'x'
    i,j = i+1,j+1
  #SouthWest
  i,j = I + 1,J - 1
  while ( (i < Nn) and (j >= 0) ):
    if (res[i][j] in blocks):
       break
    else:
       res[i][j] = 'x'
    i,j = i+1,j-1
  return res

#Rook can attack horizontally/vertically
def checkRook(I,J,res):
  #North
  i,j = I - 1,J
  while ( i >= 0):
    if (res[i][j] in blocks):
       break
    else:
       res[i][j] = 'x'
    i -= 1
  #South
  i,j = I + 1,J
  while ( i < Nn):
    if (res[i][j] in blocks):
       break
    else:
       res[i][j] = 'x'
    i += 1

  #East
  i,j = I,J+1
  while ( j < Nn ):
    if (res[i][j] in blocks):
       break
    else:
       res[i][j] = 'x'
    j += 1
  #West
  i,j = I,J-1
  while ( j >= 0):
    if (res[i][j] in blocks):
       break
    else:
       res[i][j] = 'x'
    j -= 1
  return res

#Start of program
#N - Chess Size
#m - No. of pieces
N,m = map(int, input().rstrip().split()) 
Nn = N+4
blocks = ['K','R','B','N','Q']

#Create a (N+4) * (N+4) blank matrix, to avoid dimension boundary checks
#Strip the top two rows, bottom two rows, left two cols & right two cols before presenting the result
#Add two rows & two cols for each of piece position
res = [["-"] * (Nn) for i in range(Nn)]
pieces = []
#Read all pieces
for _ in range(m):
  i,j,p = input().rstrip().split(",")
  i,j = map(int,[i,j])
  #print(i,j,p)
  res[i+1][j+1] = p
  pieces.append([i+1,j+1,p])

#printMatrix(res)
for x in pieces:
  i,j,p = x
  if (p == 'K'):
    checkKing(i,j,res)
  if (p == 'R'):
    checkRook(i,j,res)
  if (p == 'B'):
    checkBishop(i,j,res)
  if (p == 'Q'):
    checkBishop(i,j,res)
    checkRook(i,j,res)
  if (p == 'N'):
    checkKnight(i,j,res)
 
counter = 0
#printMatrix(res)
#Strip the extra rows & columns
Nres = [x[2:Nn-2] for x in res[2:Nn-2]]
#printMatrix(Nres)
for x in Nres:
  counter += x.count('-')
print(counter)
  
