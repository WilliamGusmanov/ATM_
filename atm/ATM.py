import datetime

from atm.Bank import Bank
from atm.BankAccount import BankAccount
from atm.Card import Card
from atm.Checking import Checking
from atm.Savings import Savings
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
            self.callDeposit()
            return True
        elif number == 1:
            self.callWithdrawal()
            return True
        elif number == 2:
            self.callDisplayBalance()
            return True
        elif number == 3:
            self.callTransferFunds()
            return True
        else:
            self.screen.displayExitMessage()
            return False

    def callWithdrawal(self):
        self.screen.displayAccountsList(self.bankAccount.user_accounts_list)
        self.screen.promptWithdrawQuestion()
        answer = input().lower()

        for account in self.bankAccount.user_accounts_list:
            if account.getAccountName() == answer:
                self.screen.displayAskWithdrawal()
                decreaseBal = input()
                while int(decreaseBal) > account.getBalance():
                    self.screen.displayOverWithdrawal()
                    decreaseBal = input()
                self.screen.displayWithdrawalMessage(decreaseBal)
                account.decreaseBalance(int(decreaseBal))
                return
        self.screen.displayAccountNotFound(answer)

    def callDisplayBalance(self):
        self.screen.displayAccountsList(self.bankAccount.user_accounts_list)
        self.screen.displayPromptAccountName()
        account_name = input().lower()
        account_name = account_name.lower()

        for account in self.bankAccount.user_accounts_list:
            if account.getAccountName() == account_name:
                amount = account.getBalance()
                message = "" + account_name + " has $" + str(amount)
                self.screen.displayBalance(message)
                return
        self.screen.displayAccountNotFound(account_name)

    def callDeposit(self):
        self.screen.displayAccountsList(self.bankAccount.user_accounts_list)
        self.screen.promptDepositQuestion()
        answer = input().lower()

        for account in self.bankAccount.user_accounts_list:
            if account.getAccountName() == answer:
                self.screen.displayAskDeposit()
                increaseBal = input()
                self.screen.displayDepositMessage(increaseBal, account.getAccountName())
                account.addBalance(int(increaseBal))
                return
        self.screen.displayAccountNotFound(answer)
    def callTransferFunds(self):

        # Ask for donor account.
        self.screen.promptDonorAccount()
        self.screen.displayAccountsList(self.bankAccount.user_accounts_list)
        donor = input().lower()
        transferAmount = 0

        # If account exists, select and validate transfer amount.
        for donorAccount in self.bankAccount.user_accounts_list:
            if donorAccount.getAccountName() == donor:
                self.screen.selectTransferAmount()
                transferAmount = input()
                while int(transferAmount) > donorAccount.getBalance():
                    self.screen.displayOverWithdrawal()
                    transferAmount = input()
                # Select recipient account.
                self.screen.promptRecipientAccount()
                recipient = input().lower()

                # Find recipient account, confirm, then transfer.
                for recipientAccount in self.bankAccount.user_accounts_list:
                    if recipientAccount.getAccountName() == recipient:
                        verify = self.screen.confirmTransfer()
                        # input validation & break in case "no" goes here.
                        if int(verify) == 1:
                            donorAccount.decreaseBalance(int(transferAmount))
                            recipientAccount.addBalance(int(transferAmount))
                            self.screen.displayTransferMessage(transferAmount, donor, recipient)
                            return
                self.screen.displayAccountNotFound(recipient)
                return
        self.screen.displayAccountNotFound(donor)

def main():
    """initialize initial values"""
    # initialize bank
    bank = Bank('Bank of America')

    # initialize users and cards

    # initialize Williams BankAccount
    williams_debit_card = Card('111231314', datetime.datetime(2020, 5, 17))  # year, month, day
    williams_bank_account = BankAccount('William', 'Gusmanov', williams_debit_card, '0123')

    williams_checking = Checking("checking", 500)
    williams_saving1 = Savings("saving", 1000, 0.01)
    williams_saving2 = Savings("financial aid", 3000, 0.02)

    williams_bank_account.addAccount(williams_checking)
    williams_bank_account.addAccount(williams_saving1)
    williams_bank_account.addAccount(williams_saving2)

    bank.addNewBankAccount(williams_bank_account)

    # initialize the atm machine
    atm = ATM(bank)

    '''begin atm transaction'''
    atm.screen.displayHomeScreen('Bank of America')
    atm.screen.displayLogin()

    atm.insertCard(williams_debit_card)
    atm.validateCard()
    atm.screen.displaySuccessfulValidation()

    # we need a scanner here
    correct_pin = False
    # will throw exception once number of tries exceed limit
    # here we enter pin and verify it.
    while not correct_pin:
        atm.screen.promptPin()
        pin = input()
        correct_pin = atm.enterPin(pin)
        atm.screen.displaySuccessfulPin() if correct_pin else atm.screen.displayIncorrectPin()

    continue_transaction = True
    while continue_transaction:
        message = '\n press [0] for deposit funds \n ' \
                  'press [1] for withdraw funds \n press [2] for display balance \n ' \
                  'press [3] for transfer funds \n press any other key to exit'
        atm.screen.displayOptions(message)  # display options
        input_number = int(input())
        continue_transaction = atm.options(input_number)


if __name__ == '__main__':
    main()
