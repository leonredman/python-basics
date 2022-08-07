public void prepend(int newItem) {
   // Resize if the array is full
   if (arrayData.length == arrayListLength) {
      resize(arrayListLength * 2);
   }

   // Shift all array items to the right,
   // starting from the last index and moving 
   // down to the first index
   for (int i = arrayListLength; i > 0; --i) {
      arrayData[i] = arrayData[i - 1];
   }

   // Insert the new item at index 0
   arrayData[0] = newItem;
        
   // Update the array list's length
   ++arrayListLength;
}
   
public void insertAfter(int index, int newItem) {
   // Resize if the array is full
   if (arrayData.length == arrayListLength) {
      resize(arrayListLength * 2);
   }

   // Shift all the array items to the right,
   // starting from the last item and moving down to
   // the item just past the given index
   for (int i = arrayListLength; i > index + 1; --i) {
      arrayData[i] = arrayData[i - 1];
   }

   // Insert the new item at the index just past the
   // given index
   arrayData[index + 1] = newItem;
        
   // Update the array's length
   ++arrayListLength;
}