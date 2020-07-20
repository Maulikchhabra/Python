#Syntax => tupple=(value1, value2, value3)

#Tuples are immutable and have fix lengths

#Empty tupple = ()

tup1=("maulik")
tup2=("maulik",)
print(type(tup1)) #will return string as for single element in tuple , a comma is necessar after the element
print(type(tup2)) #will return tuple

print(tup2[0]) #accessing through indexes


tup3=(1,2,3,4,5)
count=0
for i in tup3:
    print("tup3[%d]=%d"%(count,i)) #iterating through the tuple
    count=count+1

# tuple_variable[start:stop:step]

#negative indexing 
# -1 is rightmost element -2 being second last  


#Deleting tuple
del tup2

#Basic tuple operations = repetition, concatenation, membership, iteration

#Tuple in-built functions
print(len(tup3))
print(max(tup3))
print(min(tup3))
