from functools import reduce

'''
Learn: 
    - Reduce function
    - enumrate() , help() , reversed()
'''

"""
Reduce function:
    - Reduce take function + itertor 
    - Reduce run function on first and second element and give result
    - Then run function on reuslt and Third element
    - Then run function on result and Fourth element
    - Till one element is left and this is result of reduce 
    - The function can be defined def or lambda 
"""

# to use reduce import from functools
def all_sum(num1,num2):
    return num1+num2
my_numbers=[1,5,20,100]
reuslt=reduce(all_sum,my_numbers)
print(reuslt) # reduce function return result 

# ( ( (1+5) + 20 ) + 100 ) = 126
# explan reduce use for apply some rules of all elememnt 
print("#"*50)
# reduce with lambda
result = reduce(lambda num1,num2 : num1+num2,my_numbers )
print (result)

print("!"*50)
# enumurate function use for loop on index or key and value on iterable 
for i,v in enumerate(my_numbers):
    print(f"index {i} value {v}")

print("%"*50)
help(reversed)  # help(function or object) return defination of this object

print("@"*50)
name="Mohammed"
# reversed(iterable)  reverse this iterable
for chr in reversed(name):
    print(chr,end=" ")
print(" ")    