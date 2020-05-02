import unittest
from atm.BankAccount import BankAccount
from atm.Account import Account


class TestGetBalance(unittest.TestCase):
    def test_getBalance(self):
        account = Account("test", 500)
        result = account.getBalance()
        self.assertEqual(result, 500)

    if __name__ == '__main__':
        unittest.main()
