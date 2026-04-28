import unittest
from validateemail import validate_email

class test_validate_email_function(unittest.TestCase):
    def test_that_string_has_email_at_sign(self):
        result = validate_email("isaacurbancom")
        self.assertFalse(result, "The email has an @ and . sign")
        
    def test_that_show_email_length_is_at_least_eight_characters(self):
        result = validate_email("isaac@")
        self.assertFalse(result, "email is greater than eight characters")
        
