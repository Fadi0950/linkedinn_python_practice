"""
Which code will you use to generate a date and time output in the following format?
13-Mar-2020 16:42:58
"""
from datetime import date
from datetime import time
from datetime import datetime
now=datetime.now()
print(now.strftime("%d-%b-%Y %H:%M:%S"))
