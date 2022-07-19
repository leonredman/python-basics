# numbers

size = 6

def get_numbers(num):
    numbers = []
    user_input = input('Enter %s integers:\n' % num)

    i = 0
    for token in user_input.split():
        number = int(token)     # Convert string input into integer
        numbers.append(number)  # Add to numbers list

        print(i, number)
        i += 1

    return numbers

# Three unfinished functions are defined, which should print only certain types 
# of numbers that the user entered. Complete the unfinished functions, 
# adding loops and branches where necessary. Match the output with the below sample:

def print_all_numbers(numbers):
    # Print numbers
    print('Numbers:', numbers)

def print_odd_numbers(numbers):
    # Print all odd numbers
    odd_nums = numbers
    for odd_num in odd_nums:
        if odd_num % 2 == 0:
          odd_nums.remove(odd_num)
        print('Odd numbers:', odd_nums)

def print_negative_numbers(numbers): 
    # Print all negative numbers
    print('Negative numbers:')

nums = get_numbers(size)
print_all_numbers(nums)
print_odd_numbers(nums)
print_negative_numbers(nums)

# --------------- semi working v1

size = 6

def get_numbers(num):
    numbers = []
    user_input = input('Enter %s integers:\n' % num)

    i = 0
    for token in user_input.split():
        number = int(token)     # Convert string input into integer
        numbers.append(number)  # Add to numbers list

        print(i, number)
        i += 1

    return numbers

def print_all_numbers(numbers):
    # Print numbers
    print('Numbers:', numbers)

def print_odd_numbers(numbers):
    # Print all odd numbers
    for num in numbers:
        if num % 2 == 0:
            numbers.remove(num)
            print('Odd numbers:', numbers)

def print_negative_numbers(numbers):
    # Print all negative numbers
    print('Negative numbers:')

nums = get_numbers(size)
print_all_numbers(nums)
print_odd_numbers(nums)
print_negative_numbers(nums)

# ------

size = 6

def get_numbers(num):
    numbers = []
    user_input = input('Enter %s integers:\n' % num)

    i = 0
    for token in user_input.split():
        number = int(token)     # Convert string input into integer
        numbers.append(number)  # Add to numbers list

        print(i, number)
        i += 1

    return numbers

def print_all_numbers(numbers):
    # Print numbers
    print('Numbers:', numbers)

def print_odd_numbers(numbers):
    # Print all odd numbers
    odd_nums = numbers
    for odd_num in odd_nums:
        if odd_num % 2 == 0:
            odd_nums.remove(odd_num)         
            print('Odd numbers:', odd_nums)

def print_negative_numbers(numbers):
    # Print all negative numbers
    print('Negative numbers:')

nums = get_numbers(size)
print_all_numbers(nums)
print_odd_numbers(nums)
print_negative_numbers(nums)
