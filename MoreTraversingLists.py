def linearsearch(k,lst):
    for val in lst:
        if k==val:
            return True
    else:
        return False

n=int(input("Enter Number:"))
l=[(input("Enter element")) for i in range(0,n)]
key=int(input("Enter key:"))
res=linearsearch(key,l)