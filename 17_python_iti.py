"""
Learn:
    - Decorators
"""
"""
Decorators:
    - In others PL Mata programming
    - Every thing in python is object
    - Decorator take a function and add some functionality and return it 
    - Decorator warp other function and enhance Bahaviour
    - Decorator is higher order function  
"""
# def myDecorator(func):
#     def nested_func():
#         print("Before")
#         func()  # Execute
#         print("After")
#     return nested_func

# @myDecorator
# def hello():
#     print("Hello form Decorator")


# my_dec=myDecorator(hello)
# print(my_dec)  # decorator object
# my_dec()
# hello()

# call decorator by paramters
# def myDecoretor2(func_multibly):
#     def nest_fun(num1,num2):
#         if num1 or num2 < 0 : print("Bewary there are negative integer")
#         print("Before in myDecorator2")
#         func_multibly(num1,num2)
#     return nest_fun 

# def myDecoretor3(func_multibly):
#     def nest_fun(num1,num2):
#         print("Coming from in myDecorator 3")
#         func_multibly(num1,num2)
#     return nest_fun 

# @myDecoretor3
# @myDecoretor2
# def calc_multiply(num1,num2):
#     print(f"Mulitply {num1} * {num2} => {num1*num2}")

# calc_multiply(-3,4)
# may be define multi one decorator on function

# if i want pass many paramters

# def myDecoratorCalc(func):
#     def warrper(*args):
#         print("In Decrotor Calc")
#         if not all(list(map(lambda x : x > 0 ,args))):
#             print("Be Wary there are negative numbers in arguments")    
#         f = func(*args)
#         print(f)
#     return warrper 

# @myDecoratorCalc
# def multiply_fun(n1,n2,n3,n4):
#     return (f"{n1*n2*n3*n4}")

# multiply_fun(2,-3,2,1)

# Exmple: calc time excute function

from time import time

def DecrotorTime(func):

    def wrapper():
        start =time()
        func()
        end=time()
        print(f"Function running {end-start}")
    return wrapper
@DecrotorTime
def bigLoop():
    for _ in range(200000):
        pass  # no do any thing Only run loop and calc time using decrator

bigLoop()
