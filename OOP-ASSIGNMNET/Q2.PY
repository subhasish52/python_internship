class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance is {self.balance}.")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")
    
    def get_balance(self):
        return self.balance
account1 = BankAccount("1459010001976", "SUBHASISH", 10000)
account1.deposit(500)      
account1.withdraw(200)   
print(account1.get_balance()) 
