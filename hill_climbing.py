import graph_library as lib
import random
from queue import *

class Hill_Climbing:
    
    def __init__(self,graph) -> None:
        self.graph = graph
        
    def shortest_path(self,start,end):
        queue = PriorityQueue()
        queue.put((0,start))
        visited = set()
        visited.add(start)
        path_list = dict()
        last = None
        while not queue.empty():
            #let's pop the top element and see if it is the goal state
        
            total_cost,parent = queue.get()
        
            if parent == end:
                last = parent
                break
            #lets add the children or parent to the stack
            
            child_list = self.graph[parent]
            for child in child_list:
                location,cost = child
                if not location in visited:
                    if location in path_list:
                        current_cost = total_cost + cost
                        if path_list[location][-1] > current_cost:
                            path_list[location] = (parent,cost)
                            queue.put((current_cost,location))
                            
                        visited.add(location)
                            
                    else:
                        current_cost = total_cost + cost
                        queue.put((current_cost,location))
                        visited.add(location)
                        path_list[location] = (parent,cost)

        #now let's collect all the steps required to reach from the start state to the last state
        res = []
        if last:
            while True:
                res.append(last)
                if last == start:
                    break
                location,cost = path_list[last]
                last = location

            return res[1:], total_cost
        
    # Get the neighbors 
    def two_opt_swap(self,tour):
        n = len(tour)
        # Select two distinct indices i and j
        i, j = random.sample(range(n), 2)
        # Ensure that i < j-1
        i, j = min(i, j), max(i, j)
        if i == 0 and j == n-1:
            return tour # avoid trivial solution
        # Reverse the order of the edges between i+1 and j
        new_tour = tour[:i+1] + list(reversed(tour[i+1:j])) + tour[j:]
        return new_tour
    def get_neighbors(self,state):
        
        # to get the neighbors we will use the two opt swap
        neighbors = []
        for _ in range(100):
            neighbors.append(self.two_opt_swap(state))
            
        return neighbors
    #checks the existence of a path
    def path_inbetween(self,first,second):
        
        for _, cities in enumerate(self.graph[first]):
            
            if cities[0] == second:
                return cities[1]
        return None

    #This is the cost function
    def cost(self,state):
        total_cost = 0
        for i in range(len(state)-1): 
            #There are two cases the two cities are connected or not
            cost_in_between = self.path_inbetween(state[i],state[i + 1])
            if cost_in_between:
                total_cost += cost_in_between
                
            else:
                _,cost = self.shortest_path(state[i],state[i + 1])
                total_cost += cost
            
        return total_cost


    def fill_the_gap(self,curr_state):
        new_state = []
        n = len(curr_state)
        for i in range(n):
            if not self.path_inbetween(curr_state[i],curr_state[(i + 1) % n ]):
                path,_ = self.shortest_path(curr_state[i],curr_state[(i + 1) % n])
                new_state.extend(path[::-1])
            else:
                new_state.append(curr_state[i])
    
        new_state.append(curr_state[0])
        
        return new_state

    #This is where executions begin
    def hill_climbing(self,curr_state):
        
        curr_cost = self.cost(curr_state)
        while True:
            neighbors = self.get_neighbors(curr_state)
            neighbor_cost = []
            for index,neighbor in enumerate(neighbors):
                path_cost = self.cost(neighbor)
                neighbor_cost.append(path_cost)
                
            if min(neighbor_cost) >= curr_cost:
                break
            else:
                curr_cost = min(neighbor_cost)
                curr_state = neighbors[neighbor_cost.index(curr_cost)]
        print(curr_state)
        print(curr_cost)        
        return self.fill_the_gap(curr_state),curr_cost
    


# graph = lib.newgraph.graph
# curr_state = list(graph.keys())    
# curr_state = random.sample(curr_state,len(curr_state))
# obj = Hill_Climbing(graph)
# print(obj.hill_climbing(curr_state))
    
    
    