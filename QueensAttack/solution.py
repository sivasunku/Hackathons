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

# Traverse in each of 8 directions & get if any queen in pos can
# attack others


def get_attacks(queens, pos):
    i, j = pos
    # East - Nearest i > pos
    east = [(i, min([x[1] for x in queens if ((x[0] == i) and (x[1] > j))], default=None))]
    west = [(i, max([x[1] for x in queens if ((x[0] == i) and (x[1] < j))], default=None))]

    # North,South
    north = [(max([x[0] for x in queens if ((x[1] == j) and (x[0] < i))], default=None), j)]
    south = [(min([x[0] for x in queens if ((x[1] == j) and (x[0] > i))], default=None), j)]

    # diagonals
    # desc = [x for x in queens  if ( (sum(x) == i+j) and (x[1]>j) and (x[0]<i)) ]
    aesc = [x for x in queens if (sum(x) == i+j)]
    desc = [x for x in queens if ((x[0] - x[1]) == (i-j))]

    # North east - i < posi, j > posj and nearest one
    try:
        ne = [sorted([x for x in aesc if ((x[0] < i) and (x[1] > j))])[-1]]
    except:
        ne = []

    try:
        nw = [sorted([x for x in desc if ((x[0] < i) and (x[1] < j))])[-1]]
    except:
        nw = []
  
    # South east - i > posi, and nearest one
    try:
        se = [sorted([x for x in desc if ((x[0] > i) and (x[1] > j))])[0]]
    except:
        se = []
  
    try:
        sw = [sorted([x for x in aesc if ((x[0] > i) and (x[1] < j))])[0]]
    except:
        sw = []

    attacks = []
    for x in (east + west + north + south + ne + se + nw + sw):
        if None in x:
            pass
        else:
            attacks += [x]
    return attacks


# classes Related to Graphs
class Node(object):
    def __init__(self, name):
        """Assumes name is a string"""
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name


class Edge(object):
    def __init__(self, src, dest):
        """Assumes src and dest are nodes"""
        self.src = src
        self.dest = dest

    def get_source(self):
        return self.src

    def get_destination(self):
        return self.dest

    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()


class Digraph(object):
    """  edges is a dict mapping each node to a list of
    its children
    """
    def __init__(self):
        self.edges = {}

    def add_node(self, node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = []

    def add_edge(self, edge):
        src = edge.get_source()
        dest = edge.get_destination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

    def children_of(self, node):
        return self.edges[node]

    def has_node(self, node):
        return node in self.edges

    def get_node(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)

    def get_all_nodes(self):
        return list(self.edges.keys())

    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src + '->' + dest + '\n'
        return result[:-1]
        # omit final newline


def print_path(path):
    """  Assumes path is a list of nodes  """
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result 


def dfs(graph, start, path, lengths, to_print=False):
    """
        todo: keep memo to improve
        Traverse Depth first wise on a Graph (BruteForce)
        This returns the number of knocks that can happen in each path.
        Caller should evaluate max of lengths, to find maximum knocks this start can take out
    """
    path = path + [start]
    lengths += [len(path)]
    if to_print:
        print('Current dfs path:', print_path(path))

    if not graph.children_of(start):
        return lengths

    for node in graph.children_of(start):
        if node not in path:
            # avoid cycles
            dfs(graph, node, path, lengths, to_print)
    return lengths

# Start of program
# N - Chess Size
# m - No. of pieces
# q_index - index of all positions of queens (1,1),(3,1)..etc
# q_map- Dictionary to map which Queen is on position (1,1). qMap[(1,1)] = 'Q1' etc
# graph - Digraph that hosts all the nodes(Queens),edges(Paths between Queen)


N, m = map(int, input().rstrip().split(","))
q_index = []
q_map = {}
graph = Digraph()
res = [["-"] * N for i in range(N)]

# Switch it on, if you need more output
debug_flag = False

# Read all pieces
for _ in range(m):
    i, j, p = input().rstrip().split(",")
    i, j = int(i), int(j)
    q_index.append((i, j))
    q_map[(i, j)] = p
    graph.add_node(p)
    res[i-1][j-1] = p
    q_index.sort()

# For each  queen add node & edge
for x in q_index:
    attack_positions = get_attacks(q_index, x)
    edges = [q_map.get(x) for x in attack_positions]
    for n1 in edges:
        graph.add_edge(Edge(q_map[x], n1))

if debug_flag:
    print("Graph After Adding all Nodes")
    print(graph)
    print("Mapping of all Nodes")
    for x in sorted(graph.get_all_nodes()):
        tmp = graph.children_of(x)
        print(x, ": ", " --> ".join(tmp))

path = []
max_knocks = 0
all_nodes = sorted(graph.get_all_nodes())

for x in all_nodes:
    lengths = []
    knocks = dfs(graph, x, path, lengths, to_print=debug_flag)

    if debug_flag:
        print("If started with Node", x, " It can knock down:", knocks)
    max_knocks = max(max(knocks), max_knocks)


print(m-max_knocks+1)
