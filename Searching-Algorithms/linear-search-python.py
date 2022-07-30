# linear-search-python
def linear_search(numbers, key):
  for i in range(len(numbers)):
    if (numbers[i] == key):
      return i
  return -1  # if not found

# Main program to test the linear_search() method
numbers = [2, 4, 7, 10, 11, 32, 45, 87]
print('NUMBERS:', numbers)

key = int(input('Enter an integer value: '))
key_index = linear_search(numbers, key)

if (key_index == -1):
  print('%d was not found.' % key)
else:
  print('Found %d at index %d.' % (key, key_index))


  '''
  Output:
  NUMBERS: [2, 4, 7, 10, 11, 32, 45, 87] 
Enter an integer value: 10
Found 10 at index 3.
...
NUMBERS: [2, 4, 7, 10, 11, 32, 45, 87]  
Enter an integer value: 17
17 was not found.
  '''