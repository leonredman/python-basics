public void insertionSortDoublyLinked() {
   Node currentNode = m_head.next;
   while (currentNode != null) {
      Node nextNode = currentNode.next;
      Node searchNode = currentNode.previous;
         
      while (searchNode != null && searchNode.data > currentNode.data)
         searchNode = searchNode.previous;
      
      // Remove and re-insert currentNode
      remove(currentNode);
      if (searchNode == null) {
         currentNode.previous = null;
         prepend(currentNode);
      }
      else {
         insertAfter(searchNode, currentNode);
      }

      // Advance to next node
      currentNode = nextNode;
   }
}