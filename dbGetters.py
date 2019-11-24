import sqlite3
from contains import *

def getWordChoices(T, GT, GTQ, rules):
    sets = ['lower','upper','numerals','specialChars']
    val = getByTypeGrammarTypeAndQualifier(T, GT, GTQ)
    for swap in rules['swaps']:
        if containsAny(rules[sets[T]],swap['newChar']):
            for newVal in getBySymbolGrammarTypeAndQualifier(swap['oldChar'], GT, GTQ): val.extend([(newVal[0], swap['newChar'])])
    return val

def getByGrammarType(GT):
    conn = sqlite3.connect('words.db')
    c = conn.cursor()
    c.execute("SELECT Word, Symbol From words WHERE GrammarType="+str(int(GT)))
    words=c.fetchall()
    conn.close()
    return words

def getByType(T):
    conn = sqlite3.connect('words.db')
    c = conn.cursor()
    c.execute("SELECT Word, Symbol FROM words WHERE Type="+str(int(T)))
    words=c.fetchall()
    conn.close()
    return words

def getByTypeAndGrammarType(T,GT):
    conn = sqlite3.connect('words.db')
    c = conn.cursor()
    c.execute("SELECT Word, Symbol FROM words WHERE Type="+str(int(T))+" AND GrammarType="+str(int(GT)))
    words=c.fetchall()
    conn.close()
    return words

def getProperNouns():
    conn = sqlite3.connect('words.db')
    c = conn.cursor()
    c.execute("SELECT Word, Symbol FROM words WHERE GrammarType=6")
    words=c.fetchall()
    conn.close()
    return words

def getByGrammarTypeAndQualifier(GT, GTQ):
    conn = sqlite3.connect('words.db')
    c = conn.cursor()
    c.execute("SELECT Word, Symbol FROM words WHERE GrammarType="+str(int(GT))+" AND GrammarQualifier="+str(int(GTQ)))
    words=c.fetchall()
    conn.close()
    return words

def getByTypeGrammarTypeAndQualifier(T, GT, GTQ):
    conn = sqlite3.connect('words.db')
    c = conn.cursor()
    c.execute("SELECT Word, Symbol FROM words WHERE Type="+str(int(T))+" AND GrammarType="+str(int(GT))+" AND GrammarQualifier="+str(int(GTQ)))
    words=c.fetchall()
    conn.close()
    return words

def getBySymbolGrammarTypeAndQualifier(S, GT, GTQ):
    if len(S) != 1:
        return []
    conn = sqlite3.connect('words.db')
    c = conn.cursor()
    c.execute("SELECT Word, Symbol FROM words WHERE Symbol='"+S+"' AND GrammarType="+str(int(GT))+" AND GrammarQualifier="+str(int(GTQ)))
    words=c.fetchall()
    conn.close()
    return words

def getBySymbol(S):
    if len(S) != 1:
        return []
    conn = sqlite3.connect('words.db')
    c = conn.cursor()
    c.execute("SELECT Word, Symbol FROM words WHERE Symbol='"+S+"'")
    words=c.fetchall()
    conn.close()
    return words

def getBySymbolAndType(S, T):
    if len(S) != 1:
        return []
    conn = sqlite3.connect('words.db')
    c = conn.cursor()
    c.execute("SELECT Word, Symbol FROM words WHERE Type="+str(int(T))+" AND Symbol='"+S+"'")
    words=c.fetchall()
    conn.close()
    return words

def getUniqueQualifiersForGrammarType(GT):
    conn = sqlite3.connect('words.db')
    c = conn.cursor()
    c.execute("SELECT DISTINCT GrammarQualifier FROM words WHERE GrammarType="+str(int(GT))+" ORDER BY GrammarQualifier ASC")
    words=c.fetchall()
    conn.close()
    return words
