Merge(numbers, i, j, k) {
  // Create temporary array mergedNumbers
  // Initialize position variables
  
  // Add smallest element to merged numbers
  while (leftPos <= j && rightPos <= k) {
     if (numbers[leftPos] <= numbers[rightPos]) {
        mergedNumbers[mergePos] = numbers[leftPos] 
        ++leftPos
     }
     else {
        mergedNumbers[mergePos] = numbers[rightPos] 
        ++rightPos
     }
     ++mergePos
  }


  // If left partition not empty, add remaining elements
  while (leftPos <= j) {
    mergedNumbers[mergePos] = numbers[leftPos]
    ++leftPos
    ++mergePos
 }
 
 // If right partition not empty, add remaining elements
 while (rightPos <= k) {
    mergedNumbers[mergePos] = numbers[rightPos]
    ++rightPos
    ++mergePos
 }
 
 // Copy merge number back to numbers
 for (mergePos = 0; mergePos < mergedSize; ++mergePos) {
    numbers[i + mergePos] = mergedNumbers[mergePos]
 }
}
