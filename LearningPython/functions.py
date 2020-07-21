#Syntax =>
#   def funName(args):
#     statements to be executed
#     return statement

def hello():
    return "hello there"

str=hello()
print(str)    


def fun(i):
    i=i+10
    print(i)

fun(5)


#Default arguments
def me(age,name="maulik"): #default arguments only come in right side
    print("My name is",name,"and I am ",age,"years old.")

me(20)    
me(15,"john") #overwriting default argument


#variable arguments
def people(*ppls):
    for ppl in ppls:
        print(ppl)
    print(ppls)  #printing all arguments  

people("john","smith","mark","june")


#Keyword arguments

def func(**kwargs):
    print(kwargs)

func(a=1)
func(a=1,b=2,c=3) 


def arithm(a,b,c):
    c=a+b/c
    print(c)

arithm(c=2,b=10,a=1)
arithm(a=1,b=10,c=2)    