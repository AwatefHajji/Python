class BankAccount:
    accounts=[]

    def __init__(self, int_rate): 
        self.int_rate = int_rate
        self.balance = 0
        BankAccount.accounts.append(self)
    def deposit(self, amount):
        self.balance+=amount
        return self
    
    def withdraw(self, amount):
        if(amount <= self.balance):
            self.balance-=amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance-= 5
        return self
    
    def display_account_info(self):
        print(f"Balance: {self.balance}")
    def yield_interest(self):
        if(self.balance>0):
            self.balance += (self.balance * self.int_rate)
        return self
    @classmethod
    def display_info(cls):
        for account in cls.accounts:
            print(f"Balance: {account.balance} \n interest rate : {account.int_rate}")
    

# account1 = BankAccount(.05)
# account2 = BankAccount(.02)

# account1.deposit(10).deposit(2000).deposit(40).withdraw(600).yield_interest().display_account_info()
# account2.deposit(100).deposit(2000).deposit(400).withdraw(60).yield_interest().display_account_info()

# BankAccount.display_info()