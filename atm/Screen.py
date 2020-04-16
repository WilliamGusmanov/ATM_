class Screen:

    @staticmethod
    def promptPin():
        print('Please enter your Pin Number: ')

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

    @staticmethod
    def displaySuccessfulValidation():
        print('no errors found.')

    @staticmethod
    def displayIncorrectPin():
        print("Incorrect PIN entered.")

    @staticmethod
    def displaySuccessfulPin():
        print("correct pin.")

    @staticmethod
    def displayAttemptsRemaining(attempts):
        print("You have " + attempts + " attempts remaining")

    @staticmethod
    def displayPromptAccountName():
        print("Please enter the name of the account: ")

    @staticmethod
    def displayBalance(message):
        print(message)

    @staticmethod
    def displayAccountsList(accountList):
        print("Which account would you like to withdrawal from?")
        print("Your accounts: ", end = '')
        for account in accountList:
            print(account.getAccountName() + ", ", end = '')

    @staticmethod
    def displayAskWithdrawal():
        print("How much would you like to withdrawal?")