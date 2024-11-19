class BankAccount:
    bank_name = "Tech4Girls Bank"
    

    def __init__(self, account_holder):
        self.account_holder = account_holder  
        self.balance = 0 
    
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    
    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"{amount} withdrawn. New balance: {self.balance}")
            else:
                print("Insufficient balance to withdraw the requested amount.")
        else:
            print("Withdrawal amount must be positive.")
    
    
    @staticmethod
    def bank_policy():
        print("At Tech4Girls Bank, we prioritize our customers satisfaction, safety and financial security.")
    

    @classmethod
    def get_bank_name(cls):
        return cls.bank_name


account1 = BankAccount("Akua")
account2 = BankAccount("Babs")


account1.deposit(500)
account1.withdraw(200)

account2.deposit(1000)
account2.withdraw(500)


BankAccount.bank_policy()

