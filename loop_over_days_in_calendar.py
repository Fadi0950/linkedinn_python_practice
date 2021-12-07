#loop over days of calendar
#zero's mean that the day of the week is in an overlapping month
import calendar
# c=calendar.TextCalendar(calendar.SUNDAY)
# for i in c.itermonthdays(2017,8):
#     print(i)
"""comments
The calendar module provide usefull utilities of the given locale,
such as the name of the days and months in both full abbreviated form 
"""
for name in calendar.month_name:
    print(name,end=' ')
print("\r")
for day in calendar.day_name:

    print(day,end=' ')

