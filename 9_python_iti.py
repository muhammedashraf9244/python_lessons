'''
Learn:
    - Lexical Scope & Golobal Scope
    - Shorthand If 
    - Multiple assignment & swap
    - Enhanced Print menas change print out
    - Split & Join
    - is , is not
    - Enumerate function 
    - all , any , id , bin , ord bulit in function
    
'''
"""
Trips & Trick 
    Lexical Scope & Golobal Scope
    lexical scope means when define varaible in block of code 
    interpreter see if varaible not define in this block, see outside block  
"""
# golobal varaible
name="Mohammed"
def my_fun():
    # local varaible
    name="Ali"
    print(f"name in my_fun {name}")

my_fun()
print(f"name in global scope {name}")

my_list=[]
print('Access golobal varaiable ')
# if i want to access golobal varaible use keyword name global
def my_fun_g():
    # local varaible
    my_list.append("In Function not use noglobal")
    global name
    name ="Ali"
    print(f"name in my_fun {name}")
my_fun_g()

print(f"name in global scope {name}")
print(f"my list f{my_list}")

'''
List and Dic not use global with it
Immutable data structure use = and golobal 
imutable data struture not use golobal or = 
'''

'''
Shorthand If 
var_name=value if exper else anthor_value
'''
grade_numeric=80
grade_letter="C" if grade_numeric >= 78 and grade_numeric <=  85 else "D"
print(f'grad {grade_letter}')

'''
Multiple assignment & swap
'''
a,b=5,6
#sawp
a,b=b,a
print(f'a {a} b {b}')
#multiple assignment 
x,y=(1,2)
x1,y1=[1,2]
print(f'x {x} y {y}')
print(f'x {x1} y {y1}')

# * means zero or one 
# Sequence Unpacking
x2,y2,*m,z=(1,2,3,5,6,9,6,10)
# * with variable is list 
print(f'x2 {x2} y2 {y2}')
print(f'm {m} type *m is {type(m)}  z {z}')

# *list_name means unpacking each elemnt in list
lis1=[1,2,3]
print(*lis1)

'''
Enhanced Print menas change print out 
'''
print("I’m ", end=" ")
print("Ahmed", end="\n")

'''
Split & Join
string_name.split(sep) or sep.join(list_name)
split convert string to list above sep
join convert list to string
'''
mystr="Ahmed Mohammed Ali"
mylist=mystr.split(" ")
print(f'mylist {mylist}')
my_new_str=":".join(mylist)
print(f"str {my_new_str}")

'''
== , is 
!= , is not 
== eqaul values but is equal refernces 
!= , is not eqaul values but is not equal refernces 
'''

lis1=[1,2,3]
list2=[1,2,3]
print(f"list1==list2 {lis1==list2}")
print(f"list1 is list2 {lis1 is list2}")
list3=lis1
print(f"list1==list3 {lis1==list3}")
print(f"list1 is list3 {lis1 is list3}")

'''
Enumerate function use if i want to loop on list with index and value
'''
for i,v in enumerate(lis1):
    print(f"index {i} value {v}")

'''
all , any , bin , id 
all(iterable) return True if All values is evaluate to true
any(iterable) return True if one or more is evaluate to true
bin(a) return binary number of a
id(variable) return address of variable in memory 
ord(char) return ACII code of this character
'''
# a = 10,12 # tuple of data
a,b=10,12
l1=[1,2,3]
l2=l1   # get the same referance of l2
print(all([[],1,2,3,""]))
print(any([[],1,2,3,""]))
print(bin(5))
print(id(a),id(b))
print(id(l1),id(l2))
print(ord('A'))