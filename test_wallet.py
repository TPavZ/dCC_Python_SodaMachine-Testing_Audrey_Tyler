import unittest
from wallet import Wallet

class TestFillWallet(unittest.TestCase):
    def setUp(self):
        """instantiates wallet with 88 coins added to money list"""
        self.wallet = Wallet()
    
    def test_money_list_length(self):
        """checks that all 88 coins were add to the money list"""
        money_list_length = len(self.wallet.money)
        self.assertEqual(money_list_length, 88)

if __name__ == '__main__':
    unittest.main()