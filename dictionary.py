#dictionary
dict = {
    "name" : "Anu Kuntal",
    "class" : "A1",
    "marks" : [97,93,92,69,18,]
}

print(type(dict))
print(dict)
print(dict["marks"])

dict["class"] = "A++"
dict["standard"] = 2
print(dict)

null_dict = {}
print(null_dict)

#Nested Dictionary
student = {
    "name" : "Pradyumn Chaudhary",
    "subject" : {
     "phy" : 95,
     "chem" : 89,
     "maths" : 42,  
    }
}

print(student)
print(student["subject"])
print(student["subject"]["chem"])

#dictionary_methods
print(student.keys())
print(student.values())
print(dict.items())
print(student.get("subject"))

dict.update(student)

print(dict)