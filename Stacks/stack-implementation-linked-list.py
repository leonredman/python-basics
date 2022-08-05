from LinkedList import LinkedList
from Node import Node

class Stack:
    def __init__(self):
        self.list = LinkedList()
        
    def push(self, new_item):
        self.list.prepend(new_item)    # Insert as list head (top of stack)
    
    def pop(self):
        popped_item = self.list.head   # Copy list head (top of stack)
        self.list.remove_after(None)   # Remove list head
        return popped_item             # Return popped item


num_stack = Stack()

node_a = Node(45)
node_b = Node(56)
node_c = Node(11)

num_stack.push(node_a)
num_stack.push(node_b)
num_stack.push(node_c)

# Output stack
print('Stack after push:', end=' ')
node = num_stack.list.head
while node != None:
   print(node.data, end=' ')
   node = node.next
print()

popped_node = num_stack.pop()  # Pop node_c

# Output final stack
print('Stack after pop:', end=' ')
node = num_stack.list.head
while node != None:
   print(node.data, end=' ')
   node = node.next
print()

'''
output
Stack after push: 11 56 45 
Stack after pop: 56 45
'''