from LinkedList import LinkedList

class Stack:
    def __init__(self):
        self.list = LinkedList()
        
    def push(self, new_item):
        self.list.prepend(new_item)    # Insert as list head (top of stack)
    
    def pop(self):
        popped_item = self.list.head   # Copy list head (top of stack)
        self.list.remove_after(None)   # Remove list head
        return popped_item             # Return popped item
