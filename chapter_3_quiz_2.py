"""
Question 2
1-Which code can you use to print a standard,
2-text-formatted monthly calendar for every month in 2020,
3-using Sunday as the first day of the week?
"""

import calendar
cal = calendar.TextCalendar(calendar.SUNDAY)
for m in range(1,13):
    print(cal.formatmonth(2020, m, 0, 0))