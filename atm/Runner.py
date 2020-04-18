from atm.ATM import ATM
from atm.Bank import Bank
from atm.BankAccount import BankAccount
from atm.Card import Card
from atm.Checking import Checking
from atm.Savings import Savings
from atm.Account import Account
import datetime


# ISAIAH WAS HERE
# Testing again

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
