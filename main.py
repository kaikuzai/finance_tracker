from user import User


user_name = input("Who does this account belong to?: ")
user_start_amount = int(input(f"what is the current balance in {user_name}'s account?: "))

account_1 = User(user_name)
account_1.add_to_account(user_start_amount)

account_1.give_name()
account_1.total_amount()
