#OOp

# dry principle--- do not repeat yourself

# i = 0  
# while i < 5: # this is while loop 
#     print('hello world')
#     i = i + 1
# print('this is the end')

# i = 0
# while i < 5:
#     print('Hello world')
#     i = i + 1 
#     break
#     print('this is afte break')
# print('I am end')

# i = 0
# while i < 5:
#     print('Hello world')
#     i = i + 1 
#     continue # mathi ko matra continue garney
#     print('this is afte break')
# print('I am end')


# names = ['ram' , 'sita', 'hari', 'shyam']

# i = 0
# while i < len(names):
#     print(f'hi {names[i].capitalize()}')
#     i = i + 1

# num = input("enter a number ")
# i = 2

# while i <= num:
#     print(i)
#     i = i + 2

# for variable_name in iterables:
# statements


# string list set tuple dictionary range

# print( list (range(10)))
# print( list (range(2:10)))
# print( list (range(2:10:2)))

# ffor i in 'umesh';
# print(i)

# for item in ['ram', 'hari', 'shyam', 'sita']:
#     print(item)

# string list set tuple dictionary range

# grades = {'ram': 20, 'hari':40, 'sita':25}

# for item in grades:
#     print(item)

# for item in grades.keys():
#     print(item)

# for item in grades.values():
#     print(item)

#string list set tuple dictionary range

# grades = { 'ram':20 , 'shyam':30 , 'hari': 80}

# print(grades.items())
# for k, v in grades.items():
#     print(k, v)

# for num in range(10):
#     print(num)

# k, v = ('ram', 20)

# for num in range(10):
#     if num % 2 == 0:
#         print(num)
#     else:
#         continue
#         print("hi")


# ram 85
# shyam 62
# hari 55

# neter your name ram Ram rAM Ram ram 

# >= 80 Hi ram your grade is .... you passed with distinction
# >= 60 and < 80 Hi your grade is ... you passed with first division 
# < 50 mom's flying chapppal receive dat 15km/hr

name = input('Enter your name: ')
grade = int(input('Enter your grade: '))

if grade >= 80:
    print(f'Hi {name}, your grade is {grade}. You passed with distinction.')
elif grade >= 50 and grade < 80:
    print(f'Hi {name}, your grade is {grade}. You passed with first division.')
else: 
    print(f'Mom’s flying chappal received at {grade} km/hr!')
