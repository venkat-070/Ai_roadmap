class BankAccount:
    def __init__(self,owner,balance = 0):
        self.owner = owner
        self.balance = balance
    def show_balance(self):
        print("Account owner: "+self.owner+" | Balance: "+str(self.balance))
class SavingsAccount(BankAccount):
    def __init__(self,owner,balance,interest_rate = 2.5):
        super().__init__(owner,balance)
        self.interest_rate = interest_rate
    def add_interest(self):
        self.balance += self.balance*(self.interest_rate*0.01)
        self.show_balance()
acc1 = SavingsAccount("ravi",5000)
acc1.show_balance()
acc1.add_interest()


    

