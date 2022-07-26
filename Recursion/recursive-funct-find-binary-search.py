# A recursive function find() carrying out a binary search algorithm.

def find(low, high):
    mid = (high + low) // 2  # Midpoint of low..high
    answer  = input('Is it %d? (l/h/y): ' % mid)

    if (answer != 'l') and (answer != 'h'):  # Base case
        print('Got it!')
    else:
        if answer == 'l':
            find(low, mid)
        else:
            find(mid+1, high)

print('Choose a number from 0 to 100.')
print('Answer with:')
print('   l (your num is lower)')
print('   h (your num is higher)')
print(' any other key (guess is right).')

find(0, 100)

'''
 output:
Choose a number from 0 to 100.
Answer with:
   l (your num is lower)
   h (your num is higher)
 any other key (guess is right).
Is it 50? (l/h/y): l
Is it 25? (l/h/y): h
Is it 38? (l/h/y): h
Is it 44? (l/h/y): l
Is it 41? (l/h/y): y
Got it!
'''