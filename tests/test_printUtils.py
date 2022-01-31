import unittest
from src.printUtils import printUtils

class TestPrintValid(unittest.TestCase):
    def test_lengthOf(self):
        item=printUtils.printValid("This is Valid")
        self.assertEqual("Valid Input - This is Valid",item)

class TestPrintInvalid(unittest.TestCase):
    def test_lengthOf(self):
        item=printUtils.printInvalid("This is not Valid")
        self.assertEqual("Invalid Input - This is not Valid",item)