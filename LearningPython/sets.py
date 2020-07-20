#Syntax => set={val1,val2,val3}

days={"Mon","Tue","Wed","Thurs","Fri","Sat","Sun"}

print(type(days))
print(days)

list=[1,2,3,4,5]
setList=set(list) #convert any other data structure into sets 
print(setList)


#Heterogenous
set1={True,"abc",12} #with immutable elements
print(set1)

#set2={12,25,[1,2,3]} with mutable elements (GIVES ERROR)


#Empty set creation
set2={} #will create empty dictionary so incorrect
set3=set() #will correct empty set


#Duplicate elements
set3={1,2,2,3,3,4}
print(set3)


#Insertion into set
setList.add(6) #add() function inserts the element to the set
print(setList)

setList.update({7,8,9,10}) #update() function inserts more than one element to the set
# update function requires argument as an iterable like list,set ,dictionary
print(setList)


#Deletion on set
# discard() and remove() methods
#if item to be deleted is not present in set ,discard() does nothing while remove() throws error.

setList.discard(10)
setList.discard(15)
print(setList)

setList.remove(9)
#setList.remove(16) throws error as it is not in set
print(setList)

#pop() method can also be used which generally eliminates last element but do not work properly in case of unsorted sets.
setList.pop()
print(setList)

setList2={2,1,5,3,7} #unsorted set
setList2.pop()
print(setList2)

#clear() method entirely empties the set removing all element
setList2.clear()
print(setList2)


#Set operations
a={1,2,3,4}
b={4,5,6}

#Union of two sets (|)
print(a|b) #union operation
print(a.union(b)) #union() method

#Intersection of two sets (&)
print(a&b) #intersection operation
print(a.intersection(b)) #intersection() method

#Intersection-update => removes the items from original set that are not present in both sets
c={1,2,3,4,5}
d={4,5,6,7,8}
c.intersection_update(d) #will delete all elements except 4 and 5
print(c)

#Difference of two sets
print(a-b) #difference operator
print(a.difference(b)) #difference() method

#Symmetric difference (^) => delete the common part of both the sets and merge the else
print(a^b) #symmetric operator
print(a.symmetric_difference(b)) #symmetric difference method()


#Set comparisons
e={1,2,3,4}
f={2,4}
print(e>f)
print(e<f)
print(e==f)


#Frozen sets (cam't be altered by add or remove functions as these sets are immutable.)
froze1=frozenset(a) #passing only iterables as arguments
print(type(froze1)) 
print(froze1)



