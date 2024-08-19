firstName = "Pradyumn"
lastName = "Chaudhary"
str1 = "i am IronMan"

#concatenation
fullName = firstName + " " + lastName
print(fullName)

#length
print(len(fullName))

#slicing
sliceing = fullName[0:5]
print(sliceing)
print(fullName[-9:-1]) #negative indexing

#String functions
print(lastName.endswith("ary"))
print(str1.capitalize())
str2 = str1.capitalize()
print(str1.replace("a","o"))
print(str1.find("o"))
print(str2)
print(str2.count("n"))