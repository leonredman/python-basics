# append() method definition

def append(self, new_node):
    if self.head == None:
        self.head = new_node
        self.tail = new_node
    else:
        self.tail.next = new_node
        self.tail = new_node
  
# append() method call

node_a = Node(95)    # Creates a node with a data value of 95
node_b = Node(42)    # Creates a node with a data value of 42

num_list.append(node_a)  # Method call has one argument
num_list.append(node_b)