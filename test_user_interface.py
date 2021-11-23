#Note: Since user_interface is a module, not a class, these TestCases will not require a setUp method

import unittest
import user_interface
import cans
import coins

class TestValidateMainMenu(unittest.TestCase):
    """Test validate_main_menu"""

    def test_input_1_returns_tuple(self): #1
        """test takes input of 1, ensuring the tuple of (True, number) is returned"""
        taken_input_int = user_interface.validate_main_menu(1)
        self.assertEqual(taken_input_int, (True, 1))

    def test_input_2_returns_tuple(self): #2
        """test takes input of 2, ensuring the tuple of (True, number) is returned"""
        taken_input_int = user_interface.validate_main_menu(2)
        self.assertEqual(taken_input_int, (True, 2))

    def test_input_3_returns_tuple(self): #3
        """test takes input of 3, ensuring the tuple of (True, number) is returned"""
        taken_input_int = user_interface.validate_main_menu(3)
        self.assertEqual(taken_input_int, (True, 3))

    def test_input_4_returns_tuple(self):#4
        """test takes input of 4, ensuring the tuple of (True, number) is returned"""
        taken_input_int = user_interface.validate_main_menu(4)
        self.assertEqual(taken_input_int, (True, 4))

    def test_invalid_input_returns_tuple(self):#5
        """test takes an invalid input, int. not 1-4, ensuring the tuple of (False, None) is returned"""
        taken_input_int = user_interface.validate_main_menu(0)
        self.assertEqual(taken_input_int, (False, None))


class TestTryParseInt(unittest.TestCase):
    """Test try_parse_int"""
    def test_string_number_returns_int_number(self):#6
        """Test that takes in a string number ex "5" and returns int. 5"""
        input_string = user_interface.try_parse_int("5")
        self.assertEqual(input_string, 5)

    def test_invalid_string_returns_int_0(self):#7
        """Test that takes in a string "hello" , returns int. 0"""
        input_string = user_interface.try_parse_int("hello")
        self.assertEqual(input_string, 0)


class TestGetUniqueCanNames(unittest.TestCase):
    """Test get_unique_can_names"""
    def test_duplicate_cans_returns_list_of_unique_names_only(self):#8
        """Test taking in cans (two of each type) to a list. Ensure 3 distinct soda names get returned""" 
        can_list = [cans.Cola(), cans.Cola(), cans.OrangeSoda(), cans.OrangeSoda(), cans.RootBeer(), cans.RootBeer()]
        list_unique_can_len = user_interface.get_unique_can_names(can_list)
        self.assertEqual(len(list_unique_can_len), 3)

    def test_empty_list_of_cans(self):#9
        """Test taking in an empty list, will return empty list""" 
        can_list = []
        list_unique_can_len = user_interface.get_unique_can_names(can_list)
        self.assertEqual(len(list_unique_can_len), 0)


class TestDisplayPaymentValue(unittest.TestCase):
    """Test display_payment_value"""
    def test_list_of_coins_returns_correct_value(self): #0.41 #10
        """Test taking in a string of coins to return the sum of values"""
        coin_list = [coins.Dime(), coins.Nickel(), coins.Penny(), coins.Quarter()]
        total_coin_list_value = user_interface.display_payment_value(coin_list)
        self.assertEqual(total_coin_list_value, 0.41)

    def test_empty_list_of_coins_has_0_value(self): #11
        """Test taking in a string of nothing returns 0 value"""
        coin_list = []
        total_coin_list_value = user_interface.display_payment_value(coin_list)
        self.assertEqual(total_coin_list_value, 0)


class TestValidateCoinSelection(unittest.TestCase):
    """Test validate_coin_selection"""
    def test_input_1_returns_coin_tuple(self): #12
        """test takes input of 1, ensuring the tuple of (True, Quarter) is returned"""
        selection_int = user_interface.validate_coin_selection(1)
        self.assertEqual(selection_int, (True, "Quarter"))

    def test_input_2_returns_coin_tuple(self): #13
        """test takes input of 2, ensuring the tuple of (True, Dime) is returned"""
        selection_int = user_interface.validate_coin_selection(2)
        self.assertEqual(selection_int, (True, "Dime"))

    def test_input_3_returns_coin_tuple(self): #14
        """test takes input of 3, ensuring the tuple of (True, Nickel) is returned"""
        selection_int = user_interface.validate_coin_selection(3)
        self.assertEqual(selection_int, (True, "Nickel"))

    def test_input_4_returns_coin_tuple(self): #15
        """test takes input of 4, ensuring the tuple of (True, Penny) is returned"""
        selection_int = user_interface.validate_coin_selection(4)
        self.assertEqual(selection_int, (True, "Penny"))

    def test_input_5_returns_coin_tuple(self): #16
        """test takes input of 5, ensuring the tuple of (True, Done) is returned"""
        selection_int = user_interface.validate_coin_selection(5)
        self.assertEqual(selection_int, (True, "Done"))

if __name__ == '__main__':
    unittest.main()