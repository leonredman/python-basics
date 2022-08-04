# remove_after method

def remove_after(self, current_node):
    # Special case, remove head
    if (current_node == None) and (self.head != None):
        succeeding_node = self.head.next
        self.head = succeeding_node  
        if succeeding_node == None: # Remove last item
            self.tail = None
    elif current_node.next != None:
        succeeding_node = current_node.next.next
        current_node.next = succeeding_node
        if succeeding_node == None: # Remove tail
            self.tail = current_node