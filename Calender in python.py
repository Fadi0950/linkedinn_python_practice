#This is clendar module
import calendar
from datetime import date
from datetime import time
from datetime import datetime
#create a plain text calendar
calend=calendar.TextCalendar(calendar.MONDAY)
st=calend.formatmonth(2017,1,0,0)
print(st)