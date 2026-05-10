from unittest import TestCase

import redigestionthree

class space_compressor(TestCase):

    def test_that_space_compressor_function_exists(self):
        redigestionthree.space_compressor("hello world")
