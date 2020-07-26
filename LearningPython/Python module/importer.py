import file #syntax for import (imports whole file)
name=input("Enter your name: ")
file.display(name)


from file import multiply #syntax for from inport (imports specific part of file)
#It can also be used as to import all attributes=> from file import * 
res=multiply(5,2)
print(res)


#Renaming a module 
import file2 as hello


#dir() method
list1=dir(file)
print(list1)


#reload() method
#reload(hello)
