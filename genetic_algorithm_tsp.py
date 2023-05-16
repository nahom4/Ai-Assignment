from queue import *
import graph_library as lib
import random
class Genetic_Algorithm:
    
    def __init__(self,graph,population_size = 100,generation = 100,mutation_rate= 0.5,percent=0.7) -> None:
        self.graph = graph
        self.mutation_rate = mutation_rate
        self.population = []
        self.percent = percent
        self.population_size = population_size  
        self.generation = generation
        chromosome = list(self.graph.keys())
        
        
        for _ in range(population_size):
            random.shuffle(chromosome)
            self.population.append((self.cost(chromosome),chromosome[:]))
    def path_inbetween(self,first,second):
        
        for _, cities in enumerate(self.graph[first]):
            
            if cities[0] == second:
                return cities[1]
        return None
            
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
    
    def cross_over(self,parent1,parent2):
        
        n = len(parent1)
        child1 = [-1] * n
        child2 = [-1] * n

        # Choose two random crossover points
        cx1, cx2 = sorted(random.sample(range(n), 2))

        # Copy the subsequence between the crossover points
        child1[cx1:cx2] = parent1[cx1:cx2]
        child2[cx1:cx2] = parent2[cx1:cx2]

        # Map any duplicate values in the copied subsequence
        for i in range(cx1, cx2):
            if parent2[i] not in child1:
                # Map the corresponding value in parent2 to child1
                j = parent2.index(parent1[i])
                while child1[j] != -1:
                    j = parent2.index(parent1[j])
                child1[j] = parent2[i]

            if parent1[i] not in child2:
                # Map the corresponding value in parent1 to child2
                j = parent1.index(parent2[i])
                while child2[j] != -1:
                    j = parent1.index(parent2[j])
                child2[j] = parent1[i]

        # Copy the remaining values from the parents
        for i in range(n):
            if child1[i] == -1:
                child1[i] = parent2[i]
            if child2[i] == -1:
                child2[i] = parent1[i]
        child1,child2 = self.mutate(child1),self.mutate(child2)
        return child1, child2

    def mutate(self,chromosome):
        #swap two random indices
        index1 = random.randint(0,len(chromosome)-1)
        index2 = random.randint(0,len(chromosome)-1)
        
        if random.random() < self.mutation_rate:
            chromosome[index1],chromosome[index2] = chromosome[index2],chromosome[index1]
            
        return chromosome
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
    
    def genetic_algorithm(self):
        
        for _ in range(self.generation):
            
            
            self.population.sort(key=lambda x:x[0])
            self.population = self.population[:int(self.percent*len(self.population))]  
            
            for _ in range((self.population_size - len(self.population)) // 2):
                parent1,parent2 = random.sample(self.population,2)
                child1,child2 = self.cross_over(parent1[1],parent2[1])
                # print('child1',child1)
                # print('child2',child2)
                self.population.extend([(self.cost(child1),child1),(self.cost(child2),child2)])      
           
        self.population.sort(key=lambda x:x[0])
        
        result = self.fill_the_gap(self.population[0][1]) 
        print(result)
        print(self.population[0][0])
        
        return result,self.population[0][0]
        
# graph = lib.newgraph.graph       
# genetic = Genetic_Algorithm(graph)
# print(genetic.genetic_algorithm())