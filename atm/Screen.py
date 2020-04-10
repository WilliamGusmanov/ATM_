class Screen:

    @staticmethod
    def promptPin():
        print('Please enter your Pin Number.')

    @staticmethod
    def displayLogin():
        print('Please enter your card.')

    @staticmethod
    def displayHomeScreen(bank_name):
        print('Welcome to ' + bank_name + '!')

    @staticmethod
    def displayOptions(message):
        print(message)

    @staticmethod
    def displayWithdrawalMessage(amount):
        print('Withdrawing ' + amount)

    @staticmethod
    def displayDepositMessage(amount, account_name):
        print('Depositing ' + amount + ' into ' + account_name)

    @staticmethod
    def displayTransferMessage(amount, account_name1, account_name2):
        print("Transferring " + amount + " between " + account_name1 + " and " + account_name2)

    @staticmethod
    def displayExitMessage():
        print("Thank you, Goodbye!")
