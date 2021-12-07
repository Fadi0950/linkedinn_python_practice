"""
You need to calculate tomorrow's date. Which option should you choose?
"""
from datetime import date
from datetime import time

from datetime import datetime
from datetime import timedelta
today=datetime.today()
print(today)
nextday=today+timedelta(days=1)
print(nextday)