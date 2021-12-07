"""
1-What should come instead of the ???
2-placeholders for this code to correctly print the number of days until your birthday on Jun 30?
3-Hint: the number of days in a timedelta object can be returned using its days attribute.
"""


from datetime import time
from datetime import date
from datetime import datetime
from datetime import timedelta
today=date.today()
bday=date(today.year,6,30)
diff=(bday-today).days
if diff>0:
  print("Birthday in %d days" % diff)
else:
  print("Birthday in %d days" % (diff+365))

