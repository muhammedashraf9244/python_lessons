'''
Learn:
    - Contorl & Loop Statement
    - Break and Continue Statement
    - for and else statment 
    - input function   
'''
# control
x=int(input("Enter value of X: "))
if x==5:
    print("x is equal 5")
elif x > 5:
    print("x is bigger than 5") 
else:
    print("X is small than 5") 

# looping use for
my_list=[1,2,8,2,9,7,10,45]

'''
in JS 
for(int i=0;i<my_list.length-1;i++){
    consel.log(my_list[i])
}
as in python is easy use for as for each about each element and print value 
'''
# first method 
for i in my_list:
    print(i)

# seond method 
# use static length 
for i in [0,2,3,4,5,6,7]:
    print(my_list[i])

# Third Method use dynamic length use range(start,stop,step) fun
for i in range(0,len(my_list),1):
    print(f"index {i+1} and value {my_list[i]} ")

'''
or 
for i in range(len(my_list)):
    print(f"index {i} and value {my_list[i]} ")
range(n) genarate number form 0 to n-1 and setp is 1
'''
# looping use while 
count=0
while count <= len(my_list)-1:
    print(f"index {count+1} and value {my_list[count]} ")
    count+=1

# break & continue
# continue means not compile next instruction and start form next iteration
# break means stop compile statemnts in loop and exit from this block of code 
count=0
while count <= len(my_list)-1:
    if my_list[count]%2==0:
        count+=1
        continue
    else:
        print(f"The odd number is {my_list[count]} ")
        count+=1

# input function for enter input form user
# defalut data enter form input is string
name=input('Enter your name: ')
age=int(input('Enter your age: '))
print(f'Your name name {name} type is {type(name)}')
print(f'Your age {age} type is {type(age)}')