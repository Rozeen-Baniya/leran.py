name = input('Enter your name: ')
grade = int(input('Enter your grade: '))


if grade >= 80:
    print(f'Hi {name}, your grade is {grade}. You passed with distinction.')
elif grade >= 50 and grade < 80:
    print(f'Hi {name}, your grade is {grade}. You passed with first division.')
else: 
    print(f'Moms flying chappal received at {grade} km/hr!')