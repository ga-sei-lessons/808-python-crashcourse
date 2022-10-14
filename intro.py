# I am a comment -- wil not be executed

# i am a 
# multiline
# comment

'''
I am a docstring
'''

"""
I am also a doc string
"""

# use the builtin print function for output
# print("Hello, Spam!")

# cntrl + d leaves the python3 repl

# python functions start with the 'def' keyword
def greeting(name):
    # this comment is tabbed in to the function scope
    print("hello", name, "how are you liking python?")

# greeting('Gabe')

# python_variables_use_snake_case
# varaible names use snake_case
# function names use snake_case

# define a varaible (no variable declaration keyword)
# my_varaible = 'spam'
# print(my_varaible)
# my_varaible = 'eggs'
# print(my_varaible)
# there is no const, but convention amoung python programmers indicates conts WITH_CAPS
MY_CONST = 'do not change'
# MY_CONST = 'will this work?'

# ## # ## # ## # ## #
# DATA TYPES

# Boolans
None # Nonetype is the abscense of explicit value (Nonetype falsy) -- also used a null
True # truthy value
False # falsy value

# booleans an control flow
has_bank_account = None

# if has_bank_account:
#     print('there is a bank account!')
#     print('i am in the if')
#     # 
#     # more codde
#     # 
# else:
#     print('there is no bank account')

# logical operators (return bools)
# and -- &&
# or -- ||
# not/! -- !

# comparison operators (return bools)
# == -- equality
# != -- not equal
# > < >= <= -- greater than/less than

account_balance = 30

# if has_bank_account and account_balance > 99:
#     print("you\'re rich!")
# #else if uses elif keyword
# elif has_bank_account and account_balance > 50:
#     print('keep saving, one day you will be rich!')
# else:
#     print('you are broke')

# python ternary statements
# [on true] if [boolean expression] else [on false]
should_get_account = 'don\'t open an account' if has_bank_account else 'open an account'
# print(should_get_account)

# ## # ## # ## # ##
# Text Types (strings)
my_string = "double quotes are fine"
my_other_string = 'single quotes are fine'

breakfast = 'spam eggs bacon sausage'
# using dir() to print out all of the instance methods of an instance of an object
# print(dir(breakfast))
# print(breakfast.upper())
# print(breakfast.index('s'))
# # bracket notation using indexes
# print(breakfast[5])
# # negetive values start from the back 
# print(breakfast[-2])
# # 'in' keyword returns a bool (works on all data containers)
# print('spam' in breakfast) 
# if 'spam' in breakfast:
#     print('well I don\'t like spam'.upper())
# # len() find how long a string (works on all data containers)
# print(len(breakfast))
# # string slicing (works on list data containers)
# #           [start index: end index : steps]
# # defaults: [0          : last index: 1]
# # slice out spam
# print(breakfast[0:4:1]) # returns new string of indexes 0 - 5 'spam'
# print(breakfast[:4]) # same us previous line, using default values
# # i don't like spam
# print(breakfast[4:]) # remove spam, keep the rest of the string
# print(breakfast[::3]) # keep everything and skip every other
# # negetive step, iterates in reverse
# print(breakfast[::-1]) # reversal trick

# ## # ## # ## # ## #
# Numeric datatypes

# integers -- whole numbers
my_int = 10
# floats are decimals
my_float = 2.17823
# print(type(my_int), type(my_float), type(breakfast))
# # int plus float
# print(10 + 10.0) # integers are coerced into floats
# # no type coersion between strings and number types
# print(int('10') + 10) # using classes for type conversion

# int # integer class
# float # floating point class
# str # string class 

# # complex number
# my_complex = 3j
# print(my_complex + 10j + 10)

# # math operators
# # + - / * % -- arithmitic
# # there is no ++ -- 
# # += -= /= *= %= **= 
# # number ** to the power of -- exponent operator
# # // forced integer division (rounds down) -- Math.floor(10 / 3.3)
# my_int += 33.6
# print(my_int)
# print(2 ** 8)
# print(10 // 3.3)

# ## # ## # ## #
# Scope in python

# global scope
my_value = 10

# adds 5 to my value
def add_five():
    # global keyword to refer to a varaible from the scope above
    global my_value
    my_value += 5
    print(f'my_value inside of add_five: {my_value}')
    # pass # tells python to skips this indentation scope

# prints out my_value
def print_val():
    # string interpolation in python
    # format string
    print(f'my_val: {my_value}')

# add_five()
# print_val()

# ## # ## # ## #
# DATA CONTAINERS

# lists -- numerically indexed container (aka arrays)
my_list = ['spam', 'eggs', 'sausage', 'bacon']
# dictionaries -- key/value pairs {}
my_dictionary = {
    # named keys need to be strings in quotes
    'spam': 'eggs',
    'fruit': 'banana',
    # any datatype can be a key
    10: '35',
    True: 'wtffffffff'
}
# # tuples -- indexed lists that cannot change
# my_tuple = ( 'cannot', 'change', 'same value twice', 'same value twice' )
# # Sets -- unindexed collections that cannot have the same value twice and cannot change
# my_set = { 'cannot', 'change', 'must be unique' }

# looping and working with lists
# can use numbers to acces indexes, and slice notation
# print(my_list[0])
# print(my_list[1:])
# my_list[1] = 'spam'
# print(my_list)
# print(dir(my_list))
# my_list.append('spam') # places on the end of a list
# print(my_list)
# my_list.insert(0, 'spam')
# print('spam' in my_list)

# # looping
# for item in my_list:
#     print(item)

# for i, item in enumerate(my_list):
#     print(f'{i}: {item}')

# # ranges
# print(range(10))
# # 'traditional for loop'
# for i in range(len(my_list)):
#     print(f'{i}: {my_list[i]}')

# # while loops
# i = 0
# while i < len(my_list):
#     print(my_list[i])
#     # breaking a loop
#     if my_list[i] == 'sausage':
#         break
    
#     i += 1
# # looping dictionary
# for key in my_dictionary:
#     print(f'{key}: {my_dictionary[key]}')

# cannot use dot noation on dictionarys to access keys -- only to invoke instance methods
print(my_dictionary['spam'])
print(my_dictionary[True])
# set or add a value, use equality
my_dictionary['new_value'] = 'taco'
print(my_dictionary)
my_dictionary.pop('new_value') # removes new value
print(my_dictionary)
if 'new_value' in my_dictionary:
    # my_dictionary.pop('new_value')
    del my_dictionary['new_value'] # also works