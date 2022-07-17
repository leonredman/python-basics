# Convert height in Feet/inches to centimeters

cm_per_inch = 2.54
inches_per_foot = 12

def height_US_to_cm(feet, inches):
    """Converts height in feet/inches to centimeters"""
    total_inches = feet * inches_per_foot + inches
    cm = total_inches * cm_per_inch
    return cm

feet = int(input('Enter feet: '))
inches = int(input('Enter inches: '))

print('Centimeters:', height_US_to_cm(feet, inches))

''' yeild
Enter feet: 5
Enter inches: 8
Centimeters: 172.720000
'''
