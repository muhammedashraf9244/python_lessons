"""
Learn:
    - Iterable & Iterator
    - Generator
"""

"""
Iterable 
    - Object contain data can be iterated upon
    - Example (List,Dic,Set,Tuple,String)
Iterator
    - Object used to iterate over iterable using next() Method return 1 element by element 
    - You can genarate iterator from iterable using iter()
    - For loop alreday call iter()
    - 
"""
mystr="Muahmmed"  # iterable object 
for c in mystr:
    print(c,end=" ")
print("$"*50)

l=list(range(5))  # iterable object
for i in l:
    print(i,end=" ")
print("")  

"""
# This code not run because num is integer datatype not iterable
num=1586
for digit in num:
    print(digit)
"""

# iterator 

# print(next(l))  error

l_itertor=iter(l)
print(next(l_itertor))
print(next(l_itertor))
print(next(l_itertor))
print(next(l_itertor))
print(next(l_itertor))
# print(next(l_itertor))  # error StopIteration
# for i in iter(l):
#     print(i)
# for i in l_itertor:
#     print(i)

print("Genertor"*5,"\n")
"""
Generator:
    - Genrator is a function but use yield instead of return
    - It support iteration and return generator by calling yield
    - Generator function can use more yield statement
    - By using next() it resume from start 
"""
# generator function
def generator_fun():
    print("Hello 1")
    yield 1
    print("Hello 2")
    yield 2
    print("Hello 3")
    yield 3
    print("Hello 4")
    yield 4
    print("Hello 5")
    yield 5
    print("Hello 6")
    yield 6
    
# not generator fun
def generator_fun2():
    return 1

gen=generator_fun()
print(gen)  # print object generator
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for item in gen:
    print(item)
