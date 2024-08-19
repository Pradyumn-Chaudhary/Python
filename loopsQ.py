i = 0
sum = 0
n = int(input("Enter n :"))
while i<=n:
    sum = i+sum
    i+=1
print("Sum of",n,"numbers is :",sum)

m = int(input("Enter m :"))
Q = range(1,m+1)
fact = 1
for i in Q:
    fact = i*fact
print("Factorial of",m,"is :",fact)