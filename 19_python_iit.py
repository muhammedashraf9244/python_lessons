"""
Learn:
    - Error and exception 
    - 
"""

"""
Errors and Exception:
    - Exception is run time error mechanism 
    - Exception give you message to understand the problem
    - Traceback give the line to look for code in this time
    - Exception have types (Syntax error, Indexerror,  )
    - Exception list in python https://docs.python.org/3/library/exceptions.html 
"""
# x=1
# if 10/x:
#     raise Exception("Not divide 10/0")

"""
Exception Handle:
-- Try | Except | Else | Finally
----------------------------
Try => test code for errors
Except => Handel the error
Else => If no error 
Finally => Run the code
"""

try:
    # grade = int(input("Enter your Grade: "))
    print(int('Error heppens'))
except NameError:
    print("Identifier not declartion")
except ValueError:
    print('This grade is not intger')  
except:
    print('Error happens')  
else:
    print('No error in enter grade')
finally:
    print('Run code unitl if found errors')


