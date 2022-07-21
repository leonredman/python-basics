# User inputs string w/ numbers: '203 12 5 800 -10'
user_input = input('Enter numbers: ')

tokens = user_input.split()  # Split into separate strings

# Convert strings to integers
print()
nums = []
for pos, token in enumerate(tokens):
    nums.append(int(token))
    print('%d: %s' % (pos, token))

sum = 0
for num in nums:
    sum += num

print('Sum:', sum)

'''
Enter numbers: 203 12 5 800 -10
0: 203
1: 12
2: 5
3: 800
4: -10
Sum: 1010
'''