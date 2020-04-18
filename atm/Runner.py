from atm.ATM import ATM
from atm.Bank import Bank
from atm.BankAccount import BankAccount
from atm.Card import Card
import datetime

# ISAIAH WAS HERE

def main():
    """initialize initial values"""
    # initialize bank
    bank = Bank('Bank of America')

    # initialize users and cards
    williams_debit_card = Card('111231314', datetime.datetime(2020, 5, 17))  # year, month, day
    williams_bank_account = BankAccount('William', 'Gusmanov', williams_debit_card, '0123')

    bank.addNewBankAccount(williams_bank_account)

    # initialize the atm machine
    atm = ATM(bank)

    '''begin atm transaction'''
    atm.screen.displayHomeScreen('Bank of America')
    atm.screen.displayLogin()

    atm.insertCard(williams_debit_card)
    atm.validateCard()
    atm.screen.promptPin()

    # we need a scanner here
    correct_pin = False

    # will throw exception once number of tries exceed limit
    # here we enter pin and verify it.
    while not correct_pin:
        pin = input()
        atm.enterPin(pin)
        # atm.enterPin('0123')

    continue_transaction = True
    while continue_transaction:
        message = 'press [0] for deposit funds \n press [1] for withdraw funds \n press [2] for display balance \n ' \
                  'press [3] for transfer funds \n press any other key to exit'
        atm.screen.displayOptions(message) # display options
        input_number = int(input())
        continue_transaction = atm.Options(input_number)


if __name__ == '__main__':
    main()