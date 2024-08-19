list = [1,2,3,4,5,6,7]
count = 0
while count<len(list):
    print(list[count])
    count+=1


tuple = (3,8,6,9,0,5,1,5,0,9)
count = 0
while count<len(tuple):
    if(tuple[count]==0):
      print("Found at index",count)
      break
    count+=1

count = 0
while count<len(tuple):
   if(tuple[count]==0):
      count+=1
      continue
   print(tuple[count])
   count+=1
   

str = "Python"

for num in str:
    print(num)
else:print("End")

list1 = [1,4,9,16,25,36,49,64,81,100]
tuple1 = (1,4,9,16,25,36,49,64,81,100)
for el in list1:
    print(el)

for el in tuple1:
    if(el==49):
        print("Found at index",tuple1.index(49))
        break
else:
    print("The element doen't exists")

range
n = 7
seq = range(9,450,56)
for i in seq:
    print(i)


"""
Pass - Pass is a null statement that does nothing.
Pass is used as a placeholder for future code
#for i in range:
    pass

print("Passed")
"""