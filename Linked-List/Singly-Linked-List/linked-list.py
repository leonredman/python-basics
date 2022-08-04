# Node class definition and node initialization.
class Node:
    def __init__(self, initial_data):
        self.data = initial_data
        self.next = None

# Node initialization

node_a = Node(95)  # Creates a node with a data value of 95

# Class definition

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

# LinkedList initialization

num_list = LinkedList()  # Creates an empty linked list