class BankAccount:
    accounts = []

    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate * balance
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            self.balance -= 5
            print("INSUFFICIENT FUNDS: Charging a $5 fee")
        return self

    def display_account_info(self):
        print("Balance:" + " $" + str(self.balance))
        return self

    def yield_interest(self):
        self.balance += self.int_rate
        return self


# Create a User class that has an association with the BankAccount class.
# You should not have to change anything in the BankAccount class.


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.checking = self.create_account_checking()

    def create_account_checking(self):
        self.checking = BankAccount(int_rate=0.01, balance=0)
        return self.checking

    def create_account_checking(self):
        self.savings = BankAccount(int_rate=0.03, balance=1000)
        return self.savings

    def deposit_checking(self, amount):
        self.checking.deposit(amount)
        return self

    def deposit_savings(self, amount):
        self.savings.deposit(amount)
        return self

    def withdrawal_checking(self, amount):
        self.checking.withdraw(amount)
        return self

    def withdrawal_savings(self, amount):
        self.savings.withdraw(amount)
        return self

    def display_user_balance_checking(self):
        self.checking.display_account_info()
        return self

    def display_user_balance_savings(self):
        self.savings.display_account_info()
        return self

    def transfer_funds(self, amount, person):
        self.checking.withdraw(amount)
        person.checking.deposit(amount)
        return self


user1 = User(name="user1", email="user1@email.com")
user1.deposit_checking(100)
user1.display_user_balance_checking()

user2 = User(name="user2", email="user2@email.com")
user1.transfer_funds(200)
