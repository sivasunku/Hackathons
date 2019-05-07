# -*- coding: utf-8 -*-
"""
Created on Fri May  3 15:51:17 2019

@author: siva
"""

#Read input
class Node(object):
  def __init__(self, name):
    """Assumes name is a string"""
    self.name = name
    self.remaining = name
    self.parts = []
    self.status = False
  #If part is in remaining, add it.
  #Remove the characters in remaining
  #Returns - True if replaced, else False
  def addPart(self,part):
    if part in self.remaining:
      self.parts += [part]
      self.remaining = self.remaining.replace(part,"")
      return True
    return False
  def getStatus(self):
    return self.status
  def getName(self):
    return self.name
  def getParts(self):
    return self.parts
  def __str__(self):
    return ("Name:" + self.name \
            + "\n Remaining:" \
            + self.remaining \
            + "\n Parts:"\
            + str(self.parts) \
            + "\n Status" \
            + str(self.status)\
            + "\n")

N = int(input())
Names = []
inp = []
for _ in range(N):
  inp += [input()]
inp.sort()

for x in inp:
  n= Node(x)
  Names += [n]

inpParts = []
m = int(input())
for _ in range(m):
  inpParts += [input()]
inpParts = sorted(inpParts,key=len,reverse = True)
for shred in inpParts:
  for ele in Names:
    #Try adding element
    if (ele.addPart(shred)):
      #print("Added for", ele.getName())
      break
for x in Names:
  print(x.getName()+":["+", ".join(x.getParts())+"]")
