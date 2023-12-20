class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def make_deposit(self, amount):
        self.balance += amount

    def make_withdrawal(self, amount):
        self.balance -= amount

    def display_user_balance(self):
        print("User:", self.name, "Balance: $", self.balance)

    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.make_deposit(amount)
        
user1 = User("Guido van Rossum", 0)
user2 = User("Linus Torvalds", 0)
user3 = User("Larry Page", 0)

user1.make_deposit(100)
user1.make_deposit(200)
user1.make_deposit(50)
user1.make_withdrawal(75)
user1.display_user_balance()

user2.make_deposit(500)
user2.make_deposit(1000)
user2.make_withdrawal(200)
user2.make_withdrawal(300)
user2.display_user_balance()

user3.make_deposit(1000)
user3.make_withdrawal(200)
user3.make_withdrawal(100)
user3.make_withdrawal(50)
user3.display_user_balance()

user1.transfer_money(user3, 100)
user1.display_user_balance()
user3.display_user_balance()

