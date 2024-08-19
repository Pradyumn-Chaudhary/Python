def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)

print(fact(int(input("Enter n : "))))


def sum(n):
    if(n==1):
        return 1
    else:
        return n + sum(n-1)
    
print(sum(int(input("Enter n : "))))


def listed(list,n=0):
    if(n==len(list)):
        return
    print(list[n],end=" ")
    listed(list,n+1)

list = ["Hi","Hello",93,50,0.43,"Bye"]
listed(list)

