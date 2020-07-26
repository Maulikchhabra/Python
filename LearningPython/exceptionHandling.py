def div(a,b):
    c=a/b
    print(c)

try:
    a=input("First no: ")
    b=input("Second no: ")
    div(a,b)

except:
    print("Cannot divide by 0")


#We can also use else with try-except if no except works
try:
    a=5
    b=2
    div(a,b)

except:
    print("Cannot divide by 0")

else: print("Else block")    


#Except block with exception
try:
    a=5
    b=0
    div(a,b)

except Exception as e:
    print("Cannot divide by 0")
    print(e)

else: print("Else block") 


#Multiple exceptions
try:
    a=5
    b=0
    div(a,b)

except (ArithmeticError, IOError):
    print("Arithmetic")
    

#finally block   
try:
    a=5
    b=0
    div(a,b)

except Exception as e:
    print("Cannot divide by 0")
    print(e)

else: print("Else block")

finally: print("Always works")


#Raise exceptions
#type1
try:
    age=input("Enter age: ")
    if(age<18):
        raise ValueError
    else:
        print("Vote")
except ValueError: print("Age not valid!")        

#type2
try:
    age=input("Enter age: ")
    if(age<18):
        raise ValueError("Invalid age!")
    else:
        print("Vote")
except ValueError as e: print(e)


#Custom exceptions
