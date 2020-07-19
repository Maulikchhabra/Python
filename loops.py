#FOR LOOP

#Simple For loop

str="Maulik Chhabra"
for i in str:
    print(i)

list=[1,5,10,15,20]
for i in list:
    print(5*i)    


#For loop using range()
#Syntax of range is range(start,stop,step size)

for i in range(5):
    print(i)    

for i in range(0,10,2):
    print(i)    


#Nested for loop

for i in range(0,10,2):
    for j in range(1,10,2):
        print(i-j)


#For loop and else statement

for i in range(0,6):
    print(i)
else:
    print("Number over.")    


#WHILE LOOP   

#simple while loop

i=10
while(i<=15):
    print(i)
    i=i+1


#infinite while loop
#while(1):
#  print(1)   


#while loop and else statement

while(i<=15):
    print(i)
    i=i+1
else:
    print("Number over.")    