from src.characterManipulation import readFile
import unittest

class TestReturnLengthWord(unittest.TestCase):
    def test_lengthOfSix(self):
        item=readFile.returnLengthWord(6)
        self.assertEqual(6,len(item))
    def test_lengthOfSeven(self):
        item=readFile.returnLengthWord(7)
        self.assertEqual(7,len(item))

def runUnitTests():
    unittest.main()

if __name__ == '__main__':
    runUnitTests()