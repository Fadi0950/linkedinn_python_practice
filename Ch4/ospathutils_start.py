#Important
# Example file for working with os.path module
#

import os
from os import path

import datetime
from datetime import date, time, timedelta
import time


def main():
    """comments
    Print the name of the OS
    """
    print(os.name)



  
  # Check for item existence and type
  #   print(f"File exist:"+str(path.exists("textfile.txt")))
  #   print("Item is file:"+str(path.isfile("textfile.txt")))
  #   print("item is a directory:"+str(path.isdir("textfile.txt")))

  
  # Work with file paths
  #   print("Item path is:"+str(path.realpath("textfile.txt")))
  #   #separating item name form path
  #   print("Item path and name:"+str(path.split(path.realpath("textfile.txt"))))

  
  # Get the modification time
  #   t=time.ctime(path.getmtime("textfile.txt"))
  #   print(t)
  #   print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))

  
  # Calculate how long ago the item was modified
    td=datetime.datetime.now()-datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print(f"It has been {td} since the file was modified")
    print(f"or total seconds:{td.total_seconds()}")

  
if __name__ == "__main__":
  main()
