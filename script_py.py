
'''
 data structure like list and dic is mutable means we can replace value in it 
 any object of list and dic access same of address 
'''
l1=[1,2,3,4]
# l2=l1    # this is big pug because l2 have the same address memory of ll
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
tuple and string is immutable data structure means can not changes values in it after assignment  
"""
my_s='muhammed'
#my_s[0]='d'   # error
my_s1=my_s.replace('m','M')
print(f' my_string is   {my_s}' )
print(f' my_string1 is   {my_s1}' )

# homogenes use list means data have a relation l_numbers=[1,2,3,6,5]
# hetrohomogenes use tuple data not have data type t_student=('Ahmed',15)
# decalre tuple
t1=('ahmed', 15)
# not can changes data in tuple
# can acces use index 0 to n-1 
print(t1[len(t1)-1])

# dictionary is best data structure to store key and value as json data
# preferable key is immutable data but value any data type 
dic1={'name':'Muhammed','age':24,'Gender':'M'
, 'Address':{
    'street':5,
    'city':'Bani Suef'
}}

# can acces dict from key as dict[key]
print(f'street is {dic1["Address"]["street"]}')

# loop dict use key as default
print('First Method to access dict') 
#1- loop use key 
for keys in dic1.keys():
    print(f' key is {keys} and value is {dic1[keys]}')
print('Second Method to access dict') 
#2- loop use value 
for value in dic1.values():
    print(f'values of dic1 is {value}')
print('Third Method to access dict') 
#3- loop use value and key 
for key,value in dic1.items():
    print(f'key is {key} and value is {value}')

# to search about key
# 1- to search values if key in dic but avoid use 
if "name" in dic1:
    print('this dict has key name')  
else:
    print('key is not find ')
#  key not can repeate more than times 

# 2- * to access key used dict.get(key) if not found return None
if dic1.get('name'):
    print('key is name')
else:
    print('key is not found ')
# to chmage defult use 
if dic1.get('names','DefultName'):
    print('key name is found')
else:
    print('key name is not found and defualt is found')   


# to update dict 
# 1- not used this 
dic1["name"]="Ashraf"
# 2- used this 
dic1.update({'name':'Ahmed'})     
print('Update dic')
for key,value in dic1.items():
    print(f'key is {key} and value is {value}')

# to append new keys
dic1['last_name']='Ashraf'
print('Append new keys')
for key,value in dic1.items():
    print(f'key is {key} and value is {value}')

# to delete key
del(dic1['last_name'])
print('Delete key')    
for key,value in dic1.items():
    print(f'key is {key} and value is {value}')

list_1=[1,10,7,41,8,5,4]
for i in list_1:
    if i%3==0:
        print('found')
        break
else:
    print('not break ')    
    
l=list(range(5))
for i in l:
    print(i)
