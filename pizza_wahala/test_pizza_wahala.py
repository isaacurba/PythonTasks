from unittest import TestCase

from pizza_wahala import *

class PizzaWahalaTest(TestCase):

    def test_to_get_accurate_number_with_box_type(self):

        sapa_pizza_type = "sapa"
        odogwu_pizza_type = "odogwu"
        no_of_slice_sapa_type = get_number_of_slice(sapa_pizza_type)
        no_of_slice_odogwu_type = get_number_of_slice(odogwu_pizza_type)

        self.assertEqual(no_of_slice_sapa_type, 4)
        self.assertEqual(no_of_slice_odogwu_type, 12)


    def test_to_get_accurate_number_with_box_type_second(self):

        small_money_pizza_type = "smallMoney"
        big_boy_pizza_type = "bigBoys"
        no_of_slice_sapa_type = get_number_of_slice(small_money_pizza_type)
        no_of_slice_odogwu_type = get_number_of_slice(big_boy_pizza_type)

        self.assertEqual(no_of_slice_sapa_type, 6)
        self.assertEqual(no_of_slice_odogwu_type, 8)


    def test_to_check_worng_input_of_pizza_type(self):

        wrong_pizza_type = "audrey pizza"

        self.assertRaises(ValueError, get_number_of_slice, wrong_pizza_type)


    def test_that_get_pizza_type_sapa_price(self):

        sapa_price = 2_500.00
        actual_price = get_price_of_pizza_type("sapa")
        self.assertEqual(actual_price, sapa_price)

    def test_to_get_all_the_price_of_the_pizza_type(self):

        sapa_price = 2_500.00
        small_money_price = 2_900.00
        big_price_boys = 4_000.00
        odogwu_price = 5_200.00

        self.assertEqual(sapa_price, get_price_of_pizza_type("sapa"))
        self.assertEqual(small_money_price, get_price_of_pizza_type("smallMoney"))
        self.assertEqual(big_price_boys, get_price_of_pizza_type("bigBoys"))
        self.assertEqual(odogwu_price, get_price_of_pizza_type("odogwu"))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
