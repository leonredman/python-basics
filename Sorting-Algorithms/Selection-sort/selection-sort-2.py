def selection_sort(numbers):
   # A variable to hold the number of item comparisons
   comparisons = 0

   for i in range(len(numbers)-1):
          
      # Find index of smallest remaining element
      index_smallest = i
      for j in range(i+1, len(numbers)):
      
         comparisons = comparisons + 1
         if numbers[j] < numbers[index_smallest]:
            index_smallest = j
      
      # Swap numbers[i] and numbers[index_smallest]
      temp = numbers[i]
      numbers[i] = numbers[index_smallest]
      numbers[index_smallest] = temp
          
   return comparisons


# Main program to test the selection sort algorithm
numbers = [10, 2, 78, 4, 45, 32, 7, 11]

# Display the contents of the list
print('UNSORTED:', numbers)

# Call the selection_sort() function
comparisons = selection_sort(numbers)

# Display the (sorted) contents of the list
print('SORTED:', numbers)

print('Total comparisons: %d' % comparisons)

'''
Output
UNSORTED: [10, 2, 78, 4, 45, 32, 7, 11]
SORTED: [2, 4, 7, 10, 11, 32, 45, 78]
Total comparisons: 28
'''