# modify copy of list with slice notation
nums1 = []
nums2 = []

user_input = input('Enter first set of numbers: ')
tokens = user_input.split()  # Split into separate strings

# Convert strings to integers
for pos, val in enumerate(tokens):
    nums1.append(int(val))
    print('%d: %s' % (pos, val))

user_input = input('Enter second set of numbers:')
tokens = user_input.split()

# Convert strings to integers
print()
for pos, val in enumerate(tokens):
    nums2.append(int(val))
    print('%d: %s' % (pos, val))
    
# Remove elements from nums1 if also in nums2
print()
for val in nums1[:]:  # slice notation -iterate thru copy
    if val in nums2:
        print('Deleting %d' % val)
        nums1.remove(val)

# Print new numbers
print('\nNumbers only in first set:', end=' ')
for num in nums1:
    print(num, end=' ')

'''
enter numbers:
5 10 15 20 25
2 4 6 10 21 15

result:
Enter first set of numbers: 0: 5
1: 10
2: 15
3: 20
4: 25
Enter second set of numbers:
0: 2
1: 4
2: 6
3: 10
4: 21
5: 15

Deleting 10
Deleting 15

Numbers only in first set: 5 20 25 

'''