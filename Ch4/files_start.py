#
# Read and write files using the built-in Python file methods
#

def main():  
   """comments
   Open a file for writing and create it if it doesn't exist
   """
   # f=open("Textfile.txt","w+")

  
  # Open the file for appending text to the end
   f=open("textfile.txt","r")


  # write some lines of data to the file
  #  for i in range(1,10):
  #    f.write(f"This line is {i} \r\n")

  
  # close the file when done

   # f.close()
  # Open the file back up and read the contents
  #  if f.mode=="r":
  #    content=f.read()
  #    print(content)
  #readline
   if f.mode=="r":
     for x in f.readlines():
       print(x)

    
if __name__ == "__main__":
  main()
