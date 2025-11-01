# Create account class with balance & account no. Create method for debit,credit and print balance 

# Create account class with balance & account no. 
# Create method for debit, credit and print balance 

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
    
    # Debit method
    def debit(self, amount):
        self.balance -= amount
        print('Debited Rs:', amount)
        print('Total balance:', self.balance)

    # Credit method
    def credit(self, amount):
        self.balance += amount
        print('Credited Rs:', amount)
        print('Total balance:', self.balance)

    # Show balance
    def show_balance(self):
        print('Balance Rs:', self.balance)


# Creating object
acc1 = Account(200000, 100040004)

# Performing transactions
acc1.debit(1000)
acc1.credit(1000000)
acc1.credit(500000)
acc1.show_balance()