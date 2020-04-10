class Account:
    def __init__(self, account_name, initial_balance):
        self.account_name = account_name
        self.balance = initial_balance

    def getBalance(self):
        return self.balance

    def getAccountName(self):
        return self.account_name

    def addBalance(self, amount):
        self.balance = self.balance + amount

    def decreaseBalance(self, amount):
        self.addBalance(-amount)
