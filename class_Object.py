# #class
# class Student:
#     name = "Anu"

# #object
# s1 = Student()
# print(s1)
# print(s1.name)

class Student:
    college = "ABC College"
    def __init__(self,fullname,marks):
        self.name = fullname
        self.marks = marks
        print("Adding new Student to Database")

s1 = Student("Anu",97)
print(s1.name,s1.marks)

s2 = Student("Pradyumn",90)
print(s2.name,s2.college)