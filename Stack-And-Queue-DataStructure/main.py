from Stack import Stack
from Queue import Queue
from Node import Node

# Stack operations
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
print('\n')


# Queue operations
num_queue = Queue()

node_d = Node(17)
node_e = Node(24)
node_f = Node(18)

num_queue.push(node_d)
num_queue.push(node_e)
num_queue.push(node_f)

# Output queue
print('Queue after push:', end=' ')
node = num_queue.list.head
while node != None:
   print(node.data, end=' ')
   node = node.next
print()

popped_node = num_queue.pop()  # Pop node_d

# Output final queue
print('Queue after pop:', end=' ')
node = num_queue.list.head
while node != None:
   print(node.data, end=' ')
   node = node.next
print()

'''
output
Stack after push: 11 56 45 
Stack after pop: 56 45 

Queue after push: 17 24 18 
Queue after pop: 24 18 
'''