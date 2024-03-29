#!/usr/bin/python3.8
'''
Learn:
    - what is shebang line
    - how print statements
    - how make comment and multi line comment
    - data type in python and TypeConvention
    - multi line assignment
'''
"""
In many .py files we may see the shebang line on the top of the script.
Its purpose is to define the location of the interpreter. 
By adding the line #!/usr/bin/python3 on the top of the script,
we can run the file.py on a Unix system and automatically will understand that this is a python script.
Alternative, you could run the script as python3 file.py.
"""
# print in python 
# use ' ' or " " for single line prints 
# but  ''' ''' for line line statemnt print or """ """
print('Hello World !')
print('محمد اشرف ')
print("Hello World  By Muhammed ashraf ")
print('''Hello World 's Muhammed ashraf 
fffffffffffffffffffffffffffffffffffffffffffffffffff''')
# if use 's in world use " " or ''' ''' or use back slash \ is a escape character in python
print('this is Muhammed \'s book ')

# commenting in python use #(sharp) for a single line comment
'''
this is multi line comment but this is value of string but not assign to variable
this use for multi line comment
'''

# DataType in Python and TypeConvention  
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
# but when give value, interpreter can recognize it(datatype for variable)
# variable_name(identifier) = value
# rules for writing identifier of variable
'''
Starts only with: a-z or A-Z or _
Can't Contain : Punctuations Characters
Can Contain: digits but not in start 
A Python identifier doesn't be one of reserved word
''' 
a_int=10
b_float=12.5
s_str="Muhammed ashraf"
p_bool=True
x=None
# to know data type of variable use type(varaible_name)
# this method of print with variable with use format 
# % s -> str, d -> int , f -> float, s or d(1,0) -> bool
print('a_int type is %s and b_float type is %s'%(type(a_int),type(b_float)))
print('a_int type is %d and b_float type is %f, bool %s'%(a_int,b_float, p_bool))
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
print("a_swap = ",a_swap," b_swap= ",b_swap) 