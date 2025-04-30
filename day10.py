# fuctions

# functionn is a collection of statements that together peforms a specific task

# most use : It creates reusable logics

# def add():
#     print( 1 + 1)

# add() # function execution/ call
# print('hello world')
# print('hey')
# add()
# print('Today is mothers day')
# add()


# def add(i, j):
#     print(i+j) #paramerters

# add(2,2) #arguments also called positional arguments


#positional arguments
# def info(fn, ln, age)
#     print(f'Hi {fn} {ln}. YOur age is {age}')
# info('hari', 'ram', 23)

#disadvantage of positional arguments
# def info(fn, ln, age)
#     print(f'Hi {fn} {ln}. YOur age is {age}')
# info('hari', 23 , 'ram')

# keyword argument
# def info(fn, ln, age)
#     print(f'Hi {fn} {ln}. YOur age is {age}')
# info(age=28, ln='hari', fn='ram')

#default argument
# def info(fn, ln, age, balance=0):
#     print(f'Hi {fn} {ln}. YOur age is {age}')
#     print(f'your balance is {balance}')
# info(age=28, ln='hari', fn='ram')
# info(age= 40, ln= 'hariram' , fn='shree', balance=900)

# def info(fn, ln, age):
#     print(f'Hi {fn} {ln}. YOur age is {age}')

# info('ram', age=28, ln='hari')


# def add(*args):
#     print( sum(args))


# add()
# add(1)
# add(1,2)
# add(1,2,3)
# add(1,2,3,4)

# variable/ multiple length argument
    # it accepts any number of arguments

# variable length postitional arguments' order matter garney bhayo
    #represented by *args
    #stores the value in tuple

# def info(**kwargs):
#     print(kwargs)

# info()
# info(fn="ram")
# info(ln="hari", fn="shyam")


# variablel/ multiple length arguments
    #it accpts any number of arguments

# varibale length keyword argument


# def add(i,j):
#     return i+j
# a = add(2,4)
# print(a)



# def add(i,j,k):
#     return i+j+k

# def mean(i,j,k):
#     sum = add(i,j,k)
#     return sum/3

# print(mean(2,3,4))



# def info():
#     return 'ram', 'shyam'
#     print('hey')

# print(info())

# def add():
#     print(1+1)
#     print('hey')

# print(add())