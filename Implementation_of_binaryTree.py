# part 1

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        if self.left_child is None:
            self.left_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left_child = self.left_child
            self.left_child = new_node

    def insert_right(self, value):
        if self.right_child is None:
            self.right_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node

            
node_a = BinaryTree('a')

node_a.insert_left('b')
node_a.insert_right('c')

node_b = node_a.left_child
node_b.insert_left('d')
node_b.insert_right('e')

node_c = node_a.right_child
node_c.insert_left('f')
node_c.insert_right('g')

node_d = node_b.left_child
node_e = node_b.right_child
node_f = node_c.left_child
node_g = node_c.right_child

print("level 0 (root):", node_a.value)
print("level 1:", node_b.value)
print("level 1:", node_c.value)

print("level 2:", node_d.value)
print("level 2:", node_e.value)
print("level 2:", node_f.value)
print("level 2:", node_g.value)