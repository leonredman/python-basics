public void insertAfter(Node currentNode, Node newNode) {
   if (head == null) {
      head = newNode;
      tail = newNode;
   }
   else if (currentNode == tail) {
      tail.next = newNode;
      newNode.previous = tail;
      tail = newNode;
   }
   else {
      Node successor = currentNode.next;
      newNode.next = successor;
      newNode.previous = currentNode;
      currentNode.next = newNode;
      successor.previous = newNode;
   }
}