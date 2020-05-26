# Assignment 4 #

# 1. 
# d) is the answer
# 2. 
# a) is the answer

# from assignment text
#def hash_function(input_string, table_size):
#    total = 0
#    for pos in range(len(input_string)):
#        total = total + ord(input_string[pos])
#    return total % table_size
#
#my_list = ['qwerty', '123456', 'password', 'football']
#for item in my_list:
#    print(hash_function(item, 11), end='')

# 3.
# from the assignment text 
class Graph:
    graph = dict()
    def add_edge(self, node, neighbour):
        if node not in self.graph:
            self.graph[node] = [neighbour]
        else:
            self.graph[node].append(neighbour)

    # prints out the number of edges
    def print_num_of_edges(self):
        edgez = 0
        
        for nodez in self.graph:
            edgez += len(self.graph[nodez])
        print("\nTotalt antall kanter i grafen:", edgez)
                           

my_graph = Graph()
my_graph.add_edge('City 1', 'City 5')
my_graph.add_edge('City 2', 'City 4')
my_graph.add_edge('City 3', 'City Y')
my_graph.add_edge('City X', 'City 5')
my_graph.add_edge('City Y', 'City 1')
my_graph.add_edge('City Z', 'City 1')

# runs the method to get the total amount of edges in the graph my_graph
my_graph.print_num_of_edges()