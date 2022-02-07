## This is mimic the game wordle
from characterManipulation import readFile
from printUtils import printUtils
class wordleClass:
    def __init__(self):
        self.wordObjects=[]
        self.wordToBeGuessed=""
        self.guessesMade=0
        self.activeIndex=0
        self.wordLength=5
        self.stateOfGuess = readFile.printBlanks(self.wordLength)
        self.lettersInWord = []
        self._input = "Please provide input: "

    def genWords(self):
        self.activeIndex = 0
        self.wordObjects = []
        while len(self.wordObjects)<=self.wordLength:
            self.wordObjects.append(readFile.printBlanks(self.wordLength))

    def printWordObject(self):
        for i in self.wordObjects:
            print(i)

    def initGame(self):
        print(f"Launching game!")
        self.stateOfGuess = readFile.printBlanks(self.wordLength)
        self.lettersInWord = []
        self.guessesMade=0
        self.genWords()
        self.genWord()
        print(f"Word is {self.wordToBeGuessed}")

    def genWord(self):
        self.wordToBeGuessed=readFile.returnLengthWord(self.wordLength)

    def getLetters(self):
        return self.lettersInWord
    def getState(self):
        return self.stateOfGuess
    def printSOW(self):
        "Return the current State of the world"
        print(f"Letters in word: ")
        print(self.getLetters())
        print(f"Current State of Guess:")
        print(self.getState())
        self.printWordObject()
    def makeGuess(self,guess):
        gameOver = False
        if len(guess)!=self.wordLength:
            printUtils.printer(False,"Guess input does not conform")
            return gameOver
        if readFile.validWordGuess(guess) and not self.wordObjects.__contains__(guess):
            self.wordObjects[self.activeIndex]=guess
            self.activeIndex+=1
            printUtils.printer(True,"Valid guess")
            self.guessesMade+=1
            for i in guess:
                if self.wordToBeGuessed.__contains__(i) and not self.lettersInWord.__contains__(i):
                    self.lettersInWord.append(i)
            self.stateOfGuess = readFile.goodGuess(self.wordToBeGuessed, self.stateOfGuess, guess)
            self.printSOW()
            if self.wordToBeGuessed==guess:
                printUtils.printer(True,"You successfully got the word")
                self.printSOW()
                gameOver=True
            if self.guessesMade==self.wordLength:
                printUtils.printer(True, "You did not successfully got the word")
                self.printSOW()
                gameOver=True
            return gameOver
        else:
            printUtils.printer(False,"Invalid Input - Word not in word dictionary or Word has been guessed")
            return gameOver

    def runGameLogic(self):
        while True:
            launchGame=False
            print(f"Please provide start or quit to exit")
            resp=input(self._input).lower().lstrip(" ").rstrip(" ")
            if resp=="quit":
                break
            if resp=="start":
                self.initGame()
                launchGame=True
            while launchGame:
                print(f"Please provide guess or quit to exit")
                guess = input(self._input).lower().lstrip(" ").rstrip(" ")
                if guess=="quit":
                    break
                if self.makeGuess(guess):
                    break
        return True