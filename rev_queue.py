class Stack:
     def __init__(node):
         node.data = []
     def Empty(node):
         return node.data == []
     def push(node, data):
         node.data.append(data)
     def pop(node):
         return node.data.pop()


class Queue:
    def __init__(node):
        node.data = []
    def Empty(node):
        return node.data == []
    def enQueue(node, data):
        node.data.insert(0,data)
    def deQueue(node):
        return node.data.pop()

def Reverse():
    while( not Q.Empty()):
        S.push(Q.deQueue())
    while( not S.Empty()):
        Q.enQueue(S.pop())


S = Stack() 
Q = Queue()
Q.enQueue(5)
Q.enQueue(4)
Q.enQueue(3)
Q.enQueue(2)
Q.enQueue(1)
print(Q.data)
Reverse()
print(Q.data)




# program to reverse a queue  
from queue import Queue  
  
# Utility function to print the queue  
def Print(queue): 
    while (not queue.empty()): 
        print(queue.queue[0], end = ", ")  
        queue.get() 
  
# Function to reverse the queue  
def reversequeue(queue): 
    Stack = []  
    while (not queue.empty()):  
        Stack.append(queue.queue[0])  
        queue.get() 
    while (len(Stack) != 0):  
        queue.put(Stack[-1])  
        Stack.pop() 
  

if __name__ == '__main__': 
    queue = Queue() 
    queue.put(10)  
    queue.put(20)  
    queue.put(30)  
    queue.put(40)  
    queue.put(50)  
    queue.put(60)  
    queue.put(70)  
    queue.put(80)  
    queue.put(90)  
    queue.put(100)  
  
    reversequeue(queue)  
    Print(queue) 
  
