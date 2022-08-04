def remove(self, current_node):
    successor_node = current_node.next
    predecessor_node = current_node.prev

    if successor_node is not None:
        successor_node.prev = predecessor_node

    if predecessor_node is not None:
        predecessor_node.next = successor_node

    if current_node is self.head:
        self.head = successor_node

    if current_node is self.tail:
        self.tail = predecessor_node