class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def make_withdrawal(self, amount):
        self.balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.balance}")

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.balance += amount


user1 = User("Guido van Rossum", 150)
user2 = User("John Doe", 100)

user1.make_withdrawal(50)

user1.display_user_balance()
user2.display_user_balance()

user2.transfer_money(user1, 25)

user1.display_user_balance()
user2.display_user_balance()




