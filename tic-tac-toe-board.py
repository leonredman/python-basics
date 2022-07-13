# tic tac toe board

'''
Complete the print_tic_tac_toe function with parameters horiz_char and vert_char that prints a tic-tac-toe board with the characters as follows.
def print_tic_tac_toe(horiz_char, vert_char):
    # FIXME: complete function to print game board
    return
Ex: print_tic_tac_toe('~', '!') prints:
x ! x ! x
~ ~ ~ ~ ~
x ! x ! x
~ ~ ~ ~ ~
x ! x ! x
'''

def print_tic_tac_toe(horiz_char, vert_char):
    print('x', vert_char, 'x', vert_char, 'x')
    print(horiz_char,horiz_char,horiz_char,horiz_char,horiz_char)
    print('x', vert_char, 'x', vert_char, 'x')
    print(horiz_char,horiz_char,horiz_char,horiz_char,horiz_char)  
    print('x', vert_char, 'x', vert_char, 'x')
    return

print_tic_tac_toe('~', '!')