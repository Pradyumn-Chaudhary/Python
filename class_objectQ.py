class Bank:
    def __init__(self,balance,acc_no):
        self.balance = balance
        self.acc_no = acc_no

    def debit(self,ammount):
        self.balance -= ammount
        print("Rs.",ammount,"is debited from your account")
        print("Remaining Balance is Rs.",self.balance_check())
    
    def credit(self,ammount):
        self.balance += ammount
        print("Rs.",ammount,"is credited to your account")
        print("Your Balance is Rs.",self.balance_check())

    def balance_check(self):
        return self.balance

c1 = Bank(10000,231939020)
print(c1.balance)
print(c1.acc_no)

c1.debit(2000)
c1.credit(7000)

