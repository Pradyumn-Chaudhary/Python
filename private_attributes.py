class Account:
    def __init__(self,acc_no,acc_pw):
        self.acc_no = acc_no
        self.__acc_pw = acc_pw #can change any attribut to private by adding 2 underscore(__) in starting 

    def __hello(self):         #private method
        print("Hello",self.name)
    
    def welcome(self,name):
        self.name = name
        self.__hello()

    def show_pw(self):
        print("Password :",self.__acc_pw)

c1 = Account("12345","abcde")
# print(c1.acc_no,"\n",c1.__acc_pw)   #not working outside the class as it private
#c1.__hello()                         #not working outside the class as it private

c1.welcome("Shradha")
c1.show_pw()