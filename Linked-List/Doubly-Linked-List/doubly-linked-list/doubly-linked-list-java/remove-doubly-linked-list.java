public void remove(Node currentNode) {
   Node successor = currentNode.next;
   Node predecessor = currentNode.previous;
      
   if (successor != null)
      successor.previous = predecessor;
         
   if (predecessor != null)
      predecessor.next = successor;
         
   if (currentNode == head)
      head = successor;
         
   if (currentNode == tail)
      tail = predecessor;
}