class Bank:
    bankAccounts = []
    bankName = ""

    def __init__(self, name):
        self.bankName = name

    '''add a new bank account to bankAccounts'''
    def addNewBankAccount(self, user_account):
        self.bankAccounts.append(user_account)


