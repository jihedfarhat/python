class User:
    def __init__(self, name):
        self.name = name
        self.account = BankAccount()

    def make_deposit(self, amount):
        self.account.deposit(amount)

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)

    def display_user_balance(self):
        print(f"User: {self.name}, Account Balance: ${self.account.balance}")

    def transfer_money(self, other_user, amount):
        self.account.withdraw(amount)
        other_user.account.deposit(amount)


class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5

    def display_account_info(self):
        print(f"Balance: ${self.balance}")

    def yield_interest(self):
        if self.balance > 0:
            interest = self.balance * self.int_rate
            self.balance += interest


user1 = User("Guido van Rossum")
user2 = User("John Doe")

user1.make_deposit(1000)
user1.make_withdrawal(200)
user1.display_user_balance()

user2.make_deposit(500)
user2.make_withdrawal(100)
user2.display_user_balance()

user1.transfer_money(user2, 300)
user1.display_user_balance()
user2.display_user_balance()