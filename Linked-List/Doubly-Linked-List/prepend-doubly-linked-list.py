def prepend(self, new_node):
   if self.head == None:
      self.head = new_node
      self.tail = new_node
   else:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node