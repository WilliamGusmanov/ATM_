class BankAccount:
    def __init__(self, first_name, last_name, card, pin_number):
        if self.validatePinCreation(pin_number):
            self.pin_number = pin_number
        self.first_name = first_name
        self.last_name = last_name
        self.card = card
        self.user_accounts_list = [] # a list of accounts like checkings/savings

    @staticmethod
    def validatePinCreation(pin_number):
        pin_size_val = False
        pin_type_val = False
        if len(pin_number) == 4:
            pin_size_val = True
        for character in pin_number:
            if str.isdigit(character):
                pin_type_val = True
        if pin_type_val and pin_size_val:
            return True
        else:
            return False

    # add a new user account (checking or savings) to accounts
    def addAccount(self, new_account):
        self.user_accounts_list.append(new_account)

    def getPinNumber(self):
        if self.pin_number is not None:
            return self.pin_number
        else:
            raise Exception('there is no pin number.')

    def getCardID(self):
        return self.card.getCardNumber()

