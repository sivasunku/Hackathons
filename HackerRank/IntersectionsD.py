# -*- coding: utf-8 -*-
"""
Created on Fri May  3 16:43:47 2019

@author: siva
"""

# -*- coding: utf-8 -*-
"""
Created on Fri May  3 15:51:17 2019

@author: siva
"""
def inLine(x,y,line1):
  #print("Check:",x,y,line1)
  (x1,y1),(x2,y2) = line1
  if ( (y>=min(y1,y2)) and (y<=max(y1,y2))  and \
       (x>=min(x1,x2)) and (x<=max(x1,x2)) ):
    return True
    return False

def line_intersection(line1, line2):
  xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
  ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1]) #Typo was here
  
  det = lambda a,b:a[0] * b[1] - a[1] * b[0]

  div = det(xdiff, ydiff)
  if div == 0:
    return False
  d = (det(*line1), det(*line2))
  x = det(d, xdiff) / div
  y = det(d, ydiff) / div
  if (inLine(x,y,line1) and inLine(x,y,line2)):
    return True
  else:
    return False
  
N = int(input())
pairs = []
count = 0
for _ in range(N):
  x1,y1,x2,y2 = map(int, input().rstrip().split())
  pairs.append([(x1,y1),(x2,y2)])
for i,l1 in enumerate(pairs):
  for l2 in pairs[i+1:]:
    #print(i,l1,l2)
    if ( line_intersection(l1,l2) ):
      count += 1
print(count)
