"""
Learn:
    - zip() 
    - Pillow Module
    - Documenting vs Commenting
    - Pylint and giw use for enhancement code 
"""
'''
Loop many than itertor zip()
zip() return a zip object conatin all objects
zip() length is the length of lowest iterable
'''

# list1=[1,2,3,4]
# list2=["Ahmed","Muhammed","Ali"]

# zip_obj=zip(list1,list2)
# print(zip_obj)  # object zip

# # for print loop on the lowest length of iterable 
# for item_list1,item_list2 in zip_obj:
#     print(f"Item list 1 {item_list1}")
#     print(f"Item list 2 {item_list2}")

# Practical with image
# from PIL import Image
# myImage=Image.open("./profile.png")
# myImage.show()

# go to https://pillow.readthedocs.io/en/stable/

"""
Documenting vs Commenting
    - Documenting is string for explan class or function and module
    - Can be access from help()
    - Made for understand functionality of complex code
    - There are one line and multible line
"""

# def print_hello():
#     '''This function use for print hello python'''  # this is Document for explain function
#     print("Hello in python")

# print_hello()
# print(dir(print_hello))
# print(print_hello.__doc__)
# help(print_hello)

def print_hello(name):
    '''
    print_hello function use for
     print name hello python
     Parameters:
      name => person name that use function
     Return:
      Return hello Message from person
     '''  
    print(f"Hello {name}in python")

#print(print_hello.__doc__)
help(print_hello)
