from math import sqrt
from math import floor

V = int(raw_input())
MAX = 1000000

def round(num):
    return floor(num*100+.5)/100

def minKey(key, mstSet):
    min = MAX
    min_index = -1
    for v in range(0,V):
        if mstSet[v]==0 and key[v] < min:
            min = key[v]
            min_index = v
    return min_index
    
def printMST(parent, graph):
    print "{:.2f}".format(round(sum(graph[i][parent[i]] for i in range(1,V))))
    return

def MST(graph):
    parent = dict()
    key = dict()
    mstSet = dict()
    
    for i in range(0,V):
        key[i] = MAX
        mstSet[i] = 0
        
    key[0] = 0
    parent[0] = -1
    for count in range(0,V):
        u = minKey(key,mstSet)
        mstSet[u] = 1
        
        for v in range(0,V):
            if graph[u][v] and mstSet[v]==0 and graph[u][v] < key[v]:
                parent[v] = u
                key[v] = graph[u][v]
    printMST(parent, graph)


while V != 0:
    data = []
    for i in range(1, V+1):
        x,y = map(int, raw_input().split())
        data.append((x,y))
    
    graph = []
    for i in data:
        x = []
        for j in data:
            x1,y1 = i
            x2,y2 = j
            x.append( sqrt((x1-x2)**2 + (y1-y2)**2) )
        graph.append(x)
    MST(graph)
    
    V = int(raw_input())