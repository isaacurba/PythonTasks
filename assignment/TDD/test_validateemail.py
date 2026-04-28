import unittest
from validateemail import validate_email

class test_validate_email_function(unittest.TestCase):
    def test_that_string_has_email_at_symbol(self):
        email = validate_email("isaacurbancom")
        self.assertFalse(email, "The email has an @ and . sign")
        
    def test_that_show_email_length_is_at_least_eight_characters(self):
        email = validate_email("mail@")
        self.assertFalse(email, "email is not than eight characters")
        
    def test_that_shows_email_does_not_start_or_ends_with_at_symbol(self):
        email = validate_email("@meemail.com@")
        self.assertFalse(email, "email does not starts with the @ sign ")
        
