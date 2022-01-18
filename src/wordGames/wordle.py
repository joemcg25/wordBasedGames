#TODO Need to add logic to print word state
#TODO Print out if any letters are in the word

## This is mimic the game wordle
from characterManipulation import readFile
from printUtils import printUtils
class wordleClass:
    def __init__(self):
        self.wordObjects=[]
        self.wordToBeGuessed=""
        self.noGuesses=5
        self.guessesMade=0
        self.activeIndex=0
        self.guessState = readFile.printBlanks(self.noGuesses)

    def genWords(self):
        self.activeIndex = 0
        self.wordObjects = []
        while len(self.wordObjects)<self.noGuesses:
            self.wordObjects.append(readFile.printBlanks(self.noGuesses))

    def printWordObject(self):
        for i in self.wordObjects:
            print(i)

    def initGame(self):
        print(f"Launching game!")
        self.guessesMade=0
        self.genWords()
        self.genWord()
        print(f"Word is {self.wordToBeGuessed}")
        self.printWordObject()

    def genWord(self):
        self.wordToBeGuessed=readFile.returnLengthWord(self.noGuesses)

    def checkWord(self):
        pass

    def makeGuess(self,guess):
        gameOver = False
        if len(guess)!=self.noGuesses:
            printUtils.printInvalid(f"Guess input does not conform")
            return gameOver
        if readFile.validWordGuess(guess) and not self.wordObjects.__contains__(guess):
            self.wordObjects[self.activeIndex]=guess
            self.activeIndex+=1
            printUtils.printValid(f"Valid guess")
            self.printWordObject()
            self.guessesMade+=1
            if self.wordToBeGuessed==guess:
                printUtils.printValid(f"You successfully got the word")
                self.printWordObject()
                gameOver=True
            if self.guessesMade==self.noGuesses:
                self.printWordObject()
                gameOver=True
            return gameOver
        printUtils.printInvalid(f"Invalid Input - Word not in word dictionary or Word has been guessed")
        self.printWordObject()
        return gameOver

    def runGame(self):
        while True:
            launchGame=False
            print(f"Please provide start or quit to exit")
            resp=input()
            if resp=="quit":
                break
            if resp=="start":
                self.initGame()
                launchGame=True
            while launchGame:
                print(f"Please provide guess or quit to exit")
                guess = input()
                if guess=="quit":
                    break
                if self.makeGuess(guess):
                    break
        return True