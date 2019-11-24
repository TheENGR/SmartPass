import json
from charsInSet import *
from contains import *

sets = ['lower','upper','numerals','specialChars']

def main():
    rules = {}
    rules['lower'] = "abcdefghijklmnopqrstuvwxyz"
    rules['upper'] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rules['numerals'] = "0123456789"
    rules['specialChars'] = "!@#$%^&*()_+-=[]{}:`~;',<>./?\|"
    rules['minchars'] = 10
    rules['maxchars'] = 20
    rules['repchars'] = 5
    rules['chardex'] = []
    rules['mincount'] = []
    rules['swaps'] = []

    lowerQ = ("Do you wish to change the list of lower case letters?\n"
              "Default is " + rules['lower'] + "\n" 
              "Type in your list to change it, press Enter to keep default\n")

    upperQ = ("Do you wish to change the list of upper case letters?\n"
              "Default is " + rules['upper'] + "\n" 
              "Type in your list to change it, press Enter to keep default\n")

    numeralsQ = ("Do you wish to change the list of numerals?\n"
                 "Default is " + rules['numerals'] + "\n" 
                 "Type in your list to change it, press Enter to keep default\n")

    specialQ = ("Do you wish to change the list of special characters?\n"
                "Default is " + rules['specialChars'] + "\n" 
                "Type in your list to change it, press Enter to keep default\n")

    minCharQ = ("Do you wish to change the minimum number of characters?\n"
                "Default is " + str(rules['minchars']) + "\n"
                "Absolute minimun is 4\n"
                "Type in your value to change it, press Enter to keep default\n")

    maxCharQ = ("Do you wish to change the maximum number of characters?\n"
                "Default is " + str(rules['maxchars']) + "\n" 
                "Type in your value to change it, press Enter to keep default\n")

    chardexQ = ("Do you have any rules about which characters are NOT allowed in a specific index?\n"
                "EX: The first(0th) character cannot be a special character\n"
                "Put in the character index followed by a comma then the set which is disallowed\n"
                "EX: 0, specialChars\n"
                "Sets are: lower, upper, numerals, and specialChars\n" 
                "Enter as many as you want, pressing enter between each one\n")

    repcharsQ = ("How many times is a character allowed to be repeated in your password?\n"
                "Default is " + str(rules['repchars']) + "\n"
                "Type in your value to change it, press Enter to keep default\n")

    mincountQ = ("Do you have any rules about which characters sets must have a certain number of chars?\n"
                 "EX: There must be at least 3 numbers and 1 capital letter\n"
                 "Put in the character index followed by a comma then the set which has a minimum count\n"
                 "EX: 3, numerals\n"
                 "Sets are: lower, upper, numerals, and specialChars\n" 
                 "Enter as many as you want, pressing enter between each one\n")

    swapQ = ("Do you have any character swaps you wish to allow?\n"
             "EX: E is 3, a is @, \n"
             "Put in the character to be replaced followed by a comma and the character to replace it\n"
             "EX: E, 3\n"
             "WARNING: This WILL remove the other character from the list, and expand the vocabulary for the second character" 
             "Enter as many as you want, pressing enter between each one\n")

    lower = input(lowerQ)
    if len(lower):
        rules['lower'] = charsInSet(rules['lower'], lower)

    upper = input(upperQ)
    if len(upper):
        rules['upper'] = charsInSet(rules['upper'], upper)

    numerals = input(numeralsQ)
    if len(numerals):
        rules['numerals'] = charsInSet(rules['numerals'], numerals)

    special = input(specialQ)
    if len(special):
        rules['specialChars'] = charsInSet(rules['specialChars'], special)

    minchars = input(minCharQ)
    if len(minchars):
        try:
            if int(minchars) < 4:
                print("ERROR: Value too small, setting to 4")
            rules['minchars'] = max(int(minchars),4)
        except:
            print("Input must be an integer, using default value")

    maxchars = input(maxCharQ)
    if len(maxchars):
        try:
            if int(maxchars) < rules['minchars']:
                print("ERROR: Value too small, setting to the same as the min")
            rules['maxchars'] = max(int(maxchars),rules['minchars'])
        except:
            print("Input must be an integer, using default value")

    repchars = input(repcharsQ)
    if len(repchars):
        try:
            rules['repchars'] = int(repchars)
        except:
            print("Input must be an integer, using default value")

    chardex = input(chardexQ)
    while len(chardex):
        vals = chardex.split(",")
        rules['chardex'].append({"index" : int(vals[0]), "set" : vals[1].strip()})
        chardex = input()

    mincount = input(mincountQ)
    sumOfMins = 0
    while len(mincount):
        vals = mincount.split(",")
        rules['mincount'].append({"val" : int(vals[0]), "set" : vals[1].strip()})
        sumOfMins += int(vals[0])
        if sumOfMins > rules['minchars']:
            print("WARNING:\n")
            print("There are too many minimun requirements to allow for the password to be as short as allowed.\n")
            print("Updating minimum password size to " + str(sumOfMins))
            rules['minchars'] = sumOfMins
        mincount = input()

    swap = input(swapQ)    
    while len(swap):
        vals = swap.split(",")
        rules['swaps'].append({"oldChar" : vals[0].strip(), "newChar" : vals[1].strip()})
        swap = input()

    # Auto Swap missing lower and upper case combos
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    oldChars = ""
    for swap in rules['swaps']:
        oldChars += swap['oldChar']
    print(oldChars)
    for dex in range(len(lower)):
        if containsAny(lower[dex],rules['lower']+oldChars) == 0 and containsAny(upper[dex],rules['upper']) == 1:
            rules['swaps'].append({"oldChar" : lower[dex], "newChar" : upper[dex]})
            oldChars += lower[dex]
        if containsAny(upper[dex],rules['upper']+oldChars) == 0 and containsAny(lower[dex],rules['lower']) == 1:
            rules['swaps'].append({"oldChar" : upper[dex], "newChar" : lower[dex]})
            oldChars += upper[dex]

    # Remove swaped out old chars 
    for swap in rules['swaps']:
        for s in sets:
            rules[s] = rules[s].replace(swap['oldChar'],'')
            
    ##Save to file
    with open('rules.txt', 'w') as outfile:
        json.dump(rules, outfile)
