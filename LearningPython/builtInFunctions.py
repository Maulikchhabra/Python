# abs() => return absolute value of the argument

print(abs(21-1.5))
print(abs(-1.25))
print(abs(3-4j)) #magnitude of the complex is returned

# all() => return True if all passed iterable are true and false otherwise, return True on empty iterables

print(all([1,2,3])) #all true
print(all([0,False])) #0 and False are false
print(all([1,True,0,24])) #0 is false

#any() => return true if any item in iterable is true

print(any([1,2,3]))
print(any([0]))
print(any([False,True]))

#bin() => return binary value of given argument with prefix 0b.

print(bin(10))
print(bin(5))

#bool() => converts value to boolean, false if value is ommited or false and true if value is true

print(bool([]))
print(bool([1]))
print(bool(None))
print(bool("maulik"))

#callable() => return true is object is callable otherwise false

a=5
def fun():
    b=25
    print(b)

print(callable(a))
print(callable(fun))

#exec() => dynamic execution of program

exec('print(a==5)')
exec('print(a+10)')  

#sum() => get the sum of numbers in an iterable

l=[2,4,6,8]
print(sum(l))
print(sum(l,20)) #sum of l + other argument

#eval() => parses the expression passed to it ,runs python expression

print(eval('a+2'))

#float() => returns floating point number from a number or string

print(float(10))
print(float(2.5))
print(float("22.22"))

#format() => returns formatted representation of value

print(format(123,"d")) #d=int
print(format(125,"f")) #f=float
print(format(10,"b")) #b=binary