# every class made has at leat one argument... Self
# when defining functions in a class, you are createing
# methods that can be called against instances of that class.

# a class is a blueprint and
#  an object is an instance of a class
class BankAccount:
    def __init__(self, holder_name, balance, type):
        self.holder_name = holder_name
        self.balance = balance
        self.type = type
        self.__rates = {        # double underscore hides the
                                # information from the user.
            "Personal": 10,
            "Business": 50
        }

    def pay_in(self, amount):
        self.balance += amount

    def pay_monthly_fee(self):
        self.balance -= self.__rates[self.type]

        # if self.type == "Business":
        #     self.balance -= 50
        # elif self.type == "Personal":
        #     self.balance -= 10
