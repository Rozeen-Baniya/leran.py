f = open('abc.txt', 'r')

# reads the whle context of the file
# print(f.read())

# print(f.read(5))
# print(f.read(3))

# print(f.readline())
# print(f.readline())

#reads all the lines in the list
# print(f.readlines())

# for line in f.readlines():
#     print(line.strip())       



# file name milena bhane runtime error hunxa


# try:
#     f = open('abc.txt', 'r')
#     print(f.read())
# except FileNotFoundError:
#     print('file not found')


# f = open('abcd.txt', 'w')
# f = open('abc.txt', 'w')
# f.write('orewa')
# f.write('Hello guys')

# f = open('abc.txt', 'a')

# f.write('\n Hello World.\n I am Rojin')

# f = open('abc.txt' , 'a')

# print(f.closed) # checking if the file is closed or not??

# f.close()

# print(f.closed)

with open('abc.txt' , 'r') as f:
    print(f.read())
    print(f.closed)

print(f.closed)