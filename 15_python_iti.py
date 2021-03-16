"""
Learn:
    - Module Dateime
"""

"""
datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])  
The year, month and day arguments are required. tzinfo may be None
now() # return datetime now year-month-day hour:second:minute
date() return date only year-month-day
time() return time hour:minute:second
year poroprite return year
day poroprite return day
month poroprite return month
hour poroprite return hour
second poroprite return second
minute poroprite return minute
year poroprite return year
min return min datetime
max return max datetime
"""
# import datetime.datetime
from datetime import datetime

# print(dir(datetime))  # print all methods and porprites in class datetime
print(f" date now => {datetime.now()}")
print(f" date only => {datetime.now().date()}")
print(f"year only => {datetime.now().year}")
print(f"month only => {datetime.now().month}")
print(f"day only => {datetime.now().day}")
print(f"hour only => {datetime.now().time().hour}")
print(f"second only =>{ datetime.now().time().second}")
print(f"minute only =>  {datetime.now().time().minute}")

print(f"Min => {datetime.min}")
print(f"Max => {datetime.max}")

print(f"Min time => {datetime.min.time()}")
print(f"Max time => {datetime.max.time()}")

# print secific time
print(datetime(2010,2,10))

# calculate age of person
my_brith_day=input("Enter your birth day as dd-mm-yyyy: ")

# print(datetime.strptime(my_brith_day,'%d-%m-%Y'))
my_date_brith=datetime.strptime(my_brith_day,'%d-%m-%Y')
date_now=datetime.now()
age=date_now-my_date_brith  
print(f"your age => {age.days//365} Years")

"""
Date Fromat
strptime(str_date,format) new datetime parsed from a string (like time.strptime()).
striftime("Format") Format time as you like 
go https://strftime.org/
Eample format time
%a	Weekday as locale’s abbreviated name.	Mon
%A	Weekday as locale’s full name.	Monday
%w	Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.	1
%d	Day of the month as a zero-padded decimal number.	30
%-d	Day of the month as a decimal number. (Platform specific)	30
%b	Month as locale’s abbreviated name.	Sep
%B	Month as locale’s full name.	September
%m	Month as a zero-padded decimal number.	09
%-m	Month as a decimal number. (Platform specific)	9
%y	Year without century as a zero-padded decimal number.	13
%Y	Year with century as a decimal number.	2013
%H	Hour (24-hour clock) as a zero-padded decimal number.	07
%-H	Hour (24-hour clock) as a decimal number. (Platform specific)	7
%I	Hour (12-hour clock) as a zero-padded decimal number.	07
%-I	Hour (12-hour clock) as a decimal number. (Platform specific)	7
%p	Locale’s equivalent of either AM or PM.	AM
"""
print(my_date_brith.strftime("%B"))
print(my_date_brith.strftime("%b"))
print(my_date_brith.strftime("%-m"))
print(my_date_brith.strftime("%a"))
print(my_date_brith.strftime("%A"))
print(my_date_brith.strftime("%d"))
print(my_date_brith.strftime("%-d"))

print(my_date_brith.strftime("%A %B %y"))

print(my_date_brith.strftime("%A - %B - %y"))