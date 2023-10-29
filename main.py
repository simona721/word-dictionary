from PyDictionary import PyDictionary
 
dictionary = PyDictionary()


while True:
    userInput = input("Enter a word: ")
    if userInput == "":
        break
    print(dictionary.meaning(userInput))
    exitWord = input("Do you want to continue? ")
    if exitWord == "no":
        break

