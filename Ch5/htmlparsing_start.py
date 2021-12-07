# https://docs.python.org/3/library/html.parser.html?highlight=html#module-html.parser
# Example file for parsing and processing HTML
#
#import library for html parse
from html.parser import HTMLParser
metacount=0

class MyHTMLParser(HTMLParser):
  #Handling comments ,the handle_comment(self,data) is the defualt method of from html.parse
  # but override in MyHTMLpaser sub class
  def handle_comment(self, data):
    print("Encounter Comment:",data)
    pos=self.getpos()
    print("\tAt line :",pos[0],"position",pos[1])
  """
  More Example below for better understanding
  """
  def handle_starttag(self, tag, attrs):
    global metacount
    if tag=="meta":
      metacount +=1

    print("Encounter tag:", tag)
    pos = self.getpos()
    print("\tAt line :", pos[0], "position", pos[1])
    if attrs.__len__() > 0:
      print("\Attribute:")
      for a in attrs:
        print("\t",a[0],"=",a[1])




  def handle_endtag(self, tag):
    print("Encounter tag:", tag)
    pos = self.getpos()
    print("\tAt line :", pos[0], "position", pos[1])


  def handle_data(self, data):
    if data.isspace():
      return
    print("Encounter data:", data)
    pos = self.getpos()
    print("\tAt line :", pos[0], "position", pos[1])
def main():
  # instantiate the parser and feed it some HTML
  parser = MyHTMLParser()
  f=open("samplehtml.html")
  if f.mode=='r':
    content=f.read()
    parser.feed(content)
  print(metacount)
    

if __name__ == "__main__":
  main();
  