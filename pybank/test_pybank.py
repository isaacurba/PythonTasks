import unittest 

import pybank

class TestValidateEmailthe(unittest.TestCase):
    
    def test_that_validate_email_function_exist(self):
        pybank.validate_email("isaac@urban.com")
        
    def test_that_email_lenght_is_greater_than_eight(self):
        is_valid = pybank.validate_email("007isaacurban@mail.com")
        self.assertTrue(is_valid)
        
    def test_that_email_length_is_not_less_than_eight(self):
        is_invalid = pybank.validate_email("muse")
        self.assertFalse(is_invalid)
        
    def test_that_email_contains_special_character(self):
        actual = pybank.validate_email("123@mail.com")
        expected = "valid emain"
        self.assertTrue(is_valid)
