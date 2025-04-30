grades = {'ram' : 85, 'shyam' : 65, 'hari': 55, 'ramesh': 25}
while True:
    name= input('Enter your name ').lower()
    if name in grades:
        grade = grades[name]
        if grade >= 80:
            print(f'Hi {name.capitalize()}. your grade is {grade}. You passed with distinction. ')
        elif grade >= 60:
            print(f'Hi {name.capitalize()}. YOur grade i s{grade}. You passed with first division.')
        elif grade >= 50:
            print(f'Hi {name.capitalize()}. Your grade is {grade}. You passed with second division.')
        else:
            print(f"mom's flying chappal received at {grade}km/hr")
    else:
        print('name not found')
