list1 = [1,2,3,4,5,4,3,2,1]
list2 = [ 2,3,4,5,1,6,7,8,9]

list3 = list1.copy()
list4 = list2.copy()

list3.reverse()
list4.reverse()

if(list1==list3):
    print("Yes 'list1 is palindrome'")
else:
    print("No 'list1 is not palindrome'")

if(list2==list4):
    print("Yes 'list2 is palindrome'")
else:
    print("No 'list2 is not palindrome'")

print(list3,list1,list2,list4)