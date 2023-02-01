class BankAccount:
    accounts=[]

    def __init__(self, int_rate): 
        self.int_rate = int_rate
        self.balance = 0
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
    
account1=BankAccount(0.05)
account2=BankAccount(0.02)
account1.deposit(50).deposit(100).deposit(150).withdraw(200).yield_interest()
account2.deposit(50).deposit(50).withdraw(200).yield_interest()
BankAccount.accounts.append(account1)
BankAccount.accounts.append(account2)
BankAccount.display_info()