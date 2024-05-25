class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount:.2f}")
        print(f"Balance: ${self.balance:.2f}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}")
            print(f"Current Balance: ${self.balance:.2f}")
    def get_balance(self):
        return self.balance
    def __str__(self):
        return f"Account Holder: {self.account_holder}, Balance: ${self.balance:.2f}"
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        print(f"Interest: ${interest:.2f}")
        print(f"New Balance: ${self.balance:.2f}")

    def __str__(self):
        return f"Account Holder: {self.account_holder}, Balance: ${self.balance:.2f}, Interest Rate: {self.interest_rate}%"
bushra = BankAccount("1519", "bushra")
bushra.deposit(1000)
bushra.withdraw(500)
print(bushra)
b = SavingsAccount("1519", "bushra", 10)
b.deposit(150)
b.apply_interest()
print(b)
