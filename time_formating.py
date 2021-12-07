"""
Time Formating
Date Formating
strftime()
%y/%Y - Year , &a/&A - Weekday , %b/%B - Month ,%d -day of month
another method is
%c - Locale date and time ,%x - Locale's date , %X - Locale's time
%I/%H - 12/24 Hour , %M - minutes ,%S - second , %p - locale's AM/PM
"""

from datetime import date
from datetime import time
from datetime import datetime
def main():
    now=datetime.now()
    print(now)
    # % y / % Y - Year, & a / & A - Weekday, % b / % B - Month, % d - day of month

    # print(now.strftime("%a,%d,%B,%y"))
    # % c - Localedate and time, % x - Locale's date , %X - Locale's time
    # print(now.strftime("%c"))
    # print(now.strftime("%x"))
    # print(now.strftime("%X"))
    """
    Time Formating
    %I/%H - 12/24 Hour , %M - minutes ,%S - second,%p - locale's AM/PM
    """

    print(now.strftime("current time %I:%M:%S %p"))
    print(now.strftime("24 hours format: %H:%M"))

main()