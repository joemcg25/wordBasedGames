import unittest
from src.wordGames import wordle

class TestWordle(unittest.TestCase):
    def setUp(self) -> None: # Called before every test
        self.wordle = wordle.wordleClass()
        self.wordle.initGame()
    def tearDown(self) -> None: # Called after every test
        pass
    def test_makeGuessWrongLength(self):
        res=self.wordle.makeGuess("THIS GUESS IS MUCH TOO LONG")
        self.assertFalse(res)
    def test_makeGuessWrongLengthNoChangeToGuesses(self):
        res=self.wordle.makeGuess("THIS GUESS IS MUCH TOO LONG")
        self.assertEqual(0,self.wordle.guessesMade)
    def test_makeGuessWrongLengthNoChangeToIndex(self):
        res=self.wordle.makeGuess("THIS GUESS IS MUCH TOO LONG")
        self.assertEqual(0,self.wordle.activeIndex)
    def test_makeValidGuess(self):
        res=self.wordle.makeGuess("hurls")
        self.assertFalse(res)
    def test_makeGuessLengthChangeToGuesses(self):
        res=self.wordle.makeGuess("hurls")
        self.assertEqual(1,self.wordle.guessesMade)
    def test_makeGuessLengthChangeToIndex(self):
        res=self.wordle.makeGuess("hurls")
        self.assertEqual(1,self.wordle.activeIndex)
    def test_makeCorrectGuess(self):
        guess=self.wordle.wordToBeGuessed
        res=self.wordle.makeGuess(guess)
        self.assertTrue(res)
    def test_makeValidGuess2(self):
        self.wordle.makeGuess("hurls")
        res=self.wordle.wordObjects[0]
        self.assertEqual("hurls",res)
    def test_makeInvalidGuess0(self):
        res=self.wordle.makeGuess("length")
        self.assertFalse(res)