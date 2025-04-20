# list set tuple dictionary

# a = [] #empty list
# b= list() # list

# print(type(a))
# print(type(b)) 

#list nonempty

#proprties 

#heterogeneus

# a = [1, 1.1, True, 'ram']

# #list is indexed/ ordered
# print(a[0])

# #mutable/ changable (values can be added, removed, updated)

# #allow duplicates

# a = [1,2,2,2,2,4,4,4,3]
# print(a)

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # print(a[-1])

# # print(a[::2])
# # print(len(a))

# print(1 in a)

# a = [1,2, 3, 4, 5, 6, 7, 8, 9]

# del a[0]

# a[0]= 100
# del a [0]
# print(a)

names = ['ram', 'shyam', 'hari']

# names.append('rita')
# names.append('sita')


# print(names)
# print(len(names))

# names.insert(1, 'ramesh')

# print(names)

thislist = ['apple', 'banana', 'cheery']
tropical = ['mango', 'pineapple', 'papaya']

thislist.extend(tropical)
print(thislist)

new_lsit = thislist + tropical
print(new_lsit)

# # remove --removes value wise

# thislist.remove('apple')
# print(thislist)
# print(len(thislist))
# thislist.pop(2)      # remove garney
# empty pop xa bhene pachadi bata remove garxa
# thislist.clear()
# print(thislist)

# thislist = ['banana', 'apple', 'guava', 'pineapple']
# thislist.sort()
# thislist.reverse() #step wise


# thislist.sort(reverse= True) # one line
# print(thislist) 

# a= thislist.copy()
# a[0] = 'ramesh'
# print(a)
# print(thislist)