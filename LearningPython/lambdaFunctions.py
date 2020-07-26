#Syntax => lambda arguments: expression

x= lambda a: a+a/10
print(x)
print("Result =",x(20))

y= lambda a,b: a*b
print("Result =",y(2,5))


#lambda fn with filter()
list1=[10,22,37,41,100,123,29]
odd=list(filter(lambda x:(x%3==0),list1))
print(odd)


#lambda fn with map()
list2=[10,20,30,40]
squared=list(map(lambda x: x**2, list2))
print(squared)