import random
import json

def getRules():
    rules = {}
    try:
        with open('rules.txt') as json_file:
            rules = json.load(json_file)
            return rules
    except:
        quit()

def randArrayOfAcceptableChars():
    rules = getRules()
    return randFromString(rules['lower']+rules['upper']+rules['numerals']+rules['specialChars'])

def arrayOfAcceptableCharsForIndex(index):
    rules = getRules()
    allowedChars = rules['lower']+rules['upper']+rules['numerals']+rules['specialChars']
    for rule in rules["chardex"]:
        if rule["index"] == index:
            allowedChars = allowedChars.replace(rules[rule["set"]],'')
            
    return allowedChars

def randArrayOfAcceptableCharsForIndex(index):   
    rules = getRules()         
    return randFromString(arrayOfAcceptableCharsForIndex(index))

def randArrayOfLowerCaseLetters():
    rules = getRules()
    return randFromString(rules['lower'])

def randArrayOfUpperCaseLetters():
    rules = getRules()
    return randFromString(rules['upper'])

def randArrayOfNumerals():
    rules = getRules()
    return randFromString(rules['numerals'])

def randArrayOfSpecialChars():
    rules = getRules()
    return randFromString(rules['specialChars'])

def randFromString(STR):
    str_var = list(STR)
    random.shuffle(str_var)
    return ''.join(str_var) 
