a = [1,2,3,4,5,6,7,8,9,10]
# even = []
# for num in a:
#     if num % 2 == 0:
#         even.append(num)
       
# print(even)

# even = [x for x in a if x % 2 == 0]   # this is list comprehension
# print(even)

names = ['Ram' , 'shyam', 'rita', 'hari', 'sita', 'ramesh', 'sudip']
name = [name for name in names if name.lower().startswith('r')]
print(name)