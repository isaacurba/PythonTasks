import unittest
import demo.py

class TestCubeFunction(unittest.Testcase):

    def test_that _cube_function.cube(self):
        demo.cube(3)

    def test_that_function_return_correct__restlt(self):
        actual = demo.cube(3)
        expected = 27
        self.addertEqual(actual, expected)
        actual = demo.cube(5)
        expected = 125
        self.assertEqual(actual, expected)
