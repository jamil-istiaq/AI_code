# -*- coding: utf-8 -*-
"""18-37918-2-week-4-v2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19Kq08j07ggceRDoPXoTA-ATjAtbBNs_w

# Name: Istiaq Md. Jamil
ID: 18-37918-2
Sec:F

# BFS
"""

romanian_map = {
    'Arad': {'Sibiu':140, 'Zerind':75, 'Timisoara':118},
    'Zerind': {'Arad':75, 'Oradea':71},
    'Oradea': {'Zerind':71, 'Sibiu': 151},
    'Sibiu': {'Arad':140, 'Oradea':151, 'Fagaras':99, 'Rimnicu':80},
    'Timisoara': {'Arad': 118, 'Lugoj':111},
    'Lugoj': {'Timisoara':111, 'Mehadia':70},
    'Mehadia': {'Lugoj': 70, 'Drobeta':75},
    'Drobeta': {'Mehadia':75, 'Craiova':120},
    'Craiova': {'Drobeta': 120, 'Rimnicu': 146, 'Pitesti': 138},
    'Rimnicu': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu':99, 'Bucharest':211},
    'Pitesti': {'Rimnicu': 97, 'Craiova':138, 'Bucharest':101},
    'Bucharest': {'Fagaras':211, 'Pitesti': 101, 'Giurgiu':90, 'Urziceni':85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Vaslui':142, 'Hirsova':98},
    'Hirsova': {'Urziceni':98, 'Eforie':86},
    'Eforie': {'Hirsova':86},
    'Vaslui': {'Iasi': 92, 'Urziceni':142},
    'Iasi': {'Vaslui':92, 'Neamt': 87},
    'Neamt': {'Iasi':87}
}

romanian_map['Arad']['Zerind']

romanian_map['Arad']

romanian_map['Zerind']['Arad']

from queue import Queue


def bfs(startingNode, destinationNode):
    visited = {}#to store explored nodes
    print('Intitally Explore node is Empty')
    distance = {}
    print('Intitally Distance is Empty')
    parent = {}#to store path
    print('Intitally Parent node is Empty\n')

    bfs_traversal_output = []#to store the order of traversal
    frontier = Queue()

    for city in romanian_map.keys():
        visited[city] = False #if not visited
        parent[city] = None
        distance[city] = -1 #innitialize

    startingCity = startingNode
    visited[startingCity] = True
    distance[startingCity] = 0
    frontier.put(startingCity)    # arad
    print(startingCity,'Store Just Before starting\n')
    
    found = False #for breaking the loop later

    while not frontier.empty():
        u = frontier.get()     # in the first iteration it will be arad
        print(u,'is in the Frontier')
        bfs_traversal_output.append(u)
        print('Tree of traversal=',bfs_traversal_output,'\n')

        for v in romanian_map[u].keys():
            print(v,'Exploring From',u)
            
            if not visited[v]:                
                visited[v] = True
                parent[v] = u
                print(u,'Is the Parent of',v)
                distance[v] = distance[u] + romanian_map[u][v]                
                print(distance[v],'is the total distace from',u,'\n')
                frontier.put(v)
                if v== destinationNode:
                    found =True
                    break
                
        if found: break
            
    g = destinationNode
    path = []
    while g is not None:
        path.append(g)
        g = parent[g]
    
    path.reverse()
    print('Path is', path)
    print('Distance',distance[destinationNode])
    print('BFS Traversal Sequence',bfs_traversal_output)

bfs('Arad', 'Bucharest')

"""# Uniform Cost Search"""

from queue import PriorityQueue

def ucs(startingNode, destinationNode):
    visited = {}
    distance = {}
    parent = {}
    print("Initally all are Empty")

    ucs_traversal_output = []  #initially
    pq = PriorityQueue() #initially

    for city in romanian_map.keys():
        visited[city] = False
        parent[city] = None  
        distance[city] = -1
        

    startingCity = startingNode
    print('Starting From:',startingNode)
    
    visited[startingCity] = True
    distance[startingCity] = 0
    pq.put((0,startingCity)) #put the name
    print('Put',(startingCity),'in the Queue')

    while not pq.empty():
        u = pq.get()[1] #get only name of city     
        ucs_traversal_output.append(u)
        print('Traversal Tree',ucs_traversal_output)
        
        if u== destinationNode:
            break
        visited[u] = True
        for v in romanian_map[u].keys():
            print(v,'Exploring From',u)
            if not visited[v]:                
                parent[v] = u
                print(u,'Is the Parent of',v)
                distance[v] = distance[u] + romanian_map[u][v]
                print(distance[v],'is the total distace from',u,'\n')
                pq.put((distance[v],v))
                print('Put',v,'in the Queue')

    g = destinationNode
    path = []
    while g is not None:
        path.append(g)
        g = parent[g]
        

    path.reverse()
    print('Path is:',path)
    print('Distance:',distance[destinationNode])
    print('UCS sequence:',ucs_traversal_output)


ucs('Arad', 'Bucharest')

"""# DFS"""

visited = set() # Set to keep track of visited nodes.

def dfs(visited, romanian_map, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in romanian_map[node]:
            dfs(visited, romanian_map, neighbour)

# Driver Code
dfs(visited, romanian_map, 'Arad')

"""not compeleted sir. I will compelet it and send it to you sir """

from queue import Queue, PriorityQueue

def dfs(graph, start, end):
    frontier = [start, ]
    explored = []
    current_node = []

    while True:
        if len(frontier) == 0:
            #raise Exception("No way Exception")
            current_node = frontier.pop()
            explored.append(current_node)
            print(current_node)

        # Check if node is goal-node
        if current_node == end:
            return

        # expanding nodes
        for node in reversed(graph[current_node]):
            if node not in explored:
                frontier.append(node)
                
dfs(romanian_map, 'Arad', 'Bucharest')