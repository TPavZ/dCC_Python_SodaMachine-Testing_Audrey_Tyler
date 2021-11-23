import unittest
from soda_machine import SodaMachine
import coins
import cans

class TestFillRegister(unittest.TestCase):
    def setUp(self):
        """instantiates soda machine with register of 88 coins and inventory of 30 cans"""
        self.soda_machine = SodaMachine()
    
    def test_fill_register(self):
        """tests that all 88 coins were added to register list"""
        register_list_length = len(self.soda_machine.register)
        self.assertEqual(register_list_length, 88)

class TestFillInventory(unittest.TestCase):
    def setUp(self):
        """instantiates soda machine with register of 88 coins and inventory of 30 cans"""
        self.soda_machine = SodaMachine()
    
    def test_fill_inventory(self):
        """tests that all 30 cans were added to inventory list"""
        inventory_list_length = len(self.soda_machine.inventory)
        self.assertEqual(inventory_list_length, 30)

class TestGetCoinFromRegister(unittest.TestCase):
    def setUp(self):
        """instantiates soda machine with register of 88 coins and inventory of 30 cans"""
        self.soda_machine = SodaMachine()
    
    def test_get_quarter(self):
        """tests that passing in Quarter string will return Quarter object"""
        returned_coin = self.soda_machine.get_coin_from_register('Quarter')
        self.assertIsInstance(returned_coin, coins.Quarter)
    
    def test_get_dime(self):
        """tests that passing in Dime string will return Dime object"""
        returned_coin = self.soda_machine.get_coin_from_register('Dime')
        self.assertIsInstance(returned_coin, coins.Dime)
    
    def test_get_nickel(self):
        """tests that passing in Nickel string will return Nickel object"""
        returned_coin = self.soda_machine.get_coin_from_register('Nickel')
        self.assertIsInstance(returned_coin, coins.Nickel)

    def test_get_penny(self):
        """tests that passing in Penny string will return Penny object"""
        returned_coin = self.soda_machine.get_coin_from_register('Penny')
        self.assertIsInstance(returned_coin, coins.Penny)
    
    def test_get_none(self):
        """tests that passing in not recognized string will return None"""
        returned_coin = self.soda_machine.get_coin_from_register('nothing')
        self.assertEqual(returned_coin, None)

class TestRegisterHasCoin(unittest.TestCase):
    def setUp(self):
        """instantiates soda machine with register of 88 coins and inventory of 30 cans"""
        self.soda_machine = SodaMachine()
    
    def test_has_quarter(self):
        """tests that passing in Quarter string will return True"""
        true_or_false = self.soda_machine.register_has_coin('Quarter')
        self.assertTrue(true_or_false)
    
    def test_has_dime(self):
        """tests that passing in Dime string will return True"""
        true_or_false = self.soda_machine.register_has_coin('Dime')
        self.assertTrue(true_or_false)
    
    def test_has_nickel(self):
        """tests that passing in Nickel string will return True"""
        true_or_false = self.soda_machine.register_has_coin('Nickel')
        self.assertTrue(true_or_false)

    def test_has_penny(self):
        """tests that passing in Penny string will return True"""
        true_or_false = self.soda_machine.register_has_coin('Penny')
        self.assertTrue(true_or_false)
    
    def test_has_none(self):
        """tests that passing in not recognized string will return False"""
        true_or_false = self.soda_machine.register_has_coin('nothing')
        self.assertFalse(true_or_false)

class TestDetermineChangeValue(unittest.TestCase):
    def setUp(self):
        """instantiates soda machine with register of 88 coins and inventory of 30 cans"""
        self.soda_machine = SodaMachine()
    
    def test_total_payment_higher(self):
        """tests that passing in total_payment > selected_soda_price results in positive expected change value"""
        change_value = self.soda_machine.determine_change_value(1, 0.60)
        self.assertEqual(change_value, 0.4)
        
    def test_selected_soda_higher(self):
        """tests that passing in total_payment < selected_soda_price results in negative expected change value"""
        change_value = self.soda_machine.determine_change_value(0.40, 0.60)
        self.assertEqual(change_value, -0.2)
    
    def test_equal_values(self):
        """tests that passing in total_payment == selected_soda_price results in 0"""
        change_value = self.soda_machine.determine_change_value(0.60, 0.60)
        self.assertEqual(change_value, 0)

class TestCalculateCoinValue(unittest.TestCase):
    def setUp(self):
        """instantiates soda machine with register of 88 coins and inventory of 30 cans"""
        self.soda_machine = SodaMachine()
    
    def test_calculate_total_value(self):
        """instantiates each of the 4 coin types and appends them to a list and checks that total_value == 0.41"""
        coin_list = [coins.Quarter(), coins.Dime(), coins.Nickel(), coins.Penny()]
        coin_list_value = self.soda_machine.calculate_coin_value(coin_list)
        self.assertEqual(coin_list_value, 0.41)
    
    def test_empty_total_value(self):
        """passes empty list into calculate_coin_value and checks that total_value == 0"""
        coin_list = []
        
        coin_list_value = self.soda_machine.calculate_coin_value(coin_list)
        self.assertEqual(coin_list_value, 0)
        
class TestGetInventorySoda(unittest.TestCase):
    def setUp(self):
        """instantiates soda machine with register of 88 coins and inventory of 30 cans"""
        self.soda_machine = SodaMachine()     
    
    def test_get_cola(self):
        """tests that passing in Cola string will return Cola object"""
        returned_can = self.soda_machine.get_inventory_soda('Cola')
        self.assertIsInstance(returned_can, cans.Cola)
    
    def test_get_orange_soda(self):
        """tests that passing in Orange Soda string will return OrangeSoda object"""
        returned_can = self.soda_machine.get_inventory_soda('Orange Soda')
        self.assertIsInstance(returned_can, cans.OrangeSoda)
    
    def test_get_root_beer(self):
        """tests that passing in Root Beer string will return RootBeer object"""
        returned_can = self.soda_machine.get_inventory_soda('Root Beer')
        self.assertIsInstance(returned_can, cans.RootBeer)
    
    def test_get_mountain_dew(self):
        """tests that passing in Mountain Dew string will return None"""
        returned_can = self.soda_machine.get_inventory_soda('Mountain Dew')
        self.assertEqual(returned_can, None)

class TestReturnInventory(unittest.TestCase):
    def setUp(self):
        """instantiates soda machine with register of 88 coins and inventory of 30 cans"""
        self.soda_machine = SodaMachine()    
    
    def test_return_can(self):
        """instantiates one can and returns it to inventory tests to see if inventory length now 31"""
        can_to_return = cans.Cola()
        self.soda_machine.return_inventory(can_to_return)
        
        length_of_inventory = len(self.soda_machine.inventory)
        self.assertEqual(length_of_inventory, 31)
        
class TestDepositCoinsIntoRegister(unittest.TestCase):
    def setUp(self):
        """instantiates soda machine with register of 88 coins and inventory of 30 cans"""
        self.soda_machine = SodaMachine()
    
    def test_deposit_coins(self):
        """instantiates each of 4 coins and adds them to register then tests new register length == 92"""
        coin_list = [coins.Quarter(), coins.Dime(), coins.Nickel(), coins.Penny()]
        self.soda_machine.deposit_coins_into_register(coin_list)
        length_register_list = len(self.soda_machine.register)
        self.assertEqual(length_register_list, 92)
        
if __name__ == '__main__':
    unittest.main()