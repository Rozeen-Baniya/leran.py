# write a finction that takes a strintg as a parameter and retutns the length of the string and print it

# write a function that takes a string as a parameter and returns thee last character of the String 

# write a function that takess a string as a parameter and returns the first vowel present in the String 

# Write a function that takes the parameteer as a string and returns the first consonant present in the String 

# def find_str_length(s):
#     return len(s)\
    
# name = input('enter a name ')
# print(f"the length of {name} is { find_str_length(name)}")


# def find_last_char(s):
#     return s[-1]

# print(f"teh length of {name} is {find_last_char(name)}")

# def find_first_vowel(s):
#     for item in s:
#         if item in 'aeiouAEIOU':
#             return item
        
# find_first_vowel('ramesh')


# def find_first_consonant(s):
#     for item in s:
#         if item not in 'aeiouAEIOU':
#             return item
        
# print(find_first_consonant('RAMesh'))


# def is_even(n):
    # if n % 2 == 0:
    #     return True
    # else:
    #     return False

    # return True if n % 2 == 0 else False

    # return n % 2 == 0



# def count_vowels(s):
#     count = 0
#     for item in s:
#         if item in 'aeiouAEIOU':
#             count = count + 1
#     return count

# print(count_vowels('ramesh'))

# def count_consonants(s):
#     count = 0
#     for item in s:
#         if item not in  'aeiouAEIOU' and item.isalpha():
#             count = count + 1
#     return count

# print(count_consonants('ramesh maharjan'))


def is_vowel_present(s):
    for item in s:
        if item in 'aeiouAEIOU':
            return True
    return False

print(is_vowel_present('ramesh maharjan'))