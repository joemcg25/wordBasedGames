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