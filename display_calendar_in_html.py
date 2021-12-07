#This is clendar module
import calendar
from datetime import date
from datetime import time
from datetime import datetime
c=calendar.HTMLCalendar(calendar.SUNDAY)
st=c.formatmonth(2017,1)
print(st)