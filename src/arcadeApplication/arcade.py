from wordGames import basicHangman,wordle

def runHangman():
    newHangman = basicHangman.basicHangman()
    while True:
        output=newHangman.runGameLogic()
        if output==True:
            break
    return True

def runWordle():
    newWordle = wordle.wordleClass()
    while True:
        output=newWordle.runGame()
        if output==True:
            break
    return True


userOptions = ["play","quit"]
games = {"hangman": runHangman,"wordle":runWordle}
def arcadeLogic():
    while True:
        print(f"Which game would you like to play today. We have :\n {[i for i in games.keys()]}")
        userInput = input().lower()
        if userInput=="quit":
            print(f"Goodbye")
            break
        if not userInput in games.keys():
            print("I don't know how to play that game")
        else:
            print(f"Okay, lets play {userInput}")
            while True:
                if games[userInput]()==True:
                    break
