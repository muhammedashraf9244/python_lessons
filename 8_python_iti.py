"""
Learn:
    - Packing & Unpacking
    - Function in python
    - *args & **kwargs
    - Recursive function in python
"""

"""
Packing & Unpacking 
Unpacking & Unpacking  List & Tuple use * 
Unpacking & Unpacking Dictionary use **

packing means group some elemnts in one location
unpacking means ungroup some elements 
"""
# Multi line assignment 
# packing
x,y,*var=1,2,3,6,8,9
print(f"x {x} {type(x)}")
print(f"y {y} {type(y)}")
print(f"x {var} {type(var)}")

# unpakcing use with *args and **kwargs in function
list_l=[1,2,6,.3,55]
tuple_l=("Ahmed","Mohamed","Ali")
dic_student={'name':"Muhammed","grade":75}
unpacking_dic={**dic_student}
'''
# do use this format for unpacking list & tuple
print(f"Unpacking list {*list_l})
print(f"Unpacking typle {*tuple_l}")
'''
print("Unpacking list", *list_l)
print("Unpacking typle", *tuple_l)
print(f"Unpacking Dic {unpacking_dic}")

'''
Function use DRY means Don't repeate your code
function consists of 
1- Function declaration 
   function may be have arguments or return data type
    def func_name(arguments):
        # block_of_code
2- call this function
    func_name(parmeter)

Defalut value in function means we can assignment argument defalut value
Important but perfable defalut value is the last argument 
'''

def cal_slary(salary,salary_rais=50):
    tax=20/100*salary +salary_rais
    return tax and tax/2
    # if tax: return tax/2

salary=2000
my_tax=cal_slary(salary)
print("tax without raise salary ",my_tax)

my_tax=cal_slary(salary,100)
print("tax with raise salary ",my_tax)

'''
*args and **keyargs
*args means zero or more use if i call function with many parameters called positional parameters
**kwargs means zero or more use if call function with many parameters with name called named aragument 
*args is tuple of data
**kwargs is dictionary of data
'''
# without positional parameters
def mysum(x,y,o,p):
    return x+y+o+p

print(mysum(1,2,3,4))

# with use args (Positional Parameter)
'''
Very Important if call function with *args 
no any parameters after *args except **kwargs
def mysum_positional(x,y,*args) # ok
def mysum_positional(x,*args,y) # error
'''
def mysum_positional(x,y,*args):
    the_sum=0
    for i in range(len(args)):
        the_sum+=args[i]
    return the_sum+x+y
print('Positional ',mysum_positional(1,2,3,5,6,8))

# with **kwargs (Named Parameter) 
"""
Very Important if call function with **kwargs 
no any parameters after **kwargs
def mysum_named(x,y,**kwargs) # ok
def mysum_named(**kwargs,x,y) # error
"""
def mysum_named(x,y,*args,**kwargs):
    the_sum=0
    for k,v in kwargs.items():
        # print(f'{k} {v}')
        the_sum+=kwargs.get(k)
    for i in range(len(args)):
        the_sum+=args[i]    
    return the_sum+x+y
dic_l={'c':20,"s":6,'o':8}    
print('Named ',mysum_named(1,2,10,20,**dic_l))


"""
Function Recursion
is a function which call itself 
There are two main parts to recursive functions:
general (recursive) case--the case for which the solution is expressed in terms of a smaller version of itself.
In other words, here, the problem space is made smaller and smaller. (the smaller problem space is sent to the calling function)
base case--the case for which the solution can be stated nonrecursively.
Here, a solid solution is found.
Example Factorial, Power,....
facorial(n)=n * !(n-1)  # !(n-1) general case 
factorial(n-1)=(n-1) * !(n-2) # !(n-2) general case
 .......
 ......
 facorial(0) or facorial(1) = 1 # base case
 interperter return base case for solve factorial  
"""

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return  n * factorial(n-1) 

print(f"Factorial 5 = {factorial(5)}")
"""
# genral base digging 
factorial(5) = 5 * factorial(4)
factorial(4) = 4 * factorial(3)
factorial(3)= 3 * factorial(2)
factorial(2) = 2 * factorial(1)
factorial(1) = 1 * factorial(0)
factorial(0) = 1  # base case 
# find solution of base case
factorial(1) = 1 * 1
factorial(2) =  222 * 1
factorial(3) = 3 * 2
factorial(4) = 4 * 6
factorial(5) = 5 * 24  # finish return the last recursive 
"""
"""
Problem
  delete unoccurrences sequence letter in word 
input : wwworrlefd
output : worlefd
"""
# My solution 
def unoccurr_word(word):
    if len(word) == 1 : return word
    if word[0] == word[1]: return unoccurr_word(word[1:])
    return word[0] + unoccurr_word(word[1:])

print(f' wweoolodw => {unoccurr_word("wweoolodw")}')

"""
Try recursive function 
unoccurr_word(word):
    if len(word) == 1 : return word
    if word[0] == word[1] return unoccurr_word(word[1:])
    return word[0] + unoccurr_word[1:]

unoccurr_word(wweoold) => weold
unoccurr_word(wweoold) => unoccurr_word(weoold)
unoccurr_word(weoold) => w + unoccurr_word(eoold) 
unoccurr_word(eoold) => e + unoccurr_word(oold)
unoccurr_word(oold) => unoccurr_word(old)
unoccurr_word(old) => o + unoccurr_word(ld)
unoccurr_word(ld) => l + unoccurr_word(d)
unoccurr_word(d) => d 
# find the last recursive
unoccurr_word(ld) => l + d = 'ld'
unoccurr_word(old) => o + 'ld' = 'old'
unoccurr_word(oold) => 'old'
unoccurr_word(eoold) => e + 'old' = 'eold'  
unoccurr_word(weoold) => w + 'eold' = 'weold'
unoccurr_word(wweoold) => 'weold'
"""

'''
Lambda Funtion is samll function or anonymous function 
- It has no name
- you can call it without defining it 
- Lambda function is sample function not decalaration with def
- Lambda is one single expression
- Lambda type is function  
Formal Lambda function 
variable_name = lambda (parms,..) : expersion
'''
# sample function 
def print_hello(name):
    print(f"hello {name}")

print_hello('Muhammed')

# lambda function 
print_lambda_hello=lambda name : print(f'hello  {name} in Lambda function ')
print_lambda_hello('Muhammed')  # call function lambda 
print(print_lambda_hello)     # return address of function lambda

# lambda function return expersion without make return
# __name__ for knew name of function 

print(print_hello.__name__) # print_hello
print(print_lambda_hello.__name__) # lambda 