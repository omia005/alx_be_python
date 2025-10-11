Class BankAccount :
   def __init__(self, account_balance=0):
     self.account_balance = account_balance

   def deposit(self,amount):
     if amount > 0:
            self.account_balance += amount
            return True
        else:
            print("Error: Deposit amount must be positive.")
            return False
     def withdraw(self, amount):
        if amount <= 0:
            print("Error: Withdrawal amount must be more than zero.")
            return False
        elif amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            print("Error: Insufficient funds for withdrawal.")
            return False

     def display_balance(self):
       print(f"Current balance: ${self.account_balance:.2f}")
     
