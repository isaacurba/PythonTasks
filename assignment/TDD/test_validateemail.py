import unittest
from validateemail import validate_email

class test_validate_email_function(unittest.TestCase):
    def test_that_string_has_email_at(self):
        result = validate_email("isaac@urban")
        self.assertTrue(result, "The email has an @ sign")
        
if __name__    == '_main_':
    unittest.main() 
        
