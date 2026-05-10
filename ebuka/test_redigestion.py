from unittest import TestCase

import redigestion

class toggleCase(TestCase):

    def test_that_case_toggle_exists(self):
        redigestion.case_toggle("PyThOn")

    def test_that_does_the_actual_case_toggle(self):
        actual_value = redigestion.case_toggle("PyThOn")
        expected_value = "pYtHoN"
        self.assertEquals(actual_value, expected_value)
