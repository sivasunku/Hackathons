#!/bin/python3

import os
import sys

#
# Complete the downToZero function below.
#
def factors(n):
  t = int((n ** 0.5) // 1)
  for i in range(t+1,1,-1):
    if ((n % i) == 0):
      return(max(n/i,i))
  return(n)

def downToZero(n):
  count = 0
  while (n > 0):
    print("n at outer:",n,count)
    while (True):
      print("n at inner:",n,count)
      k = factors(n)
      if (k == n):
        break
      else:
        count += 1
        n = k
    n -= 1
    count += 1
  print(count)
  return(count)

  
if __name__ == '__main__':
    #fptr = open("result.txt", 'w')
    #q = int(input())

    for q_itr in range(q):
        n = int(input())
        result = downToZero(n)
        fptr.write(str(result) + '\n')
    fptr.close()
