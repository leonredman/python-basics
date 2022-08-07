public void append(int newItem) {
   // Resize if the array is full
   if (arrayData.length == arrayListLength) {
      resize(arrayListLength * 2);
   }

   // Insert the new item at index arrayListLength
   arrayData[arrayListLength] = newItem;

   // Increment the array's length
   ++arrayListLength;
}
   
public void resize(int newAllocationSize) {
   // Create a new array with the indicated size
   int[] newArray = new int[newAllocationSize];

   // Copy items in current array into the new array
   for (int i = 0; i < arrayListLength; ++i) {
      newArray[i] = arrayData[i];
   }

   // Assign the arrayData member with the new array
   arrayData = newArray;
}