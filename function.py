def calc_sum(a,b):
    return a+b

print(calc_sum(3,8))

def cal_fact(n):
    i = 1
    fact = 1
    while i<=n:
        fact = fact*i
        i+=1
    print(fact)

cal_fact(int(input("Enter n : ")))

def odd_Even(n):
    if(n%2==0):
        print("Even")
    else:
        print("Odd")

odd_Even(int(input("Enter Number : ")))