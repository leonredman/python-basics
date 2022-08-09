from LinkedList import LinkedList
from Node import Node

class Queue:
    def __init__(self):
        self.list = LinkedList()
        
    def push(self, new_item):
        self.list.append(new_item)     # Insert as list tail (end of queue)
    
    def pop(self):
        popped_item = self.list.head   # Copy list head (front of queue)
        self.list.remove_after(None)   # Remove list head
        return popped_item             # Return popped item


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
Queue after push: 17 24 18 
Queue after pop: 24 18
'''