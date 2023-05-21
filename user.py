
class User:
    """"In this class we declare all the methods related to an inidividual unique user"""

    def __init__(self, name, amount=0):
        self.name = name 
        self.amount = amount

    def give_name(self):
        print(self.name)

    def total_amount(self):
        print(self.amount)

    def  add_to_account(self, amount):
        self.amount += amount
        # print(f"{self.name} now has {self.total_amount()} in their account")
