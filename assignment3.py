# task is to write a function that takes a string as a parameter and returns the length of the string and print it

# def name(fn):
#     print(len(fn))

# names = input('enter your name ')
# name(names)


# the main finding of this is that there is no required of = sign while assigning value


# def name(fn):
#     print(len(fn))

# name('hari')


# --------------------------------------------------------------------------------------------

# task a function that takes a string as a parameter and returns the last character of the string

# def name(ln):
#     print(ln[-1])
# name('ram')   simple method 

#asks for the value

# def name(ln):
#     print(ln[-1])
# names = input('Enter a keyword ')
# name(names)


# --------------------------------------------------------------------------------------------


# def vowel(s):
#     vowels = 'aeiou'
#     for char in s:
#         if char.lower() in vowels:
#             return char
#     return None  


# result = vowel("hEllo World")
# print(result)  

#-----------------------------------------------------------------------------------------------


# def vowel(s):
#     vowels = 'aeiou'
#     for char in s:
#         if char.isalpha() and char.lower() not in vowels:
#             return char
#     return None


# result = vowel("hEllo World")
# print(result)  


#-----------------------------------------------------------------------------------------------


# def num(a):
#     a= int(a)
#     if a % 2 == 0:
#         print(True)
#     else:
#         print(False)

# nums= input('enter a number ')
# num(nums)


#-----------------------------------------------------------------------------------------------

# def count_vowels(s):
#     vowels = 'aeiou'
#     count = 0
#     for char in s:
#         if char.lower() in vowels:
#             count = count + 1
#     return count

# result = count_vowels("Hello World")
# print(result)


#-----------------------------------------------------------------------------------------------

# def count_vowels(s):
#     vowels = 'aeiou'
#     count = 0
#     for char in s:
#         if char.lower() not in vowels:
#             count = count + 1
#     return count

# result = count_vowels("Hello World")
# print(result)

#-----------------------------------------------------------------------------------------------


def calculate(s):
    vowels = 'aeiou'
    for char in s:
        if char.lower() == vowels:
            print(True)
        else:
            print(False)

result = calculate('vowelsconsonants')
print(result)
        
