from datetime import date
from datetime import time
from datetime import datetime
def main():
    today=date.today()
    print(today)
    print(f"The component of date {today.day},{today.month},{today.year}")
    """
    Find the weekday number
    
    """
    print(f"Today weekday number is: {today.weekday()}")
    """
    To prrint the current day name
    """
    day=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    print(f"The day is {day[today.weekday()]}")
    """
    To print the week day and name do this
    """
    print(f"The day is {day[today.weekday()]},{today.weekday()}")
main()