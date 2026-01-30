class Account():
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, dep_amt):
        self.balance = self.balance + dep_amt
        print(f"Added {dep_amt} to your account.")

    def withdraw (self, wd_amt):
        if self.balance >= wd_amt:
            self.balance = self.balance - wd_amt
            print("Withdrawl successful.")
        else:
            print("Sorry, not enough funds.")
    def __str__(self):
        return f"owner: {self.owner} \nBalance: {self.balance}"
a = Account("Suroop", 5000)
print("Account owner name is:",a.owner)
print("Owner account balance is:",a.balance)
a.deposit(1000)
print("Now, Owner account balance is:",a.balance)
      
