import unittest
from atm.BankAccount import BankAccount
from atm.Account import Account

class TestDepositBalance(unittest.TestCase):
    def test_depositBalance(self):
        account = Account("test", 500)
        account.addBalance(500)
        results = account.getBalance()
        self.assertEqual(results, 1000)

    if __name__ == '__main__':
        unittest.main()

