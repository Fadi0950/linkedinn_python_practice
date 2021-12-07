# 
# Example file for parsing and processing XML
#for working with xml you need module import xml.dom.minidom
import xml.dom.minidom

def main():

  # use the parse() function to load and parse an XML file
  doc=xml.dom.minidom.parse("samplexml.xml")


  
  # print out the document node and the name of the first child tag
  print(doc.nodeName)
  print(doc.firstChild.tagName)

  
  # get a list of XML tags from the document and print each one
  skills=doc.getElementsByTagName("skill")
  print("%d skill" % skills.length)
  for i in skills:
    print(i.getAttribute("name"))


    
  # create a new XML tag and add it into the document
  newSkills=doc.createElement("skill")
  newSkills.setAttribute("name","jQuery")
  doc.firstChild.appendChild(newSkills)

  skills = doc.getElementsByTagName("skill")
  print("%d skill" % skills.length)
  for i in skills:
    print(i.getAttribute("name"))



  

if __name__ == "__main__":
  main()

