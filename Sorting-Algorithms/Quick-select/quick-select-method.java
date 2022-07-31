int quickselect(int[] numbers, int startIndex, int endIndex, int k) {
   if (startIndex >= endIndex) {
      return numbers[startIndex];
   }

   int lowLastIndex = partition(numbers, startIndex, endIndex);
   if (k <= lowLastIndex) {
      return quickselect(numbers, startIndex, lowLastIndex, k);
   }
   return quickselect(numbers, lowLastIndex + 1, endIndex, k);
}