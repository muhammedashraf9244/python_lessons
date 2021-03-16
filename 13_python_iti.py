"""
Learn: 
    - Map function
    - Filter function
"""


"""
Bulit in function => Map :
    - Map take function and itertor map(function,itertor)
    - Map called because map function on every element in itertor 
    - The function can de defined as def or lambda 
"""
def print_n(number):
    return f'{number}'

list_l=list(range(10))

"""
for n in list_l:
    print(n)
"""
list_number = map(print_n,list_l)
print(list_number)  # object map
for n in list_number:
    print(n,end=" ")

# lambda with map 
print(" ")
print("#" * 50)
list_number=map((lambda n : f"{n}"), list_l)
for n in list_number:
    print(n,end=" ")

# for enter number 
'''
n=int(input("enter number of list "))
list_n=[]
for _ in range(n):
    item=int(input("Enter your namber: "))
    list_n.append(item
print(list_n)
'''
# Example for enter numbers 
print(" ")
print("-"*50)
# list_n=list(map(lambda i : int(i),input("enter as 1 2 3 : ").split()))
# list_n=list(map(int,input("enter your list as 1 2 10 : ").split()))
# print(list_n)

"""
Bulit in function => Filter :
    - Filter take function and itertor filter(function,itertor)
    - Filter called filter because return Data of itertor if codtion si True  
    - Filter is same map function run function on every element in itertor 
    - The function can de defined as def or lambda 
    - Function need to retun Boolean Value 
"""
print("\nFilter Function")
print("*"*50)
def checkNumber(n):
    if n > 10:
        return n

list_l2=[10,50,1,8,10,5]
myresult=filter(checkNumber,list_l2)
print(myresult)  # print filter object 
for item in myresult:
    print(item)
print("@"*50)
# if 
list_l2=[10,50,0,0,5,10,8,-60,2]
for item in filter(checkNumber,list_l2):
    print(item)

print("#"*50)
# note That Filter function not return data if all data evalute True 
def checkNumber_1(n):
    return n == 0 
    # if  n == 0 : return True  # ok 
    # if n == 0 : return n # not return data because return data is 0 and 0 is equal False
    # if n > 10 : return True  # ok

for item in filter(checkNumber_1,list_l2):
    print(item)

print("Filter_Lambda"*5)

my_names=["Ahmed","Osam","Ali","Mona","Mohammed"]
for name in filter(lambda name_person : name_person.startswith("A"),my_names):
    print(f"-{name}-")