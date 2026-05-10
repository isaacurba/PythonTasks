from unittest import TestCase

import redigestionTwo

class toggleCase(TestCase):

    def test_that_digit_adder_exists(self):
        redigestionTwo.digit_adder("a1a1a1a1")

    def test_that_digit_adder_adds_the_digits(self):
        actual_value = redigestion.case_toggle("a1a1a1a1")
        expected_value = redigestion.case_toggle("a1a1a1a1")
        self.assertTrue(actual_value, expected_value)
