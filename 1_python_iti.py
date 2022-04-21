#!/usr/bin/python3.8
'''
Learn:
    - how print statments 
    - how make comment and multi line comment
    - data type in python and TypeConvention
    - multi line assignment 
'''

# print in python 
# use ' ' or " " for single line prints 
# but  ''' ''' for line line statemnt print or """ """
print('Hello World !')
print('محمد اشرف ')
print("Hello World  By Muhammed ashraf ")
print('''Hello World 's Muhammed ashraf 
fffffffffffffffffffffffffffffffffffffffffffffffffff''')
# if use 's in world use " " or ''' ''' or use back slash \
print('this is Muhammed \'s book ')

# comment in python use # for singel line comment
'''
this is multi line comment but this is value of string but not assign to variable
this use for multi line comment
'''

# DatType in Python and TypeConvention  
''' 
int() for Integer
float() for Float and double 
str() for string
bool() for Boolean has value True of False
dict() for Dictionary data structure
list() for List data structure
tuple for Tuple data structure
NoneType as Null in Other PL use None as x=None
'''
# in python we do not declare variable 
# but when give value we can knew the datatype for variable
# variable_name(identifier) = value
# rules for writing identifier of variable
'''
Starts only with: a-z or A-Z or _
Can’t Contain : Punctuations Characters
Can Contain: digits but not in start 
A Python identifier doesn’t be one of reserved word
''' 
a_int=10
b_float=12.5
s_str="Muhammed ashraf"
p_bool=True
x=None
# to know data type of variable use type(varaible_name)
# this method of print with variable with use format 
print('a_int type is %s and b_float type is %s'%(type(a_int),type(b_float)))
print('s_str type is {0} and p_bool type is {1}'.format(type(s_str),type(p_bool)))
print(f'x type is {type(x)}')
"""
we can camel case like this 
isStudent=True
but in python use synake syntax
is_stuent=True
"""

#multi line assignment 
a,b,c,p=10,256.3,"Muhammed Ahsraf",False
# swap in python using multi line assignment
a_swap,b_swap=10,56
print("a_swap = ",a_swap," b_swap= ",b_swap) 
a_swap,b_swap=b_swap,a_swap
print("a_swap = ",a_swap," b_swap= ",b_swap) 