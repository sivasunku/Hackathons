# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 19:06:49 2019

@author: siva
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 13:36:40 2019

@author: siva
"""
#BruteForce
def bruteForce(N,startA = 2,startCounts = 0):
  a = max(1,startA)
  Lima = N //3
  count = startCounts
  while (a < Lima):
    b = a
    while (b <= N//2):
      #print(a,b)
      lhs = a**2 + b**2 + 1
      c = (lhs ** 0.5)
      if ( (c == int(c)) and (a + b + c <= N) ):
        count += 1
        print(a,b,c)
      b += 4
    a += 2
  return count
#Obtuse triangles if a^2 + b^2 = c^2-1
def matMul(A,B):
  result = [[sum(a * b for a, b in zip(A_row, B_col))  
                        for B_col in zip(*B)] 
                                for A_row in A] 
  return(result)


matA = [[1, -2, 2], [2, -1, 2], [2, -2, 3]]
matB = [[1, 2, 2], [2, 1, 2], [2, 2, 3]]
matC = [[-1, 2, 2], [-2, 1, 2], [-2, 2, 3]]
matAT = [[1, 2, 2], [-2, -1, -2], [2, -2, 3]]
matBT = [[2, 1, 1], [2, -2, 2], [2,-1, 3]]
matCT = [[2, -1, 1], [2, 2, 2], [2, 1, 3]]
I1 =  [[2], [2], [3]]
I2 =  [[18], [30], [35]]
I3 =  [[22], [46], [51]]
I4 =  [[34], [38], [51]]
I5 =  [[44], [68], [81]]
I6 =  [[64], [112], [1291]]

#matC = [[4, 4, 2], [8, 9, 4], [8, 9, 1]]
def findPairs(N):
  count = 0
  L = []
  L.append(I1)
  L.append(I2)
  L.append(I3)
  L.append(I4)
  L.append(I5)
  L.append(I6)
  
  for i in L:
    x = i
    print("Starting with MatA & List",i)
    while (True):
      c = x[0][0] + x[1][0] + x[2][0]
      if ( (c < N) and (x[0][0] <= x[1][0] ) and (x[1][0] <= x[2][0])):
      #if ( (c < N) ):
        print(x[0][0],x[1][0],x[2][0])
        count +=1
      elif( x[0][0] > N//3):
        print(x[0][0],N//3,"Breaking")
        break
      x = matMul(matA,x)

  print("Multiplication with MatrixAT")
  
  for i in L:
    x = i
    print("Starting with MatAT & List",i)
    while (True):
      x = matMul(matAT,x)
      c = x[0][0] + x[1][0] + x[2][0]
      if ( (c < N) and (x[0][0] <= x[1][0] ) and (x[1][0] <= x[2][0])):
        print(x[0][0],x[1][0],x[2][0])
        count +=1
      else:
        break


  return(count)

N = 500
n = bruteForce(N)
n1 = findPairs(N)
print("BruteForce for ",N,"=",n)
print("Regular",n1)
