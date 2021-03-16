'''
Lear:
    - Dictionary and method 
    - For and else statement
'''

# Dictionary is best data structure to store key and value as json data
# preferable key is immutable data type (string) but value any data type 
dic1={
'name':'Muhammed',
'age':24,
'Gender':'M',
'Address':{
    'street':5,
    'city':'Bani Suef'
},
"email":["hom9244@gmail.com","muhashraf@gamil.com"]
}

# can acces dict from key as dict[key]
print(f'street is {dic1["Address"]["street"]}')
print(f'The first email {dic1["email"][0]}')

# How add new value 
# list use append
dic1["email"].append("ashraf9244@gmail.com")
dic1["Gender"]="F"

# loop dict use key as default
print('First Method to access dict') 
#1- loop use key keys() return key 
for keys in dic1.keys():
    print(f' key is {type(keys)} and value is {dic1[keys]}')
'''
# anthor way of print key 
for key in dic1:
    print(f"v is {key}")
'''
print('Second Method to access dict') 
#2- loop use value values() return value 
for value in dic1.values():
    print(f'values of dic1 is {value}')

print('Third Method to access dict') 
#3- loop use value and key store in tuple
for key,value in dic1.items():
     print(f'key is {key} and value is {value}')
# for t1 in dic1.items():
#     print(f'key is {t1[0]} and value is {t1[1]}')

# to search about key or values
# 1- to search if key in dic use keys()
# or if key in dic1:
if "name" in dic1.keys():
    print('this dict has key name')  
else:
    print('the dict not have key name ')
#  key not can repeate more than times 

# 2- Search about value in dic1 use values()
# but if key store list of data use get(key) 
if "hom9244@gmail.com" in dic1.get('email'):
    print('hom9244@gmail.com is found')
else:
    print('hom9244@gmail.com is not found')


# 2- to access key used dict.get(key) if not found return None
if dic1.get('name'):
    print('key is name')
else:
    print('key is not found ')
'''
Very Important
But if use dic1[key] this key is not found return error 
'''
# to change defult use 
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

'''
else with for and break means if found for and break not be interpret anyone times
in this condition else will be interpreted
'''
list_1=[1,10,7,41,8,5,4]
for i in list_1:
    if i%3==0:
        print('found')
        break
else:
    print('not break ')    

# pass statement use if we not know what code with run
# _ means loop without count number of iteration
for _ in range(10):
    pass
l=list(range(5))
for i in l:
    print(i)