# inheritance - inherit the characters from parent class by child class 
    #advantage - resuable code
# abstraction
    # Some process is going on but we are unknown about how it process
# polymorphism
# encapsulation
    # the process of grouping together properties and methods of a class in a single class is called incapsulation
    # the debugging process becomes easy


# class FullTimeEmployee:
#     def __init__(self,fn, ln, age ):
#         self.first_name = fn 
#         self.last_name = ln 
#         self.age = age

# class PartTimeEmployee:
#     def __init__(self, fn, ln, age):
#         self.first_name = fn 
#         self.last_name = ln 
#         self.age = age 

class Employee:
    def __init__(self, fn, ln, age):
        self.first_name = fn 
        self.last_name = ln 
        self.age = age

class FullTimeEmployee(Employee):
    pass

class PartTimeEmployee(Employee):
    pass

f = FullTimeEmployee('Rojin', 'Baniya' , 20)
print(f.first_name )
print(f.last_name)