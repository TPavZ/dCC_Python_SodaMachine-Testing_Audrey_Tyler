import unittest
from customer import Customer
import coins    
import cans

class Testgetwalletcoin(unittest.TestCase):
    """Test get_wallet_coin"""
    def setUp(self):
        self.customer = Customer()
    
    def test_get_quarter(self):
        """Passing in "Quarter" string will return a Quarter object"""
        returned_coin = self.customer.get_wallet_coin("Quarter")
        self.assertEqual(returned_coin.name, "Quarter")
    
    def test_get_dime(self):
        """Passing in "Dime" string will return a Dime object"""
        returned_coin = self.customer.get_wallet_coin("Dime")
        self.assertEqual(returned_coin.name, "Dime")
    
    def test_get_nickel(self):
        """Passing in "Nickel" string will return a Nickel object"""
        returned_coin = self.customer.get_wallet_coin("Nickel")
        self.assertEqual(returned_coin.name, "Nickel")
    
    def test_get_penny(self):
        """Passing in "Penny" string will return a Penny object"""
        returned_coin = self.customer.get_wallet_coin("Penny")
        self.assertEqual(returned_coin.name, "Penny")
    
    def test_get_invalid_coin(self):
        """Passing in an invalid string that will return none"""
        returned_coin = self.customer.get_wallet_coin("Quarter") or self.customer.get_wallet_coin("Dime") or self.customer.get_wallet_coin("Nickel") or self.customer.get_wallet_coin("Penny")
        self.assertNotEqual(returned_coin.name, "anything else")

class Testaddcoinstowallet(unittest.TestCase):
    """Test add_coins_to_wallet"""
    def setUp(self):
        self.customer = Customer()

    def test_add_coins(self):
        """Test that takes in three items and checks if the wallet list increased by 3"""
        original_wallet = len(self.customer.wallet.money)
        self.customer.add_coins_to_wallet([coins.Penny(), coins.Penny(), coins.Penny()])
        new_wallet = len(self.customer.wallet.money)
        self.assertEqual((original_wallet + 3), new_wallet)

    def test_add_nothing(self):
        """Test that takes in nothing and confirms no changes where made to wallet"""
        original_wallet = len(self.customer.wallet.money)
        self.customer.add_coins_to_wallet([])
        new_wallet = len(self.customer.wallet.money)
        self.assertEqual(original_wallet, new_wallet)
    

class Testaddcantobackpack(unittest.TestCase):
    """Test add_can_to_backpack"""
    def setUp(self):
        self.customer = Customer()
    
    #Test will repeat for each type of can.
    def test_add_one_cola_to_backpack(self):
        """Test that takes in one soda (Cola) and makes sure the len of the items in backpack increases by one"""
        original_backpack = len(self.customer.backpack.purchased_cans)
        self.customer.add_can_to_backpack(cans.Cola)
        new_backpack = len(self.customer.backpack.purchased_cans)
        self.assertEqual(original_backpack + 1, new_backpack)

    def test_add_one_orangesoda_to_backpack(self):
        """Test that takes in one soda (OrangeSoda) and makes sure the len of the items in backpack increases by one"""
        original_backpack = len(self.customer.backpack.purchased_cans)
        self.customer.add_can_to_backpack(cans.OrangeSoda)
        new_backpack = len(self.customer.backpack.purchased_cans)
        self.assertEqual(original_backpack + 1, new_backpack)
        
    def test_add_one_rootbeer_to_backpack(self):
        """Test that takes in one soda (RootBeer) and makes sure the len of the items in backpack increases by one"""
        original_backpack = len(self.customer.backpack.purchased_cans)
        self.customer.add_can_to_backpack(cans.RootBeer)
        new_backpack = len(self.customer.backpack.purchased_cans)
        self.assertEqual(original_backpack + 1, new_backpack)

if __name__ == "__main__":
    unittest.main()

    