if __name__ == '__main__':
    N = int(input())
    
list1=[]

for i in range(0,N):
    str=input().split()

    for i in range(1,len(str)):
        str[i]=int(str[i])

    if str[0]=="append":
        list1.append(str[1])
    elif str[0]=="remove":
        list1.remove(str[1])
    elif str[0]=="print":
        print(list1)
    elif str[0]=="insert":
        list1.insert(str[1],str[2])
    elif str[0]=="sort":
        list1.sort()
    elif str[0]=="extend":
        list1.extend(str[1:])
    elif str[0]=="pop":
        list1.pop()
    elif str[0]=="reverse":
        list1.reverse()
    elif str[0]=="count":
        print(list1.count(str[1]))
    elif str[0]=="index":
        print(list1.index(str[1]))                                   
