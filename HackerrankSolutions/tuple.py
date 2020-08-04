if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

tup1=tuple(integer_list)
#print(tup1)
print(hash(tup1))    