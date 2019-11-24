from contains import *

f = open("temp.txt", "a")

GT = input("What is the Grammar Type?")
GTQ = input("Grammar Type Qualifier?")

word = input("Word:\n")
while len(word):
    firstLetter = word[0]
    TYPE=0
    if containsAny("!@#$%^&*()_+-=[]{}:`~;',<>./?\|", word[0]):
       word = word[1:]
       TYPE=3
    elif containsAny("0123456789", word[0]):
       TYPE=2
    elif containsAny("ABCDEFGHIJKLMNOPQRSTUVWXYZ", word[0]):
       TYPE=1

    f.write("""c.execute("INSERT INTO words VALUES (""")
    f.write(str(TYPE)+", '"+word+"', '"+firstLetter+"', "+GT+", "+GTQ+""")")\n""")
    word = input()
f.close()
