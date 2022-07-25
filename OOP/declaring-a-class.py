# Declare a class named PatientData that contains two data members named height_inches and weight_pounds.

class PatientData:
    def __init__(self):
        self.height_inches = 0
        self.weight_pounds = 0

lunaLovegood = PatientData()
print('Patient data (before):', end=' ')
print(lunaLovegood.height_inches, 'in,', end=' ')
print(lunaLovegood.weight_pounds, 'lbs')


lunaLovegood.height_inches = 63
lunaLovegood.weight_pounds = 115

print('Patient data (after):', end=' ')
print(lunaLovegood.height_inches, 'in,', end=' ')
print(lunaLovegood.weight_pounds, 'lbs')

''' Expected output
Patient data (before): 0 in, 0 lbs
Patient data (after): 63 in, 115 lbs
'''