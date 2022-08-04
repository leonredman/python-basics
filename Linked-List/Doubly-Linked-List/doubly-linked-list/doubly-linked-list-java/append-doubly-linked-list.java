public void append(Node newNode) {
   if (head == null) {
      head = newNode;
      tail = newNode;
   }
   else {
      tail.next = newNode;
      newNode.previous = tail;
      tail = newNode;
   }
}