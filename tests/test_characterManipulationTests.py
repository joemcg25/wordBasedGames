import unittest
from src.characterManipulation import readFile

class TestReturnLengthWord(unittest.TestCase):
    def test_lengthOf(self):
        item=readFile.returnLengthWord(6)
        self.assertEqual(6,len(item))

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

class TestAlterWord(unittest.TestCase):
    def test_genWord(self):
        item = readFile.alterWord("toChange",3,"A")
        self.assertEqual(item,"toCAange")

class TestGetIndexes(unittest.TestCase):
    def test_genWord0(self):
        item = readFile.getIndexes("This This This ","T")
        self.assertEqual(item,[0,5,10])
    def test_genWord1(self):
        item = readFile.getIndexes("This This This ","Z")
        self.assertEqual(item,[])
    def test_genWord2(self):
        item = readFile.getIndexes("This This This Love","L")
        self.assertEqual(item,[15])

class TestPrintBlanks(unittest.TestCase):
    def test_printBlanks0(self):
        item = readFile.printBlanks(0)
        self.assertEqual(item,"")
    def test_printBlanks1(self):
        item = readFile.printBlanks(4)
        self.assertEqual(item,"____")

class TestValidGuess(unittest.TestCase):
    def test_validGuess0(self):
        item = readFile.validLetterGuess("a")
        self.assertTrue(item)
    def test_validGuess1(self):
        item = readFile.validLetterGuess("4")
        self.assertFalse(item)
    def test_validWordGuess0(self):
        item = readFile.validWordGuess("word")
        self.assertTrue(item)
    def test_validWordGuess1(self):
        item = readFile.validWordGuess("notQWord")
        self.assertFalse(item)

class TestReturnLengthWord(unittest.TestCase):
    def test_returnLengthWords0(self):
        item = readFile.returnLengthWord(4)
        self.assertEqual(len(item),4)
    def test_returnLengthWords1(self):
        item = readFile.returnLengthWord(8)
        self.assertEqual(len(item),8)

class TestReturnLengthWords(unittest.TestCase):
    def test_returnLengthWords0(self):
        item = readFile.returnLengthWords(2,4)
        self.assertTrue(len(item)<=4)
    def test_returnLengthWords1(self):
        item = readFile.returnLengthWords(5,8)
        self.assertTrue(len(item)<=8)

class TestGetIndexes(unittest.TestCase):
    def test_getIndexes0(self):
        item = readFile.getIndexes("test","t")
        self.assertEqual(item,[0,3])
    def test_getIndexes1(self):
        item = readFile.getIndexes("test","q")
        self.assertEqual(item,[])

class TestCheckLetters(unittest.TestCase):
    def test_checkLetters0(self):
        item = readFile.checkLetters("test","t")
        self.assertEqual(item,["t"])
    def test_checkLetters1(self):
        item = readFile.checkLetters("test","q")
        self.assertEqual(item,[])
    def test_checkLetters2(self):
        item = readFile.checkLetters("flash","fla")
        self.assertEqual(item,["f","l","a"])

class TestGoodGuess(unittest.TestCase):
    def test_goodGuess0(self):
        item=readFile.goodGuess("butter","______","t")
        self.assertEqual(item,"__tt__")
    def test_goodGuess1(self):
        item=readFile.goodGuess("butter","______","t")
        item = readFile.goodGuess("butter", item, "b")
        self.assertEqual(item,"b_tt__")
    def test_goodGuess2(self):
        item=readFile.goodGuess("butter","______","t")
        item = readFile.goodGuess("butter", item, "b")
        item = readFile.goodGuess("butter", item, "q")
        self.assertEqual(item,"b_tt__")

def runUnitTests():
    print(__name__)
    unittest.main()

if __name__ == '__main__':
    runUnitTests()