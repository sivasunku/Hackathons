#!/bin/python3

import math
import os
import random
import re
import sys

Total = 0
iterN=0

def bruteForce(arr):
  L = len(arr)
  count = 0
  for i in range(L):
    for j in range(i+1,L):
      m = max(arr[i:(j+1)],default = arr[i])
      if ((arr[i] * arr[j]) <= m):
        #print("(",i,j,")")
        count += 1
  #print("BruteForce:",count)
  return(count)
# Divide the array into left & right to the Max element present
# sort left part & right part (Decreasing order)
# Start at maximum of left part , start multiplying with max of right part, 
#   till prod is greater than Max
#   TotalPairs = remaining * remaining right
# Repeat this process untill atleast one value is moved.
#  Repeat this process for Left & right arrays
# 

#Check single pair for one iteration
# left -array,Right Array, max value 
# Returns the paris with i,j where i*j <= Max
def checkPair(left,right,m):
  s_left = left.copy()
  s_left.sort(reverse = True)
  s_left_len = len(s_left)
    
  s_right = right.copy()
  s_right.sort(reverse = True)
  s_right_len = len(s_right)
    
  #if ((s_right_len <=10) or (s_left_len <=10)):
  #  return bruteForce(left+right)

  i_loop = j_loop = True
  count = i = j = 0
  while ( (i_loop == True) and (i < s_left_len) ):
    j = 0
    i_loop = False
    j_loop = True
    while ( (j_loop == True) and (j < s_right_len) ):
      if ( (s_left[i] * s_right[j]) > m):
        i_loop = True
        j += 1
      else:
        j_loop = False
    #While loop else
    else:
      #Add number of remaining elements in left * right to Count
      count += (s_right_len -j)
    i += 1
  else:
    count += (s_right_len) * (s_left_len - i)
  return count

#find the max value and divide the array to left & right
def solve(inp):
  global Total
  global iterN
  iterN += 1
  if (len(inp) == 0):
    return 0
  if (len(inp) <= 10):
    return bruteForce(inp)

  m = inp.index(max(inp))
  left = inp[:m]
  right = inp[m+1:]
  print("In Iter:",iterN,len(inp))
  temp = checkPair(inp[:m],inp[m:],inp[m])
  print("Left:",len(left),"Right:",len(right),"Input:",len(inp))
  print("temp:", temp)
  print("======================================================")
  #print("After checkpair Total:",Total)
  #print("Left\n",left)
  #print("Right\n",right)
  return ( temp + solve(left) + solve(right))

  
if __name__ == '__main__':
    
    fptr = open("result.txt", 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = solve(arr[:arr_count])
    print("Grand Result:", result)
    print("With Brute Force Grand",bruteForce(arr))
    fptr.write(str(result) + '\n')

    fptr.close()
