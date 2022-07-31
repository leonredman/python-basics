# insertion sort - python

def insertion_sort(num_list):
  for i in range(1, len(num_list)):
    j = 1

    # Insert num_list[i] into sorted part
    # stopping once num_list[i] in correct position
    while j > 0 and num_list[j] < num_list[j-1]:
      # swap num_list[j] and num_list[j-1]
      temp = num_list[j]
      num_list[j] = num_list[j-1]
      num_list[j-1] = temp
      j -= 1

# Create a list of unsorted values
numbers = [10, 2, 78, 4, 45, 32, 7, 11]

# Print unsorted list
print('UNSORTED:', numbers)

# Initial call to insertion_sort with index
insertion_sort(numbers)

#Print sorted list
print('SORTED:', numbers)

'''
Output
UNSORTED: [10, 2, 78, 4, 45, 32, 7, 11]
SORTED: [2, 4, 7, 10, 11, 32, 45, 78]
'''