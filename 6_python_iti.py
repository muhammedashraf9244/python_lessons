"""
Learn:
    - Types Collection in python
    - Big mistake when use list
    - Tuple in python
    - Set and methods of it in python 
"""

'''
Collection in python
Tuple, Set, List and Dictionary are heterogeneous data structure means can store multible data type
'''

'''
 Data structure like list and dic is mutable means we can replace value in it 
 any object of list and dic access same of address
 Very Important : All mutable data structure is store as referance in memory 
'''
l1=[1,2,3,4]
# l2=l1    # this is big bug because l2 have the same address memory of ll
#l2[0]=10
# print(f'l1 {l1}')
# print(f'l2 {l2}')

# to avoid this problem if you want copy data from list to anthor 
# 1- use silcing
l2=l1[:]
l2[2]="sd"
print(f'l1 {l1}')
print(f'l2 {l2}')

# 2- extend 
l2=[]   # pointer to empty list
l2.extend(l1)
l2[3]='sdd'
print(f'l1 {l1}')
print(f'l2 {l2}')

# 3- append but this copy data as list of list not use  
l2=[]
l2.append(l1)
print(f'l1 {l1}')
print(f'l2 {l2}')

"""
tuple and string is immutable data structure means not can change values in it after assignment  
"""
my_s='muhammed'
#my_s[0]='d'   # error
my_s1=my_s.replace('m','M')
print(f' my_string is   {my_s}' )
print(f' my_string1 is   {my_s1}' )

# Homogeneous use list means data structure have a same data type l_numbers=[1,2,3,6,5]
# Heterogeneous use tuple data structure not have same data type but related t_student=('Ahmed',15)
# decalre tuple
t1=('ahmed', 15)
# not can changes data in tuple
# can acces use index 0 to n-1 
# Methods in Tuple
'''
index(value) return index if value found else return error use try and except
count(index) reurn number of occurrences of value in Tuple if not found return 0
'''
print(t1[len(t1)-1])
value=15
try:
    print(t1.index(value))
except:
    print(f'This value {value} not found in tuple') 

'''
Sets are used to store multiple items in a single variable
A set is a collection which is both unordered, unindexed, unchangable and 
not allow duplicate data.
unordered means ever loop about data access random not in order sequence  
unindexed menas can not access data using index or key.
unchangable can not change data in set but can add
'''
myset_names={"Mohammed","Ahmed","Ibraim","Mohammed","mohammed"}
for name in myset_names:
    print(name)

myset_hetro={1,2.6,"Mohammed",True,False,True}
for hetro in myset_hetro:
    print(hetro)

'''
After run above code you can understand 
what I mean that set is unordered, unindexed and unchangeable
mohammed != Mohammed
'''    
# 1- Access Set 
#print(myset_names[0]) # error set is not indexded
# Only way to access set is for in loop
print("If Mohammed in set_names ",'Mohammed' in myset_names)

# 2- Add and Update
# add(value) add value in set 
# update(another_Iterable) add another Iterable and if dublicate data with set not allowed
# Iterable can be list or tuple or dic
myset_names.add("Ali")
myset_names.add("Ahmed")
print(myset_names)
myset_names.update(myset_hetro)
print(myset_names)
mylist_age=[25,26,36,20]
# mylist_age is Iterable
myset_hetro.update(mylist_age)
print(myset_hetro)

# 3- remove, discard and pop 
# remove(value) If the item to remove does not exist, remove() will raise an error so use try and except.
# discard(value) If the item to remove does not exist, discard() will NOT raise an error and return None
# pop() method to remove an item, but this method will remove the last item
# Remember that sets are unordered, so you will not know what item that gets removed.

try:
    myset_hetro.remove(0)
except:
    print("0 not found in myset_hetro")

if myset_hetro.discard(0):
    print('0 is found in myset_hetro')
else:
    print('0 not found in myset_hetro')  
