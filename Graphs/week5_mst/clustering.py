#Uses python3
import sys
import math

class Node:
    def __init__(self,x,y,i):
        self.x = x
        self.y = y
        self.parent = i
        self.rank = 0

class Edge:
    def __init__(self, a, b, c):
        self.u = a
        self.v = b
        self.weight = c
        
def weight(x1,y1,x2,y2):
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
        
def MakeSet(i,nodes,x,y):
    return nodes.append(Node(x[i],y[i],i))

def Find(i,nodes):
    if (i != nodes[i].parent):
        nodes[i].parent = Find(nodes[i].parent,nodes)
    return nodes[i].parent

def Union(u,v,nodes):
    r1 = nodes[u].parent
    r2 = nodes[v].parent
    if (r1 != r2):
        if (nodes[r1].rank > nodes[r2].rank):
            nodes[r2].parent = r1
        else:
            nodes[r1].parent = r2
            if (nodes[r1].rank == nodes[r2].rank):
                nodes[r2].rank += 1
                
def clustering(x, y, k):
    n = len(x)
    nodes = []
    edges= []
    for i in range(n):
        MakeSet(i,nodes, x,y)
    for i in range(n):
        for j in range(i+1,n):
            edges.append(Edge(i,j,weight(x[i],y[i],x[j],y[j])))
    edges = sorted(edges,key = lambda edge: edge.weight)
    Union_num = 0
    for edge in edges:
        if Find(edge.u,nodes) != Find(edge.v,nodes):
            Union_num += 1
            Union(edge.u,edge.v,nodes)
        if(Union_num > n - k):
            return edge.weight
    return -1.


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
