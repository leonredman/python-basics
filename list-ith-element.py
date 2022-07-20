# List 'ith' element
'''
Consider the following program that allows a user to print 
the age of the Nth oldest known person to have ever lived:

Modify the program to print "1st", "2nd", "3rd", "4th" and "5th" 
rather than "1th", "2th", etc., without introducing redundant statements 
(Hint: Precede the below if statement with a separate elif statement that 
determines the appropriate ending based on the number).
'''

oldest_people = [122, 119, 117, 117, 116]  # Source: Wikipedia.org

nth_person = int(input('Enter N (1-5): '))
#insert code
if nth_person == 1:
    tense_let = 'st'

elif nth_person == 2:
    tense_let = 'nd'

elif nth_person == 3:
    tense_let = 'rd'

elif nth_person >=4:
    tense_let = 'th'

if (nth_person >= 1) and (nth_person <= 5):
    print('The %d%s oldest person lived %d years' % \
          (nth_person, tense_let, oldest_people[nth_person-1]))
