import unittest
from src.wordGames import basicHangman

class TestBasicHangman(unittest.TestCase):
    def setUp(self) -> None: # Called before every test
        self.hangman = basicHangman.basicHangman()
        self.hangman.flipSetDifficulty(True)
        self.hangman.initGame()
    def tearDown(self) -> None: # Called after every test
        pass
    def test_flip_difficultyTrue(self):
        self.hangman.flipSetDifficulty(True)
        self.assertTrue(self.hangman._difficultySet)
    def test_flip_difficultyFalse(self):
        self.hangman.flipSetDifficulty(False)
        self.assertFalse(self.hangman._difficultySet)
    def test_initGameEasy(self):
        self.assertEqual(self.hangman._noGuesses,10)
    def test_initGameMedium(self):
        self.hangman._difficultyVal="medium"
        self.hangman.initGame()
        self.assertEqual(self.hangman._noGuesses,7)
    def test_makeGuess(self):
        self.hangman._difficultyVal="medium"
        self.hangman.initGame()
        self.assertEqual(self.hangman._noGuesses,7)
    def test_makeCorrectGuess(self):
        word=self.hangman._wordToBeGuessed
        self.hangman.handleGuess(word)
        self.assertEqual(self.hangman._stateOfGuess,word)
    def test_addToGuesses1(self):
        self.hangman.handleGuess("a")
        self.assertTrue(self.hangman._guesses.__contains__("a"))
    def test_addToGuesses2(self):
        self.hangman.handleGuess("a")
        self.hangman.handleGuess("b")
        self.assertTrue(self.hangman._guesses.__contains__("a") and self.hangman._guesses.__contains__("b"))
    def test_addToGuesses3(self):
        self.hangman.handleGuess("a")
        self.hangman.handleGuess("1")
        self.assertTrue(not self.hangman._guesses.__contains__("1"))
    def test_addToGuesses4(self):
        self.hangman.handleGuess("a")
        self.hangman.handleGuess("a")
        self.assertEqual(["a"],self.hangman._guesses)
    def test_addToGuesses_wordGuess(self):
        self.hangman.handleGuess("attempted")
        self.hangman.handleGuess("a")
        self.assertEqual(["attempted","a"],self.hangman._guesses)
    def test_guessesReduce(self):
        self.hangman.handleGuess("attempt")
        self.hangman.handleGuess("attempts")
        self.assertEqual(8,self.hangman._noGuesses)
    def test_guessesReduce1(self):
        self.hangman.handleGuess("attempt")
        self.hangman.handleGuess("attempt")
        self.assertEqual(9,self.hangman._noGuesses)
    def test_restartGame(self):
        self.hangman.handleGuess("attempt")
        self.hangman.handleGuess("a")
        self.hangman.handleGuess("b")
        self.hangman.handleGuess("z")
        word=self.hangman._wordToBeGuessed
        self.hangman.initGame()
        res=self.hangman._wordToBeGuessed!=word and self.hangman._noGuesses==10
        self.assertTrue(res)
    def test_goodGuess(self):
        self.hangman._wordToBeGuessed="butter"
        self.hangman._stateOfGuess="______"
        self.hangman.handleGuess("t")
        self.hangman.handleGuess("b")
        self.hangman.handleGuess("r")
        self.assertEqual("b_tt_r",self.hangman._stateOfGuess)