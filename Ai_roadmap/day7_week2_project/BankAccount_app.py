class BankAccount:
    def __init__(self,owner,balance = 0):
        self.owner = owner
        self.balance = balance
    def check_balance(self):
        print("\nAccount owner: "+self.owner)
        print("Current Balance: "+str(self.balance)+"\n")
    def deposit(self,amount):
        self.balance += amount
        print(str(amount)+" Sucessfully Deposited ")
        self.check_balance()
    def withdraw(self,amount):
        if(self.balance >= amount):
            self.balance -= amount
            print("\n"+str(amount)+" Credited sucessfully..\n")
        else:
            print("\nInsufficient funds..\n")
        self.check_balance()
    def __str__(self):
        return "Account owner: "+self.owner+" | balance: "+str(self.balance)
name = input("Enter your name: ")
acc = BankAccount(name)
while True:
    print("1. Deposit\n2. Withdraw\n3. check balance\n4. Exit")
    x = input("\nselect an option: ")
    if x == "1":
        amt = float(input("Enter amount: "))
        acc.deposit(amt)
    elif x == "2":
        amt = float(input("Enter amount: "))
        acc.withdraw(amt)
    elif x == "3":
        acc.check_balance()
    elif x == "4":
        print("Thank you for using our bank account.")
        break
    else:
        print("Invalid input")
print(acc)
        