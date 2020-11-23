from modules.bank_account import *

# account = {
#     "holder_name": "John",
#     "balance": 500,
#     "type": "business account"
# }

# print(get_account_name(account))


bank_account = BankAccount("John", 500, "Business")
bank_account_2 = BankAccount("Jimmy", 600, "Personal")
print(bank_account.holder_name)

bank_account.holder_name = "Jamie"

print(bank_account.holder_name)


bank_account.pay_in(50)

print(bank_account.balance)
print(bank_account_2.balance)

bank_account.pay_monthly_fee()
bank_account_2.pay_monthly_fee()

print(bank_account.balance)
print(bank_account_2.balance)
