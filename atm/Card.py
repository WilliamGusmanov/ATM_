class Card:
    def __init__(self, card_number, expiration_date):
        self.__expirationDate = expiration_date
        self.__card_number = card_number

    def getCardNumber(self):
        return self.__card_number

    def getExpirationDate(self):
        return self.__expirationDate
