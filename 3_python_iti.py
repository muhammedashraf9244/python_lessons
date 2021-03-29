"""
Learn:
    - Mutable and Immutable in python
    - If string is immutable data type
    - String methods in python
    - String Format with float numbers 
"""


# Vey Important Mutable and Immutable 
'''
Mutable data type can changes value in place 
Immutable data type not can changes value in place 
'''
# Very Important String is Immutable
first_name, mid_name = "Mohammed ","Ahmed "
last_name="Ali"
age=24
fullName = f"{first_name}{mid_name}{last_name} my age {age} "
print(fullName)
print(fullName[5])
#fullName[5]="M" # error becasue string is Immutable
# we use replace and assign in varaible
fullName=fullName.replace('a','A')
print(fullName)
# String Method
print(fullName.capitalize()) # for Capitalize captial each char from start word but if char is captial covert to samll char 
print(fullName.title())  # captial each char if found char is captial do not change 
print(len(fullName)) # for length of string
digits,containDigits = "0102002932", "Tel0102002932"
print(digits.isdigit())
print(containDigits.isdigit())
'''
go to https://towardsdatascience.com/41-questions-to-test-your-knowledge-of-python-strings-9eb473aa8fe8
strip() rstrip() lstrip() default remove spaces
strip() remove spaces from rigth and left 
rstrip() remove spaces from rigth 
lstrip() remove spaces from left  
find(sub, start=0, end=-1) return start index of sub if found in string else return -1 
index(sub, start=0, end=-1) reurtn start index of sub if found in string else give error 
'''
my_str="  I am pythonist  "
print(my_str.find('amn'))
# print(my_str.index('amn')) # error 
print(my_str.strip())
print(my_str.rstrip())
print(my_str.lstrip())
#   change default strip(chr)
my_str="#@#@@@@@@I am pythonist#@#@####@"
print(my_str.strip("#@"))
print(my_str.rstrip("#@"))
print(my_str.lstrip("#@"))
'''
upper() Return a copy of the string converted to uppercase.
lower() Return a copy of the string converted to lowercase.
zfile(width) add zeros on the left, to fill a field of the given width.
'''
my_str="muhammed"
print(my_str.upper())
print(my_str.lower())
c,d,f='1','11','111'
print(c.zfill(3))
print(d.zfill(3))
print(f.zfill(3))

'''
split(sep, maxsplit) * rsplit(sep, maxsplit) Return a list of the words in the string,
using sep defalut sep is space 
maxsplit number of split string but 
split(sep,maxsplit=n) split n string and the rest of string split all in one elemnt in list from left
rsplit(sep,maxsplit=n) split n string and the rest of string split all in one elemnt in list from right
'''
my_str="I love python and java and c++"
print(my_str.split(maxsplit=2))
print(my_str.rsplit(maxsplit=2))

'''
splitlines(keepends) Return a list of the lines in the string, breaking at line boundaries.
if Keepends True return \n with line 
'''
my_multiline_str="""
Line 1
Line 2 
Line 3
"""
my_str="Line1\nLine2"
print(my_multiline_str.splitlines(True))
print(my_str.splitlines(True))
# Slicing use index to get valued from list [start:end] or [start:end:step]
print(fullName[10:1:-1])

#  String Format with float number 
"""
Formatting expressions
Expr	Meaning	                                        Example
{:d}	integer value	                                '{:d}'.format(10.5) → '10'
{:.2f}	floating point with that many decimals	        '{:.2f}'.format(0.5) → '0.50'
{:.2s}	string with that many characters	            '{:.2s}'.format('Python') → 'Py'
{:<6s}	string aligned to the left that many spaces	    '{:<6s}'.format('Py') → 'Py    '
{:>6s}	string aligned to the right that many spaces	'{:>6s}'.format('Py') → '    Py'
{:^6s}	string centered in that many spaces	            '{:^6s}'.format('Py') → '  Py  '
"""
