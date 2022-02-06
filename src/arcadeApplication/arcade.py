import os,sys
if None==os.getenv("PROJECTROOT"):
    os.environ["PROJECTROOT"]=os.getcwd()
sys.path.append(os.getenv("PROJECTROOT")+"\\src")
from wordGames import basicHangman,wordle
#TODO Break-down of game is make guess->handle guess->continue/end game

def runGame(game):
    newGame = classGameNames[game]()
    while True:
        output = newGame.runGameLogic()
        if output == True:
            break
    return True

userOptions = ["play","quit"]
classGameNames = {"hangman":basicHangman.basicHangman,"wordle":wordle.wordleClass}

def arcadeLogic():
    while True:
        print(f"Which game would you like to play today. We have :\n {[i for i in classGameNames.keys()]}")
        userInput = input().lower().lstrip(" ").rstrip(" ")
        if userInput=="quit":
            print(f"Goodbye")
            break
        if not userInput in classGameNames.keys():
            print("I don't know how to play that game")
        else:
            print(f"Okay, lets play {userInput}")
            while True:
                if runGame(userInput)==True:
                    break
