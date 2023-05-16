import sys
import graph_library as lib
from simulated_annealing import Simulated_Aneling 
from hill_climbing import Hill_Climbing
from genetic_algorithm import Genetic_Algorithm
import random

def main(algorithm: str, filePath: str):
    graph = lib.create_graph(filePath)
    if algorithm == "ga":
        genetic = Genetic_Algorithm(graph)
        return genetic.genetic_algorithm()
    
    elif algorithm == "hc":
    
        curr_state = list(graph.keys())    
        curr_state = random.sample(curr_state,len(curr_state))
        obj = Hill_Climbing(graph)
        return obj.hill_climbing(curr_state)
        


    elif algorithm == "sa":
    
        curr_state = list(graph.keys())    
        curr_state = random.sample(curr_state,len(curr_state))
        obj = Simulated_Aneling(graph)
        return obj.simulated_annealing(curr_state)
        


if __name__ == '__main__':
    args = sys.argv
    alg = args.index('--algorithm')
    file = args.index('--file')

    main(algorithm=args[alg+1], filePath=args[file+1])