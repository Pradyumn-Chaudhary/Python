class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    
    def print_num(self):
        print(self.real,"i +",self.img,"j")

    # def add(self,num):
    #     self.real += num.real
    #     self.img += num.img
    #     return Complex(self.real,self.img)

    def __add__(self,num):                   #Dunder Function
        self.real += num.real
        self.img += num.img
        return Complex(self.real,self.img)
    
    def __sub__(self,num):                   
        self.real -= num.real
        self.img -= num.img
        return Complex(self.real,self.img)


num1 = Complex(3,8)
num1.print_num()

num2 = Complex(1,4)
num2.print_num()

# num3 = num1.add(num2)
# num3.print_num()

num3 = num1 + num2
num3.print_num()

num4 = num3-num2
num4.print_num()