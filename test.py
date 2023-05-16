import timeit
from tsp import main    
#time hill climbing, simulated annealing and genetic algorithm  
from tabulate import tabulate
import matplotlib.pyplot as plt

def draw_graph(graphs,algorithms,table,ylable):
     # Set the width of each bar
    bar_width = 0.2
    print(graphs)
    print(algorithms)
    print(table)
   
    # Calculate the x positions for the bars
    x_pos = [i for i in range(len(algorithms))]

    # Create the bar plot for each algorithm and test case
    for i in range(len(algorithms)):
        plt.bar([x + i * bar_width for x in x_pos], table[i], width=bar_width, label=algorithms[i])
    
        
    plt.xlabel('Test Cases')
    plt.ylabel(f'{ylable}')
    plt.title('Comparison of Algorithms')

    plt.xticks([x + bar_width for x in x_pos], graphs)

    plt.legend()
    
    plt.show()
    

def test():
    
    algorithms = ['hc','sa','ga']
    graphs = ['cities_8','cities_16',"cities_20"]
    execution_time = [[algorithms[i]] for i in range(3)]  
    cost_table = [[algorithms[i]] for i in range(3)]
    for graph in graphs:
        for index,algorithm in enumerate(algorithms):
            start = timeit.default_timer()
            _,cost = main(algorithm,graph)
            finish = timeit.default_timer()
            #use tables to display results
            execution_time[index].append(round(finish - start,3))
            cost_table[index].append(cost)
            print(f'{algorithm} on {graph} took {round(finish - start,3)} seconds')
       

    col_names = ["Algorithm", "cities_8","cities_16","cities_20"]
    execution_time.insert(0,col_names)
    table_text = tabulate(execution_time,tablefmt="fancy_grid")
    print(table_text)
    
    cost_table.insert(0,col_names)
    table_text = tabulate(cost_table,tablefmt="fancy_grid")
    print(table_text)
    
    execution_time.pop(0)
    cost_table.pop(0)   
    [lis.pop(0) for lis in execution_time]
    [lis.pop(0) for lis in cost_table]
  
    draw_graph(graphs,algorithms,execution_time,"Execution Time")    
    draw_graph(graphs,algorithms,cost_table,"Cost")    
    
test()
