import secrets
from getAllowedTypes import *
from contains import *
sets = ['lower','upper','numerals','specialChars']

def getRandomizedCharOptionFromRules(numChars, rules):
    allowedCount = getMinViableCountAndRandRemainder(numChars, rules)
    out = tryAndGetCharOptions(numChars, rules,allowedCount)
    while len(out) == 0:
        print("WARNING: Unable to create a password based off the chardex, repchars, and set mincount rules\n")
        print("Please increase the length of the password or loosen those rules\n")
        print("Trying again, press Cntrl+C to kill the program\n")
        out = tryAndGetCharOptions(numChars, rules,allowedCount)
    return out

def getMinViableCountAndRandRemainder(numChars, rules):
    allowedCount = []
    for mincount in rules['mincount']:
        for i in range(mincount['val']):
            allowedCount.append(mincount['set'])
    for i in range(len(allowedCount), numChars):
        allowedCount.append(secrets.choice(sets))
    return allowedCount

def tryAndGetCharOptions(numChars, rules,allowedCount):
    types = getAllowedTypes(numChars, rules)
    chosen = []
    for dex in types:
        choices = []
        for opt in sets:
            if containsAny(dex.split(','),[opt]) and containsAny(allowedCount,[opt]):
                choices.append(opt)
        if not containsAny(choices,allowedCount):
            return []
        chosen.append(sets.index(secrets.choice(choices)))
        allowedCount.remove(sets[chosen[-1]])
    return chosen
