# while-loop
nose = '0'  # Looks a little like a nose
user_value = '-'

while user_value != 'q':
    print(' %s %s ' % (user_value, user_value))  # Print eyes
    print('  %s  ' % nose)  # Print nose
    print(user_value*5)  # Print mouth
    print('\n')

    # Get new character for eyes and mouth
    user_input = input("Enter a character ('q' for quit): ")
    user_value = user_input[0]

print('Goodbye.\n')