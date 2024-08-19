class Student:
    def __init__(self,name):
        self.name = name

s1 = Student("Shradha")
print(s1.name)
print(s1)

#dell keyword

# del s1.name #delete object attribute
# print(s1.name)
# print(s1)

del s1 #delete object
print(s1)