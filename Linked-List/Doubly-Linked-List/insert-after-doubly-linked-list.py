def insert_after(self, current_node, new_node):
    if self.head is None:
        self.head = new_node
        self.tail = new_node
    elif current_node is self.tail:
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
    else:
        successor_node = current_node.next
        new_node.next = successor_node
        new_node.prev = current_node
        current_node.next = new_node
        successor_node.prev = new_node