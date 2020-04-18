from atm.Bank import Bank
from atm.Screen import Screen


class ATM:
    def __init__(self, bank):
        self.bank = bank  # initialize bank
        self.card = None
        self.bankAccount = None
        self.screen = Screen()
        self.attempts = 0
        self.maxAttempts = 2

    def validateCard(self):
        found_account = self.findMatchingAccount(self.card.getCardNumber())

        # check to see if the account has been found
        if found_account is not None:
            self.bankAccount = found_account
        else:
            raise Exception('There is no account associated with debit card.')

    def insertCard(self, inserted_card):
        self.card = inserted_card
        self.attempts = 0

    ''' this method searches through bank accounts and returns the account if found '''

    def enterPin(self, pin_number):
        if self.attempts < self.maxAttempts:
            if self.bankAccount.getPinNumber() == pin_number:
                return True
            else:
                self.screen.displayAttemptsRemaining(str(self.maxAttempts - self.attempts))
                self.attempts = self.attempts + 1
                return False
        raise Exception('You have exceeded the maximum number of attempts.')

    def findMatchingAccount(self, user_account_card_id):
        for account in self.bank.bankAccounts:
            if account.getCardID() == user_account_card_id:
                return account

    def options(self, number):
        if number == 0:
            print('depositing funds')
            return True
        elif number == 1:
            self.callWithdrawal()
            return True
        elif number == 2:
            self.screen.displayAccountsList(self.bankAccount.user_accounts_list)
            self.screen.displayPromptAccountName()
            account_name = input()
            answer = self.callDisplayBalance(account_name)
            self.screen.displayBalance(answer)
            return True
        elif number == 3:
            print('transferring funds')
            return True
        else:
            self.screen.displayExitMessage()
            return False

    def callWithdrawal(self):
        self.screen.displayAccountsList(self.bankAccount.user_accounts_list)
        self.screen.promptWithdrawQuestion()
        answer = input()

        for account in self.bankAccount.user_accounts_list:
            if account.getAccountName() == answer:
                self.screen.displayAskWithdrawal()
                decreaseBal = input()
                while int(decreaseBal) > account.getBalance():
                    self.screen.displayOverWithdrawal()
                    decreaseBal = input()
                self.screen.displayWithdrawalMessage(decreaseBal)
                account.decreaseBalance(int(decreaseBal))

    def callDisplayBalance(self, account_name):
        account_name = account_name.lower()
        return self.bankAccount.getAccountBalance(account_name)
