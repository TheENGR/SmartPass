import secrets
import json
import setPasswordRules
from randCharArray import *
from countSet import *
from getAllowedTypes import *
from getCharOptions import getRandomizedCharOptionFromRules
from getSentenceStructure import *
from dbGetters import * 

rules = {}
try:
    with open('rules.txt') as json_file:
        rules = json.load(json_file)
except:
    print("Please set your password rules")
    setPasswordRules.main()
    try:
        with open('rules.txt') as json_file:
            rules = json.load(json_file)
    except:
        print("You have to set your rules")
        quit()

numberOfChars = input("How many characters do you want in your password ("+str(rules['minchars'])+" to "+str(rules['maxchars'])+")?:\n")

try:
    numChars = int(numberOfChars)
except:
    print("Input must be an integer")
    quit()

if numChars < rules['minchars']:
    numChars = rules['minchars']
elif numChars > rules['maxchars']:
    numChars = rules['maxchars']

wordTypes = getRandomizedCharOptionFromRules(numChars, rules)
structure = getSentenceStructure(numChars)

password = ""
phrase = ""
for i in range(numChars):
    lib = getWordChoices(wordTypes[i], structure[i]['GT'], structure[i]['GTQ'], rules)
    if len(lib) == 0:
        print("ERROR, could not find a match, data below, please add new swaps or try again\n")
        print("T = " + str(wordTypes[i]) + " GT = " + str(structure[i]['GT'])+ " GTQ = " + str(structure[i]['GTQ']) + "\n")
    selectedWord = secrets.choice(lib)
    password += selectedWord[1]
    if len(phrase) == 0:
        phrase = selectedWord[0]
    elif structure[i]['GT'] == 10:
        phrase += selectedWord[0] + "\n"
    elif phrase[-1] == "\n":
        phrase += selectedWord[0]
    else:
        phrase += " " + selectedWord[0]

print(password)
print(phrase)
