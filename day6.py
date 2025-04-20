# a = ()
# b = tuple() #empty tuple
# days = ('sun', 'mon', 'tue', 'wed', 'thu')

# heterogeneous
# a = (1, True, 'ram')

# indexed/ ordered
# days = ('sun', 'mon', 'tue', 'wed', 'thu')
# print(days(-1))

#immutable
# print(len(days))

# print('sun' in days)
# print('Sun' .lower() in days)

# tuple with one element

# a = ()
# print(type(a))

# b = (1, 2)
# print(type(b))

# c = (1,)
# print(type(c))

# d = ('ram',)
# print(type(d))

# days = ('sun', 'mon', 'tue', 'wed', 'thu')
# del days

# tuple1 = ('a', 'b', 'c')
# tuple = (1, 2, 3)

# tuple3 = tuple1 + tuple
# print(tuple3)

# i,j,k = (1,2,3)
# print(i,j,k) 



# a = set()

# b = {1, 2, 3, 4, 5}

# Heterogeneous
# mutable
# doesnot allow duplicates
# not indexed
# a = { 'ram', 1, 1.1}
# print(a)

# b = {1,1,2,2,3,3,4,4,4,5,5,5,5,5,6,6,7}
# print(b)
# print(len(b))

# c = {'ram', 'shyam', 'hari'}
# print(c)
# print('banana' in c)

# c = {'ram', 'shyam', 'hari'}
# c.add('sita')
# print(c)
# thisset = {'apple', 'banana', 'cherry'}

# thisset.remove('banana')
# thisset.discard('bananananana')
# print(thisset)

# set1 = {'a', 'b', 'c', 1, 2}
# set2 = {1, 2, 3, 'a'}
# set3 = set1.union(set2)
# print(set3)

# set4 = set1.intersection(set2)
# print(set4)


# collection fo key values pairs

# a = {}
# b = dict()

# students_grades = {'ram': 20, 'hari': 24, 'sita': 40}
# print(students_grades)

# info = {'name': 'ram', 'age': 20, 'salary' :2-00000, 'is_married': False}

# Heterogeneous
# mutable
# keys should be unique
# students_grades = {'ram': 20, 'shyam': 30, 'hari' : 30}
# del students_grades['ram']
# print(students_grades)

# students_grades = {'ram': 20, 'shyam': 30, 'hari' : 30}
# students_grades['ram'] = 100
# print(students_grades)

# students_grades = {'ram': 20, 'shyam':25, 'hari': 30}
# students_grades['sita'] = 100
# print(students_grades)

# students_grades = {'ram': 20, 'shyam':25, 'hari': 30}
# print(students_grades.get('rama'))
# print(students_grades.keys())
# print(students_grades.values())
# print(students_grades)
# students_grades.clear()
# print(students_grades)

# thisdicti = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1994
# }

# mydict = thisdict.copy()
# print(mydict)

info = {'name': 'ram', 'age': 30, 'address': 'kathmandu'}
print(info['name'])
print(info['address']['city'])
print(info['address']['district'])

info['address']['city'] = 'maitidevi'