from bank_account import BankAccount

class SavingsAccount(BankAccount):
    """
    A saving account that earns interest.
    """

    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        """Calculates and adds interest to the balance."""
        interest = self.balance * (self.interest_rate / 100)
        self.deposit(interest)

    def __str__(self):
        return (
          f"SavingsAccount[{self.account_holder}]"
          f"Balance: GHS {self.balance:.2f}"
          f"Rate: {self.interest_rate}%"
          )

#Deomstration
savings = SavingsAccount("Bernice Tekpor", 1500, 5)

# Two deposites
savings.deposit(300)
savings.deposit(200)

print("\nBefore Interest")
print(savings)

#Apply interest
print("\nAfter Interest")
print (savings)

#Withdrawal
print("\nMaking a Withdrawal...")
savings.withdraw(400)

print("\nFinal Account Details")
print(savings)
