"""
calculate day based on a rule:For Example ,consider
A team meeting on the first friday of every month
To figure out what days that would be for each month
we can use this script
"""
import calendar
print("Team meeting will be on :")
for i in range(1,13):
    c=calendar.monthcalendar(2018,i)
    week_one=c[0]
    week_two=c[1]
    if week_one[calendar.FRIDAY] !=0:
        meetday=week_one[calendar.FRIDAY]
    else:
        meetday=week_two[calendar.FRIDAY]
    print("%15s %2d" %(calendar.month_name[i],meetday))