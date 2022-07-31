int partition(int[] numbers, int startIndex, int endIndex) {
   // Select the middle value as the pivot.
   int midpoint = startIndex + (endIndex - startIndex) / 2;
   int pivot = numbers[midpoint];
   
   // "low" and "high" start at the ends of the array segment
   // and move towards each other.
   int low = startIndex;
   int high = endIndex;
   
   boolean done = false;
   while (!done) {
      // Increment low while numbers[low] < pivot
      while (numbers[low] < pivot) {
         low = low + 1;
      }
      
      // Decrement high while pivot < numbers[high]
      while (pivot < numbers[high]) {
         high = high - 1;
      }
      
      // If low and high have crossed each other, the loop
      // is done. If not, the elements are swapped, low is
      // incremented and high is decremented.
      if (low >= high) {
         done = true;
      }
      else {
         int temp = numbers[low];
         numbers[low] = numbers[high];
         numbers[high] = temp;
         low++;
         high--;
      }
   }

   // "high" is the last index in the left segment.
   return high;
}