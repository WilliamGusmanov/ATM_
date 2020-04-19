from atm.Account import Account

''' checking is different from savings. 
    There can only be one checkings account - will be satisfied by using Singleton Pattern.'''


class Checking(Account):
    _instance = None

    def __init__(self, account_name, initial_balance):
        super().__init__(account_name, initial_balance)
        self.account_name = account_name
        self.balance = initial_balance
        if Checking._instance is not None:
            raise Exception('there can only be one checking account.')
        else:
            Checking._instance = self
