from atm.Account import Account

'''Saving Accounts have interest rates. There can be multiple saving accounts. '''


class Savings(Account):
    def __init__(self, account_name, initial_balance, interest_rate):
        super().__init__(account_name, initial_balance)
        self.account_name = account_name
        self.balance = initial_balance
        self.interest_rate = interest_rate
