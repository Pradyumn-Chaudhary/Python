class Student:
    def __init__(self,phy,chem,maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths

    # def calculate_percentage(self):
    #     self.percentage = str((self.phy+self.chem+self.maths)/3) + "%"
    #     print(self.percentage)

    @property
    def percentage(self):
        return str((self.phy+self.chem+self.maths)/3) + "%"
        

S1 = Student(91,89,93)
# S1.calculate_percentage()
print(S1.percentage)