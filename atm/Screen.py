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
    def displayAccountsList(account_list):
        print("Your accounts: ", end = '')
        message = list("")
        for account in account_list:
            message.append(account.getAccountName())
            message.append(", ")
        message[len(message) - 1] = ""
        string = "".join(message)
        print(string)


    # Withdraw Functions

    @staticmethod
    def displayAskWithdrawal():
        print("How much would you like to withdrawal?")

    @staticmethod
    def displayOverWithdrawal():
        print("You are exceeding the amount of your bank account, please try again")

    @staticmethod
    def promptWithdrawQuestion():
        print("Which account would you like to withdrawal from?")


    # Deposit Functions
    @staticmethod
    def displayAskDeposit():
        print("How much would you like to deposit?")

    @staticmethod
    def promptDepositQuestion():
        print("Which account would you like to deposit into?")


    # Transfering Funds

    @staticmethod
    def promptDonorAccount():
        print("Which account would you like to send money from?")

    @staticmethod
    def promptRecipientAccount():
        print("Which account would you like to send money to?")

    @staticmethod
    def selectTransferAmount():
        print("How much would you like to transfer?")

    @staticmethod
    def confirmTransfer():
        print("Are you sure you would like to complete this transaction?")
        print("1. Yes.")
        print("2. No.")
        answer = input()

        if int(answer) == 1:
            return True
        else:
            return False



