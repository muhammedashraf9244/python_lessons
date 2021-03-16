"""
Learn: 
    - Collection in python 
    - List and methods in python
"""

'''
Collection or Data Structure in python 
Data structure like List and Dic is Mutable means we can replace value in it 
any object of list and dic access same of address 
Very Important 
List store multi dataype as is Heterogeneous data structure 
Dictoniary store multi dataype as is Heterogeneous data structure 
'''
# declartion list 
my_list=[1,2,3,4]
# or 
my_list=list() # or mylist=[] # empty list
my_list.append(10)
print(my_list)
'''
# error 
my_list=list()
my_list[0]=1  # error
my_list[1]=2  # error
'''
# Acccess index of list using Silicing [start:end] or [start:end:step]
my_list=[1,2,3,6,8,6,10,225,336,10,25,633,63,85 ]
print(my_list[-1])  # 85
print(my_list[-1:5:-1]) # from end to index of 5 from end and step is -1 because default step is 1
print(my_list[4:]) # from index 4 to last 
print(my_list[:9]) # from start index (0) to 9 (9-1)=8
# Very Imprtant in list [start:end] end is end-1
# Very Important default step is 1
'''
Method in List
insert(index,value) insert value with index  
append(value) or append([i,c,...]) append value as it no changes in after last index
pop() remove last index or pop(index) reomove value of this index
remove(Object) or remove(Value) remove value if found if not make error so use try and catch
extend(value) append value after last index , extend([i,a,...]) append each value in list
count(value) return n number of occurrences of value if not found return 0
sort() sort list but must data in list is homgeneous data type  
'''
print(my_list.pop(8))
my_list.append(2563)
print(my_list)
my_list.insert(4,1000)
print(my_list)
try:
    my_list.remove(8)
    my_list.remove(0)
except:
    print('The value 0 not found in list')
print(my_list)
# extend method extend elemnet and append 
myappend_list=["aaaa",25,True,0]
my_list.extend(myappend_list)
print(my_list)
print(my_list.count(254866))
my_list=my_list[:12]
try:
    my_list.sort()
except:
    print('This list is not homogeneous data structure')
print(my_list)