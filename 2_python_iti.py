"""
Learn:
    - Indentations in python
    - Type Operators in python
    - Boolean Data type and Logical Operators
    - Print format in python
"""


"""
Line Indentations means block of code in other PL use {} but in python use Indentations

Level 1
    Level 2
if True:
    print(“Hello, World”)
else:
    print(“Bye, World”)

No use ; or {}
"""

# Operators in Python 
'''
1- Arithmetic Op
+ addition Op 2 + 3 #output: 5
- Subtraction Op 4 – 2 #output: 2
* Multiplication Op 4 * 5 #output: 20
/ Division Op 16 / 5 #output: 3.2
% Modulus Op 16 % 5 #output: 1
// Division without Fractions 16 // 5 #output: 3
** Exponentiation Op 2**4 = 16 
= assignment Op a=b means get value of b and store in a this s not eqaul
++x postfix 
x++ prefix
() partenes 

2- ShortCut Operator 
+= add and assign x += 3 #output: 7
-= subtract and assign x -= 2 #output: 5
*= multiply and assign x *= 6 #output: 30
/= divide and assign x /= 2 #output: 15
%= get modulus and assign x %= 8 #output: 7
//= floor divide and assign x //= 3 #output: 2
**= get exponent and assign x **= 4 #output: 16

3- Comparison Op
a <op> b
== return True if a equals b 
>= return True if a equals or greater than b
<= return True if a equals or lesser than b
!= return True if a not equals b
<> return True if a not equals b
> return True if a greater than b
< return True if a lesser than b
is is same  == but it compare between referances  
is not is same != but it compare between referances 

4- Logical Op or Boolean Op use to combine many of expersions 
and AND Logic Gate means True if and only if both sides is True
or OR Logic Gate means True if and only if one or more sides is True 
not Not Logic Gate means reserve output form True to False and so
'''
# Very Important 1 is equal True and 0 is equal False
print("True==1 ",True==1) 
print("False==0 ",False==0) 
# but any numbers not 1 or 0 not equal True of False
print("True==2 ",True==2) 

print('True=="True" ', True=="True") # means if True equal "True"  
print('"True"=="True" ',"True"=="True") 
print(f'"True" is "True" {"True" is "True"}') 
print("not(True==2) ",not(True==2)) # beacause True is 1 


# Very Impoertant any value of this is evaluate to False
'''
{},[],(),"",'',None,0,False is evaluate to False
any Others of them is evaluate to True
'''

# Very Important is experations like this 
exp=0 or 1
print(exp)
exp= 1 or "sss"
print(exp)
exp= 1 and 0
print(exp)
exp= 0 and 1
print(exp)
'''
This means or if catch True is stop but 
and if catch False is stop
'''
exp=458 and "dddddddlublub"
print(exp)
exp=[] and "dddddddlublub"
print(exp)
exp=458 and "dddddddlublub" and 0
print(exp)
exp=0 or "dddddddlublub" and 111
print(exp)

exp="SS" and 0 or "dddddddlublub" and 111
print(exp)

exp="SS" and 0 or "dddddddlublub" or 111
print(exp)

"""
Concatonation in string 
"""
# Fisrt Method
first_name="Mohammed "
mid_name = "Ahmed "
last_name="Ali"
age=24
print(mid_name) # Ahmed
fullName = first_name + mid_name * 3 + last_name +" my age "+str(age)
print(fullName) # Mohamed Ahmed Ahmed Ahmed Ali
# Second Method use placehorder %s for str, %d for Integer, %f for Float
fullName = "Hello %s%s%s my age %d"%(first_name,mid_name*3,last_name,age)
print(fullName)
# Third Method use Format function
fullName= "Hello {}{}{} my age {}".format(first_name,mid_name*3,last_name,age)
print(fullName)
# Fourth Method use format 
print("Hello {0}{1}{2} my age {3}".format(first_name,mid_name*3,last_name,age))
# Five Method use format
print("Hello {first_name}{mid_na}{last_name} my age {age}".format(first_name=first_name,mid_na=mid_name,last_name=last_name,age=age))
# Best Format is use f and {}
print(f"Hello {first_name}{mid_name}{last_name} my age {age}")