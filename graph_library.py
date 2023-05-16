from collections import *



class Node:
    
    
    def __init__(self, value, edges = []):
        self.value = value
        self.edges = edges


class graph:
    
    
    def __init__(self):
        self.graph = defaultdict(list)




    def insert_node(self, value, edges):
        newnode = Node(value, edges)
        
        for node in newnode.edges:
            if (newnode.value,node[1]) not in self.graph[node[0]]:
                self.graph[node[0]].append((newnode.value,node[1]))
            if node not in self.graph[newnode.value]:
                self.graph[newnode.value].append(node)
            

        return self.graph
    
    
    
    
    def printer(self):
        print(dict(self.graph))




    def getSuccessor(self, node):
        return self.graph[node]
  
  
  
        
    def delete_node(self, node):
        for child in self.graph[node]:
            self.graph[child].remove(node)
        del(self.graph[node])
    
    
    
    
    def delete_edge(self, start_node, end_node):
        self.graph[start_node].remove(end_node)
        self.graph[end_node].remove(start_node)
    
    
    
    
    def insert_edge(self, start_node, end_node):
        self.graph[start_node].append(end_node)
        
                

#let's create the graph
def create_graph(file_name):
    
    file1 = open(f'{file_name}.txt', 'r')
    lines = file1.readlines()

    newgraph = graph()

    for count,line in enumerate(lines):
        start,lat1,long1,goal,lat2,long2,weight = line.split()
        newgraph.insert_edge(start,(goal,int(weight)))
        newgraph.insert_edge(goal,(start,int(weight)))


    file1.close()
    return newgraph.graph




    






