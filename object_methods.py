class Student:
    @staticmethod #decorator
    def college():
        print("ABC College")

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def average(self):
        sum = 0
        for val in self.marks:
            sum += val
        return (sum)/3
    
s1 = Student("Anu",[92,97,99])
print("Hi",s1.name,"your average marks is",s1.average())
s1.college()