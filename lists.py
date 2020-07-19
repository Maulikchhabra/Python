list=[1,2,3,4,5]

#syntax = list_variable(start:stop:step)

print(list)
print(list[1]) #accessing the element at index 1
print(list[1:]) #starting from index 1
print(list[1:4]) #start at 1 end at 4
print(list[:]) #whole list
print(list[0:5:2]) #start at 0 end at 5 step size=2

list1=[1,2,3]
list2=["a","b","c"]

print(list1+list2) #concatenation
print(list1*2) #repetition
print(3 in list1) #membership
print(len(list1+list2)) #length operator


#iterations
for i in list:
    print(i)


#user inputs
#a=input("Enter an alphabet: ")
#list2.append(a) #insert in the list
print(list2)   

list.remove(4) #removing element 4 from list
print(list)


#List built in functions

print(len(list)) #length of list
print(max(list)) #max value in list
print(min(list)) #min element in list
