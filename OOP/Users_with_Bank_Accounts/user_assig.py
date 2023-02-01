from bank_account_assig import BankAccount
class User:
    def __init__(self,user_first_name,user_last_name,user_email,user_age):
        self.first_name = user_first_name
        self.last_name = user_last_name
        self.email = user_email
        self.age = user_age
        self.account= BankAccount(0.02)
    
    def display_info_user(self):
        print(f"Name: {self.first_name} {self.last_name}\n Email: {self.email}\n Age:{self.age}\n with balance = {self.account.balance}")
    def make_deposite(self,amount):
        self.account.deposit(amount)
        print(f"{self.first_name} has an account with balance ={self.account.balance}")
    def make_withdraw(self, amount):
        self.account.withdraw(amount)
    def display_user_balance(self):
        self.account.display_account_info(self)

user1=User("Asma","Neji","asma@live.fr",25)
user1.make_deposite(1000)
user1.make_withdraw(200)
user1.display_info_user()





