from datetime import  date
from datetime import time
from datetime import datetime
from datetime import timedelta


"""
How many days until Aprils fools day
"""
#Now find the today date
today=date.today()
print("This the today date "+ str(today))
afd=date(today.year,4,1)
print("To Show the April 1 day :"+str(afd))
"""
afd mean april fool day basically in this block of statment represent the whole datetime functionaly methods keywords and time delta 
"""
#so this afd<statement tell us that days and datetime can be compare
if afd < today:
    #it counts the days passed in this years related to april
    number_of_passed_days=(today-afd).days
    print(f"Aprils Fools day already went by : {number_of_passed_days}")
    #so if the aprill had passed then we will move to next year
    afd=afd.replace(year=today.year+1)
time_to_afrild=afd-today
print("its just" , time_to_afrild ,"days until April Fool's day")

