# self points to the currently running object in the memory
# self should be the first parameter of init 


# class student:
#     def __init__(self, fn, ln, add):
#         self.first_name = fn
#         self.last_name = ln
#         self.address = add

# s = student('ram', 'hari', 'sanepa')
# a = student('sree', 'shyam', 'banepa')

# #access object variables outside the class
# print(s.first_name, s.last_name, s.address)
# print(a.first_name, a.last_name, a.address)

# change object variables outside the class
# s.first_name = 'ramayan'
# s.last_name = 'shree'


# del s.first_name
# print(s.first_name)



class student:
    school_name = 'sunway'
    school_address = 'maitidevi'
    def __init__(self, fn, ln, add):
        self.first_name = fn
        self.last_name = ln
        self.address = add
        print(student.school_address)

s = student('ram', 'hari', 'sanepa')
a = student('sree', 'shyam', 'banepa')

#access object variables outside the class
print(s.first_name, s.last_name, s.address)
print(a.first_name, a.last_name, a.address)

print(student.school_name, student.school_address)


# type of variables 
    #instance variables
        # variables whose values depends upon object 
        # object level variable
        # accessed by using self inside the class and by using object name outside the class
        # copy of instance variable is created for every object

    #static variables
        # variables whose values depends on class
        # class - level variables
        # acessed by using class name both inside and outsid the class
        # copy of static variable is created once when the class is declared


# types of method getter ra setattr
