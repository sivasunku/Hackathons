import pandas as pd

#This function 
#   Builds the circles/layers co-ordinates of each layer.
#   Finds the position of X in each layer
def makeLayers(m,matrix):
  #Layers for m=5, 2,1,0
  noOfLayers = m // 2
  layers = []
  passages = []
  for x in range(noOfLayers):
    tmp = []
    #Move East
    i = x
    for j in range(x,m-x):
      tmp.append((i,j))
    #Move South
    j = m - 1 - x
    for i in range(x+1,m-x):
      tmp.append((i,j))
    #Move West
    i = m - 1 - x
    for j in range(m - x - 2,x-1,-1):
      tmp.append((i,j))
    #Move North
    j = x
    for i in range(m - x-2,x,-1):
      tmp.append((i,j))
    
    #Find the position of 'X' in the layer.
    #If it is near to starting, rotate counter clockwise, else -ve clockwise
    for t1 in tmp:
      p,q = t1
      if matrix[p][q] == 'X':
        xpos = tmp.index(t1)
        total = len(tmp)
        if xpos > ( total - xpos):
          xpos = -1 * (total - xpos)
        passages.append(xpos)
      
    layers.append(tmp)
  return layers,passages

#Shift the layer to 'n' counter clockwise, -n indicates clockwise
def Shift(chain,n): 
  return(chain[n:] + chain[:n])

#This will be called for each of the test case
def mainFunction(m,matrix):

  #make a replica of resultant matrix, either with zeroes/nulls/values.
  res = [row[:] for row in matrix]

  #Get layers co-ordinates to ls & xs - position of X in layer 
  origLayer,xPosition = makeLayers(m,matrix)

  #For each of the layer
  #  Shift the layer by 'X' position
  #  The new co-ordinates will be in tmp.
  #  Copy each of the original layer co-ordinates content with new shifted layer
  #   co-ordinates
  for n in range(0,len(origLayer)):
    shiftedLayer = Shift(origLayer[n],xPosition[n])
    for i in range(0,len(origLayer[n])):
      p0,q0 = origLayer[n][i]
      p,q = shiftedLayer[i]
      res[p0][q0] = matrix[p][q]

  #PS: Pandas shouldn't be used for real hackathon. To be changed to forloop print
  if (len(xPosition) == 0):
    print(0)
  else:
    print(" ".join(map(str,xPosition)))
  print(pd.DataFrame(res).to_string(index = False,header = False))

#Execute for each of the test case.
maxCases = int(input())
print(maxCases + 1)
for _ in range(maxCases):
  size = int(input())
  matrix = []
  for _ in range(size):
    matrix.append(list(input().rstrip().split()))
  mainFunction(size,matrix) 
