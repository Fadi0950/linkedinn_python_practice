"""
To perform mathematical operation on date & and time
timdelta module

"""
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
"""

This modules are essential and important for working with date and time
timedelta is a span of a time
not a particular date and a particular time
the timedelta class used for timebase mathematics
"""
""""
Working with timedelta is to be much noticeable b/c it's very important library 
so lets start with it 
"""

#How to construct timedelta
x=timedelta(days=360,hours=5,minutes=1)
print(x)
#print today date
today=datetime.now()
print(f"Today date is: {today}")
#print today's date one year from now
today_2=today + timedelta(365)
print(f"One year from now will be: {today_2} ")

"""
Create a time delta which take more than one argument
"""
print(f"In 2 day and 3 weeks it will be : {today+timedelta(days=2,weeks=3)}")
#Calculate the date one week ago ,formatted as string
t=datetime.now() - timedelta(weeks=1)
# % y / % Y - Year, & a / & A - Weekday, % b / % B - Month, % d - day of month
s=t.strftime("%d,%a,%B,%y")
print(f"one week it was : {s}")
print(type(today))
print(type(s))
