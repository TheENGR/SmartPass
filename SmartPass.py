import secrets
import json
import setPasswordRules
from randCharArray import *
from countSet import *
from contains import * 

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

numberOfChars = input("How many Characters do you want in your password ("+str(rules['minchars'])+" to "+str(rules['maxchars'])+")?:\n")

try:
    data = int(numberOfChars)
except:
    print("Input must be an integer")
    quit()

if data < rules['minchars']:
    data = rules['minchars']
elif data > rules['maxchars']: 
    data = rules['maxchars']

randCharOptions = randArrayOfAcceptableChars()


## Create Password
password = ""
repeat = 1
while repeat:
    password = ""
    repChars = rules['repchars']
    for i in range(data):
        allowedChars = arrayOfAcceptableCharsForIndex(i)
        if repChars <= data and repChars <= i:
            if password[-1*repChars:] == password[-1]*repChars:
                allowedChars = allowedChars.replace(password[-1], "")
        password += secrets.choice(allowedChars)

    ## Make sure there are enough chars of each type otherwise regenerate
    setCount = countBySet(password, rules)
    repeat = 0
    for mincount in rules['mincount']:
        if setCount[mincount['set']] < mincount['val']:
            repeat = 1

print(password)







        
