class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def my_function1(input_list):
    my_stack = Stack()
    my_list = []
    for item in input_list:
        my_stack.push(item)
    while not my_stack.is_empty():
        my_list.append(my_stack.pop())
    print(my_list)

my_list = [20, 30, 40, 50]
my_function1(my_list)