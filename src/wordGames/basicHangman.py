from characterManipulation import readFile
# TODO make Hangman object

class basicHangman:
    def __init__(self):
        self._noGuesses=0
        self._wordToBeGuessed = ""
        self._wordCount = 0
        self._stateOfGuess = ""
        self._guesses = []
        self._difficultySet=False
        self._difficultyVal= "easy"
        self._difficulty={"easy":[10,5],"medium":[7,7],"hard":[5,12]}
        self._commands=["start","restart","quit"]

    def handleGuess(self,input):
        if self.wordGuess(input,self._wordToBeGuessed):
            for i in input:
                self._guesses.append(i)
                self.letterGuess(i)
            return True
        if (input in self._guesses)or(self._noGuesses<1):
            return False
        self._guesses.append(input)
        self.letterGuess(input)
        return True
    def letterGuess(self,input):
        if self._wordToBeGuessed.__contains__(input):
            self._stateOfGuess=goodGuess(self._wordToBeGuessed,self._stateOfGuess,input)
            return True
        self._noGuesses -= 1
        return False
    def wordGuess(self,input,match):
        if input==match:
            return True
        return False
    def showGuesses(self):
        return self._guesses
    def showStateOfWorld(self):
        return f"Current State of Word = {self._stateOfGuess}\nYou have {self._noGuesses} guesses\nLetters guessed : {self.showGuesses()}"
    def setDifficulty(self,level):
        self._noGuesses=self._difficulty[level][0]
        self._wordToBeGuessed = readFile.returnLengthWords(0, self._difficulty[level][1])
    def printDifficulty(self):
        print(f"Please provide one of {[i for i in self._difficulty.keys()]}")
    def userSetDifficulty(self):
        self.printDifficulty()
        while True:
            level = input()
            if not level in self._difficulty.keys():
                self.printDifficulty()
            else:
                self.setDifficulty(level)
                break
        self._difficultySet=True
        self._difficultyVal=level
        print(f"Difficulty has been set to {level}")
    def initGame(self):
        self._guesses = []
        if not self._difficultySet:
            self.userSetDifficulty()
        else:
            self.setDifficulty(self._difficultyVal)
        self._wordCount = len(self._wordToBeGuessed)
        self._stateOfGuess= readFile.printBlanks(self._wordCount)
        print(f"Starting a new game\n{self.showStateOfWorld()}")
    def inputCommands(self):
        print(f"## Welcome to Hangman ##\nStart = Start a Game\nQuit = Exit Game\nChange Difficulty = Change the difficulty")
    def runGame(self):
        self.initGame()
        while True:
            print(f"Provide input - Guess a letter, type quit to quit or restart to begin a new game")
            guess = input().lower()
            if (guess == "quit") or guess == "change difficulty":
                return "quit"
            if guess == "restart":
                break
            self.handleGuess(guess)
            if (self.wordGuess(self._wordToBeGuessed, self._stateOfGuess)):
                print("You got the word")
                print(f"Final State\n {self.showStateOfWorld()}")
                break
            elif (self._noGuesses==0):
                print(f"You did not get the word")
                print(f"Final State\n {self.showStateOfWorld()}")
                print(f"The word was - {self._wordToBeGuessed}")
                break
            print(f"{self.showStateOfWorld()}")
        return "OK"
    def runGameLogic(self):
        showInit=True
        while True:
            self.inputCommands()
            userInput = input().lower()
            if userInput=="quit":
                break
            elif userInput=="restart" or userInput == "start":
                if "quit"==self.runGame():
                    break
            elif userInput=="change difficulty":
                self.userSetDifficulty()
        return True

def goodGuess(wordToBeGuessed,currentGuess,guess):
    indexList= readFile.getIndexes(wordToBeGuessed, guess)
    for i in indexList:
        currentGuess= readFile.alterWord(currentGuess, i, guess)
    return currentGuess

