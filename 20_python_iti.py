"""
Learn:
    - Regular Expersion
"""

"""
Regular expersion is a sequence of characters that define  a search pattern
Regular expersion is not in python its general concept
go to https://www.debuggex.com/cheatsheet/regex/python for all Python Regex 
Quantifiers
* 0 or more 
+ 1 or more
? 0 or 1 
{2} Exactly 2
{2,6} Exactly from 2 to 6
{3,} from 3 to more
{,6} from 1 to 5
"""

"""
Reqular Expersion => Charaters class 
[0-9] one numbers form 0 to 9 eqaul \d
[a-z] one charaters from a to z equal \w
[A-Z] one charaters from A to Z equal \w
[a-zA-z] one charaters from a to z and A to Z equal \w
[^a-z] one charcter except from a to z  equal \W
[^A-Z] one charcter except from A to Z  equal \W
[^0-9] one number except from 0 to 9  equal \D
"""
"""
Regular Expression Assertions
^	Start of string
\A	Start of string, ignores m flag
$	End of string
\Z	End of string, ignores m flag
\b	Word boundary
\B	Non-word boundary
"""
"""
email match: ^[a-zA-Z0-9\.]+@[a-z0-9]+\.(com|org|net)$
"""

"""
Regular expersion
| or 
\ Escape special characters
() Sperate group
example 
[1] (\d-|\d\>|\d\))\s?(\w)+  for 1-Html or 2>JS or 3)python
[2] ^(\d{3})\s(\d{4})\s(\d{3}|\(\d{3}\))$  for 026 2569 355 or 256 2563 (255)
[3] ^(https|http)(\:\/\/)(\w+)\.(org|com|net)$  
or 
^(https?\:\/\/)(www\.|WWW\.)?(\w+)\.(org|com|net|info)$
for 
https://pythex.org
http://pythex.com
https://pythex.net
http://www.pythex.com
http://WWW.pythex.com
"""

"""
Regualr expersion in python use re
-------------
search(reglar,sting)  return string for a match and return only first string match
findall()  return list of all string which match and return empty list for no match
"""

import re

# my_re=re.search('[A-Z]','Muahmmedashraf')

# print(my_re)  # <re.Match object; span=(0, 1), match='M'>

# span is index of string which match M
# my_re=re.search('[A-Z]','muahmmedAShraf')
# print(my_re)  # <re.Match object; span=(8, 9), match='A'>

# print(dir(my_re))
# print(my_re.span()[0])  # index which match
# print(my_re.string[my_re.span()[0]:my_re.span()[1]])  # string of index which match

email="Muhmmed.Ashraf96@gemkd.org"
my_email_paatern=r'^[a-zA-Z0-9\.]+@[a-z0-9]+\.(com|org|net)$'
is_email=re.findall(r'^[a-zA-Z0-9\.]+@[a-z0-9]+\.(com|org|net)$',email)

is_match = re.match(my_email_paatern,email)
print(f'is match {is_match}')
if is_match:
    print(f'This {email} is valid ')
else:
    print('This email is not valid')    

    