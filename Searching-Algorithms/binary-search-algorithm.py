# binary search algorithm - python

def binary_search(numbers, key):
  # Variables to hold the low, middle and high indecies
  # of the area being searched. Starts with entire range
  low = 0
  mid = len(numbers) // 2  # floor division drops any decimals and rounds down
  high = len(numbers) - 1

  # Loop until "low" passes "high"
  while (high >= low):
    # calculate the middle index
    mid = (high + low) // 2

    # Cut the range to either the left of right half,
    # unless numbers [mid] is the key
    if (numbers[mid] < key):
      high = mid -1

    else:
      return mid

  return -1 # not found

  '''
  output:
  NUMBERS: [2, 4, 7, 10, 11, 32, 45, 87] 
Enter a value: 10
Found 10 at index 3.
...
NUMBERS: [2, 4, 7, 10, 11, 32, 45, 87]
Enter a value: 17
17 was not found.
  
  '''
