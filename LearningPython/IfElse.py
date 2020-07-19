num =int(input("Enter a number :"))

if num%2==0:
    print("Number is even.") #simple if statement


if num>=18:
    print("Greater than or equal to voting age.")
else:
    print("Less than voting age.") #if-else statement


if num==18:
    print("Equal to voting age.")
elif num>18:
    print("Greater than voting age.")
else:
    print("Less than voting age.")  #if-else with elif


if num>18:
    if num<36:
        print("Greater than 18, less than 36")              
