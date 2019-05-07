# -*- coding: utf-8 -*-
"""
The easiest way to solve Maximum knocks that can happen on Queens board is using graphs.

#1. Each queen is nothing but a node in a Graph
#2. Each edge is the attackable position
#3. Aim is to find the largest path in the given Graph

#4. To add an edge for a node, try to get nearest possible attackable positions
    in all the eight directions for a Queen.
#5. Use recursive graph traversal algorithms (of course dynamically stored one)
"""

#Traverse in each of 8 directions & get if any queen in pos can 
#attack others
def getAttacks(queens,pos):
  i,j = pos
  #East - Nearest i > pos
  east = [(i,min([x[1] for x in queens if ( (x[0] == i) and (x[1] > j) )],default = None))]
  west = [(i,max([x[1] for x in queens if ( (x[0] == i) and (x[1] < j) )],default = None))]
  #North,South
  north = [(max([x[0] for x in queens if ( (x[1] == j) and (x[0] < i) )],default = None),j)]
  south = [(min([x[0] for x in queens if ( (x[1] == j) and (x[0] > i) )],default = None),j)]
  
  #diagonols 
  #desc = [x for x in queens  if ( (sum(x) == i+j) and (x[1]>j) and (x[0]<i)) ]
  aesc = [x for x in queens  if (sum(x) == i+j) ]
  desc = [x for x in queens  if ((x[0] - x[1]) == (i-j)) ]
  
  #North east - i < posi, j>posj and nearest one
  try:
    ne = [sorted([x for x in aesc if ( (x[0]<i) and (x[1]>j) )])[-1]]
  except:
    ne = []
  
  try:
    nw = [sorted([x for x in desc if ( (x[0]<i) and (x[1]<j) )])[-1]]
  except:
    nw = []
  
  #South east - i > posi, and nearest one
  try:
    se = [sorted([x for x in desc if ( (x[0]>i) and (x[1]>j) )])[0]]
  except:
    se = []
  
  try:
    sw = [sorted([x for x in aesc if ( (x[0]>i) and (x[1]<j) )])[0]]
  except:
    sw = []

  attacks = []
  for x in (east + west + north + south + ne + se + nw + sw):
    if None in x:
      pass
    else:
      attacks += [x]
  return attacks

#Classess Related to Graphs
class Node(object):
    def __init__(self, name):
        """Assumes name is a string"""
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, src, dest):
        """Assumes src and dest are nodes"""
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()

class Digraph(object):
    """edges is a dict mapping each node to a list of
    its children"""
    def __init__(self):
        self.edges = {}
    def addNode(self, node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.edges
    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)
    def getAllNodes(self):
      return list(self.edges.keys())
    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src + '->' + dest + '\n'
        return result[:-1] #omit final newline
def printPath(path):
    """Assumes path is a list of nodes"""
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result 

#todo: keep memo to improve
#Traverse Depth first wise on a Graph (BruteForce)
#This returns the number of knocks that can happen in each path.
#Caller should evaluate max of lengths, to find maximum knocks this start can take out
def DFS(graph, start, path, lengths, toPrint = False):
  path = path + [start]
  lengths += [len(path)]
  if toPrint:
    print('Current DFS path:', printPath(path))
  if (graph.childrenOf(start) == []):
    return path
  for node in graph.childrenOf(start):
    if node not in path: #avoid cycles
      DFS(graph, node, path, lengths, toPrint)
  return lengths

#Start of program
#N - Chess Size
#m - No. of pieces
#qIndex - index of all positions of queens (1,1),(3,1)..etc
#qMap- Dictionary to map which Queen is on position (1,1). qMap[(1,1)] = 'Q1' etc
#graph - Digraph that hosts all the nodes(Queens),edges(Paths between Queen)

N,m = map(int, input().rstrip().split())
qIndex = []
qMap = {}
graph = Digraph()
res = [["-"] * (N) for i in range(N)]

#Switch it on, if you need more output
debugFlag = False

#Read all pieces
for _ in range(m):
  i,j,p = input().rstrip().split(",")
  i,j = int(i),int(j)
  qIndex.append((i,j))
  qMap[(i,j)] = p
  graph.addNode(p)
  res[i-1][j-1] = p
qIndex.sort()

#For each  queen add node & edge
for x in qIndex:
  attackPositions = getAttacks(qIndex,x)
  edges = [qMap.get(x) for x in attackPositions]
  for n1 in edges:
    graph.addEdge(Edge(qMap[x],n1))

if(debugFlag):
  print("Graph After Adding all Nodes")
  print(graph)
  print("Mapping of all Nodes")
  for x in sorted(graph.getAllNodes()):
    tmp = graph.childrenOf(x)
    print(x,": "," --> ".join(tmp))

path = []
maxKnocks = 0
for x in sorted(graph.getAllNodes()):
  lengths = []
  knocks = DFS(graph,x,path,lengths,toPrint= debugFlag)
  if (debugFlag):
    print("If started with Node",x," It can knock down:",knocks)
  maxKnocks = max(max(knocks),maxKnocks)

#Print the result (m - maxKnocks)
print(m-maxKnocks)