class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdrawal(self, amount):
        self.balance -= amount
        return self

    def display_user_balance(self):
        print("User:", self.name, "Balance: $", self.balance)
        return self

    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.make_deposit(amount)
        return self
      
user1 = User("Guido van Rossum", 0)

user1.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()