for (i = 1; i < numbersSize; ++i) {
  j = i;
  // Insert numbers[i] into sorted part
  // stopping once numbers[i] in correct position
  while (j > 0 && numbers[j] < numbers[j - 1]) {
    // Swap numbers[j] and numbers[j - 1]
    temp = numbers[j];
    numbers[j] = numbers[j - 1];
    numbers[j - 1] = temp;
    --j;
  }
}
