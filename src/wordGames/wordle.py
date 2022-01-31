#TODO Need to add logic to print word state
#TODO Print out if any letters are in the word

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
        self.guessState = readFile.printBlanks(self.wordLength)

    def genWords(self):
        self.activeIndex = 0
        self.wordObjects = []
        while len(self.wordObjects)<self.wordLength:
            self.wordObjects.append(readFile.printBlanks(self.wordLength))

    def printWordObject(self):
        for i in self.wordObjects:
            print(i)

    def initGame(self):
        print(f"Launching game!")
        self.guessesMade=0
        self.genWords()
        self.genWord()
        print(f"Word is {self.wordToBeGuessed}")

    def genWord(self):
        self.wordToBeGuessed=readFile.returnLengthWord(self.wordLength)

    def checkWord(self):
        pass

    def makeGuess(self,guess):
        gameOver = False
        if len(guess)!=self.wordLength:
            printUtils.printer(False,"Guess input does not conform")
            return gameOver
        if readFile.validWordGuess(guess) and not self.wordObjects.__contains__(guess):
            self.wordObjects[self.activeIndex]=guess
            self.activeIndex+=1
            printUtils.printer(True,"Valid guess")
            self.printWordObject()
            self.guessesMade+=1
            if self.wordToBeGuessed==guess:
                printUtils.printer(True,"You successfully got the word")
                self.printWordObject()
                gameOver=True
            if self.guessesMade==self.wordLength:
                self.printWordObject()
                gameOver=True
            return gameOver
        else:
            printUtils.printer(False,"Invalid Input - Word not in word dictionary or Word has been guessed")
            return gameOver
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