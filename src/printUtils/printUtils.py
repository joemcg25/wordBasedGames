def printValid(text):
    return f"Valid Input - "+ text
def printInvalid(text):
    return f"Invalid Input - "+ text
def printer(isValid,text):
    if isValid:
        print(printValid(text))
    else:
        print(printInvalid(text))