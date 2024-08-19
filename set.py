collection1 = {1,2,3,3,3,3,4,5,4,5,6,7,"Hello"}
print(type(collection1))
print(collection1)
print(len(collection1))

#empty set
collection2 = set()
print(collection2)

#set methods
collection2.add(9)
collection2.add(57)
collection2.add("PD")
collection2.add((2,3,5,"Pradyumn"))
print(collection2)

collection1.remove(3)
print(collection1)

collection2.clear()
print(collection2)
print(len(collection2))

print(collection1.pop())
print(collection1.pop())


set1 = {1,2,3,4,5,6,7,}
set2 = {0,9,8,7,6,5,}

print(set1.union(set2))
print(set2.intersection(set1))