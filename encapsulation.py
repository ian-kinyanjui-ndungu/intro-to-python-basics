class BankAccount:
    def __init__(self,owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance+=amount
        print(f"you have deposited {amount} new balance is {self.balance}")

    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
        else:
            print(f"you cant withdraw {amount} due to insufficient funds your account balance is {self.balance}")

    def check_balance(self):
        return self.balance

#object
account=BankAccount("nyanjui", 100)
account.deposit(100)
account.check_balance()
account.withdraw(300)

print("Balance", account.check_balance())