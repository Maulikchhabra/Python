#Syntax => dictionary={"name":"maulik","age":20}

#keys in dictionary should be single element while values can be single element or iterables.

me={"name":"maulik","age":20}
print(me)
print(type(me))

#dict() method
a=[(1,"a"),(2,"b")] #list
b={(1,"ab"),(2,"cd")} #set
c=(("a","ab"),("b","cd")) #tuple
dic1=dict(a)
dic2=dict(b)
dic3=dict(c)
print(dic1)
print(dic2)
print(dic3)

#Empty dictionary
d={}

#Accessing values
print("I am %s" %me["name"])
print("And I am %d years old" %me["age"])


#Inserting values in dictionary
#one at a time
d[0]="abcd"
d["i"]="i"
d[2]="efgh"
print(d)

#set of values in single key
d[1]=1,2,3,4,5
print(d)

#Deleting values in dictionary 
#by del keyword
print(d)
del d["i"]
del d[1]
print(d)
del dic1 #deleting whole dictionary

#by using pop() method
poppedElement =d.pop(0) #deletes entry of key 0
print(d)


#Iterating over dictionary

#for all keys
for x in dic2:
    print(x)

#for all values
for x in dic2:
    print(dic2[x])    

#for all values using values() method
for x in dic2.values():
    print(x)

#for all items in dictionary
for x in dic2.items():
    print(x)


#Built-in functions

dic2.clear() #delete all items

dic=dic3.copy() # copies the dictionary
print(dic)       

dic3.update(d) #adds key value pairs to the dictionary present in d
print(dic3)


