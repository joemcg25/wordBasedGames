import random,os

if os.listdir('.').__contains__("ukenglish.txt"):
    fileName = open("ukenglish.txt", mode="r")
else:
    fileName = open("src/ukenglish.txt", mode="r")
file = fileName.readlines()
for i,j in enumerate(file):
    file[i]=j.removesuffix("\n")
wordLengths=[]
for word in file:
    wordLengths.append(len(word))

def runFunc():
    print("__name__")

def getRandomWord0(words):
    num = random.randint(0,len(words)-1)
    return words[num]

def getRandomWord():
    return getRandomWord0(file)

def genWord():
    return getRandomWord()

def toList(word):
    empty=[]
    for i in word:
        empty.append(i)
    return empty

def toWord(list):
    empty=""
    for i in list:
        empty=empty+i
    return empty

def alterWord(word,index,letter):
    if index>len(word)-1:
        return word
    list=toList(word)
    list[index]=letter
    return toWord(list)

def getIndexes(word,letter):
    empty=[]
    for i,j in enumerate(toList(word)):
        if letter==j:
            empty.append(i)
    return empty

def returnLengthWord(wordLength):
    words=[]
    start=0
    for i, j in enumerate(wordLengths):
        if j == wordLength:
            words.append(file[i])
    return getRandomWord0(words)

def returnLengthWords(wordLengthMin,wordLengthMax):
    words=[]
    start=0
    for i, j in enumerate(wordLengths):
        if j>= wordLengthMin and j<=wordLengthMax:
            words.append(file[i])
    return getRandomWord0(words)

def printBlanks(wordLength):
    return "_" * wordLength

def validWordGuess(guess):
    guess=guess.lower()
    for i in file:
        if guess==i:
            return True
    return False