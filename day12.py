# logical error

# while True:
#     a = int(input('enter first number'))
#     b = int(input('enter second number'))
#     print(f'{a} divided by {b} is {a/b}')

#runtime error/ exceptions

# try:
#     risky code: code thet  throw errors

# except:
#     alternative code 
#     code to run when error occurs
#else:
#     runs when there is no error 
# finally: 
#     run every time


while True:
    try:
        a = int(input('entere a number '))
        b = int(input('enter second number '))
        print(f'{a} divided by {b} is {a/b}')
    except ZeroDivisionError:
        print('second input cannot be zero')
    except ValueError:
        print('inputs must be numbers ')
    except Exception as e:
        print(type(e))
    finally:
        print('please visit us again')


