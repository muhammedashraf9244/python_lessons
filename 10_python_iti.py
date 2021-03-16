'''
Learn:
    - Modules & package how use 
    - OS Module
    - Random Module
    - Sys Module
    - termcolor & pyfiglet
'''

''' 
Consider a module a file containing a set of functions you want to include in your application.
'''
"""
Create Module create file with name mymodule.py
to use this module use import 

mymodule contain function or varaibles or class to import all from mymodule without use 
mymodule.any_thing use 
from mymodule import *

to name function or varaible with anthor name to use in code use as (ailias name)
from mymodule import var as myvar
"""
# "python.autoComplete.extraPaths":["/media/muhammed/New Volume/computer science/ITI_3_Python/python"]
import mymodule
from  mymodule import print_name as print_my_name
from mymodule import list_name as persons_name
print_my_name("Mohammed")
print(persons_name)

'''
To know all functions or variables in any module
'''
print(dir(mymodule))
print("S"*5)
'''
Packages is list of modules in directory 
but in python2 package can declaration with create file in package name __init__.py (dander file)
'''
'''
OS Module is module for handel with your operating system
for use import os
Methods in os 
getcwd() Return the current working directory for python interpreter your files
os.path.abspath(__file__) Return an absolute path of your script in your os
os.path.dirname(path_file) Returns the directory component of a pathname
os.chdir(dir) Change the current working directory to the specified path.
'''
import os
print(f' Current dir => {os.getcwd()}')
print(f' absolute path of your script => {os.path.abspath(__file__)}')
print(f' path of your directory of your script  {os.path.dirname(os.path.abspath(__file__))}')

#** if current directory is not same directory of your script in open file will be found error
#** for solve it it change current directory to same directory of your script 
# change current directoy of your system to directory of your script 
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.getcwd())

'''
golobale variable is a variable which python interpreter define it 
__file__ is variable store name of file 
print(__file__)
'''

"""
Random module is a module have mamny function for random number 
random() generate float point number form 0 to 1
randint(a,b) Return random integer in range [a, b], including both end points.
"""
from random import random , randint 
from math import ceil , floor
print(f"Random float point number { round(random()*100)}")
print(f"Random interger number {randint(5,10)} ")

"""
sys This module provides access to some objects used or maintained 
by the interpreter and to functions that interact strongly with the interpreter.
"""
import sys 
# use sys.path return list of path in our system may be add any path
print(sys.path)
sys.path.append("/media/muhammed/New Volume/computer science/ITI_3_Python/python/")
print(sys.path)

print('*'*50)
# termcolor & pyfiglet
import termcolor
import pyfiglet
# pyfiglet library for draw text 
# termcolor change color of text on terminal

print(termcolor.colored(pyfiglet.figlet_format("Muahmmed"),color="blue"))
