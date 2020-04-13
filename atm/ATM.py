from atm.Bank import Bank
from atm.Screen import Screen


class ATM:
    def __init__(self, bank):
        print('initializing atm')
        self.bank = bank  # initialize bank
        self.card = None
        self.bankAccount = None
        self.screen = Screen()
        self.attempts = 0
        self.maxAttempts = 2

    def validateCard(self):
        print('validating card')
        found_account = self.findMatchingAccount(self.card.getCardNumber())

        # check to see if the account has been found
        if found_account is not None:
            self.bankAccount = found_account
        else:
            raise Exception('There is no account associated with debit card.')

    def insertCard(self, inserted_card):
        print('inserting card')
        self.card = inserted_card
        self.attempts = 0

    ''' this method searches through bank accounts and returns the account if found '''

    def enterPin(self, pin_number):
        if self.attempts < self.maxAttempts:
            if self.bankAccount.getPinNumber() == pin_number:
                return True
            else:
                self.attempts = self.attempts + 1
                return False
        raise Exception('You have exceeded the maximum number of attempts.')

    def findMatchingAccount(self, user_account_card_id):
        for account in self.bank.bankAccounts:
            if account.getCardID() == user_account_card_id:
                return account

    def Options(self, number):
        if number == 0:
            print('depositing funds')
            return True
        elif number == 1:
            self.callWithdrawal()
            print('withdrawing funds')
            return True
        elif number == 2:
            print('displaying balance')
            return True
        elif number == 3:
            print('transferring funds')
            return True
        else:
            self.screen.displayExitMessage()
            return False

    def callWithdrawal(self):
        print("Withdrawal that money")
