# insert method - singly linked list

def insert_after(self, current_node, new_node):
    if self.head == None:
        self.head = new_node
        self.tail = new_node
    elif current_node is self.tail:
        self.tail.next = new_node
        self.tail = new_node
    else:
        new_node.next = current_node.next
        current_node.next = new_node