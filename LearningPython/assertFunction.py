#assert keyword is used for debugging of the code.

#Example 1
def avg(nums):
    assert len(nums)!=0,"List empty!"
    return sum(nums)/len(nums)

nums1=[1,2,3,4,5]
print("Result: ",avg(nums1))

nums2=[]
print("Result: ",avg(nums2))

#Example 2
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))

print("Result: ")
assert b!=0, "Divide by 0"
print(a/b)