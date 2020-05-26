# Assignment 5 #

# 1. 
# graph 1: width = 2, height = 4, size = 7, 
# graph 2: width = 4, height = 5, size = 13, 
# graph 3: width = 2, height = 5, size = 9, 
# 1 = full
# 2 = full
# 3 = full
# answer: d) all are full


# 2.

def binary_tree(r):
    return [r, [], []]

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]

def insert_left_child(root, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root

def insert_right_child(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])
    return root


my_tree = binary_tree('a')

insert_left_child(my_tree, 'b')
insert_right_child(my_tree, 'c')

insert_right_child(get_right_child(my_tree), 'd')
insert_left_child(get_right_child(get_right_child(my_tree)), 'e')

#print(my_tree)
# answer:
# C. ['a', ['b', [], []], ['c', [], ['d', ['e', [], []], []]]]

# 2.1
# a)

class Graph():
    graph = dict()

    def add_edge(self, node, neighbour):
        if node not in self.graph:
            self.graph[node] = [neighbour]
        else:
            self.graph[node].append(neighbour)
    
    def print_graph(self):
        print(self.graph)

    def breadth_first_search(self, node):
        searched = []
        search_queue = [node]

        while search_queue:
            searched.append(node)
            node = search_queue.pop(0)

            print("[", node, end=" ], ")
            for neighbour in self.graph[node]:
                if neighbour not in searched:
                    searched.append(neighbour)
                    search_queue.append(neighbour)


def build_my_graph2():
    my_graph = Graph()
    
    my_graph.add_edge(1, 2)
    my_graph.add_edge(1, 3)
    my_graph.add_edge(2, 4)
    my_graph.add_edge(2, 3)
    my_graph.add_edge(3, 5)
    my_graph.add_edge(4, 5)
    my_graph.add_edge(5, 6)
    my_graph.add_edge(6, 3)

    my_graph.breadth_first_search(1)


build_my_graph2()

