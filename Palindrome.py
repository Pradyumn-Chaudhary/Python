list1 = [1,2,3,"abc",3,2,1]
list2 = list1.copy()
list2.reverse()
print(list1)
print(list2)

count = 0

for el in list1 :
    if el!=list2[count]:
        print(el,list2[count])
        print("Not Palindrome")
        break
    count+=1
else:
    print("Polindrome")