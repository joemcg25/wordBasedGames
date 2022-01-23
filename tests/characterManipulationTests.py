#TODO Get running with python -m unittest
from src.characterManipulation import readFile
import unittest

class TestReturnLengthWord(unittest.TestCase):
    def test_lengthOfSix(self):
        item=readFile.returnLengthWord(6)
        self.assertEqual(6,len(item))
    def test_lengthOfSeven(self):
        item=readFile.returnLengthWord(7)
        self.assertEqual(7,len(item))

class TestRandomWord(unittest.TestCase):
    def test_randomWord(self):
        item=readFile.getRandomWord()
        self.assertTrue(item in readFile.file)

class TestRandomWord0(unittest.TestCase):
    def test_randomWord0(self):
        item = readFile.getRandomWord0(["abc","item1"])
        self.assertTrue(item in ["abc","item1"])

class TestGenWord(unittest.TestCase):
    def test_genWord(self):
        item = readFile.genWord()
        self.assertTrue(item in readFile.file)

class TestToList(unittest.TestCase):
    def test_genWord(self):
        item = readFile.toList("ToList")
        self.assertEqual(["T","o","L","i","s","t"],item)

class TestToWord(unittest.TestCase):
    def test_genWord(self):
        item = readFile.toWord(["T","o","L","i","s","t"])
        self.assertEqual(item,"ToList")

def runUnitTests():
    print(__name__)
    unittest.main()

if __name__ == '__main__':
    runUnitTests()