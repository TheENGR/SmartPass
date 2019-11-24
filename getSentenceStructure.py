import random
from dbGetters import getUniqueQualifiersForGrammarType
# Grammar Types:
#  (0)  adjective
#  (1)  adverb
#  (2)  article/determiner
#  (3)  conjunction
#  (4)  interjection
#  (5)  noun
#  (6)  proper noun
#  (7)  preposition
#  (8)  pronoun
#  (9)  verb
#  (10) punctuation 
# Grammar Type Qualifier: 
#  (0)  Quantity or number
#  (1)  Quality or opinion
#  (2)  size
#  (3)  physical quality
#  (4)  shape
#  (5)  age
#  (6)  colour
#  (7)  origin
#  (8)  material
#  (9)  type
#  (10) purpose
#  (11) how
#  (12) when
#  (13) where
#  (14) to what extent
#  (15) comparative
#  (16) present tense
#  (17) past tense

def getSentenceStructure(count):
    numAdjTypes = len(getUniqueQualifiersForGrammarType(0))
    maxStruct1 = 7+2*numAdjTypes

    sentences = []
    while count > maxStruct1:
        sentenceLen = random.randint(4,maxStruct1-1)
        sentences.append(sentenceLen)
        count -= (sentenceLen+1)
    if len(sentences) == 0:
        sentences.append(count)
    else:
        sentences.append(count-1)

    varOut = []
    for sen in sentences:
        varOut.extend(createStructure1(sen))
        varOut.append({'GT':10,'GTQ':0})
    if len(sentences) == 1:
        varOut.pop()
    return varOut

# Min of 4, Max of 7 + 2*number of types of adjective    
def createStructure1(count):
    #Smallest Example: Billy kicked my apple
    adjCount = (0,0)
    if count >= 8:
        # We need Adjectives
        adjCount = divmod(count-7,2)
    
    structure = []
    if count > 5:
        structure.append({'GT':2,'GTQ':0}) # owner ex: my, his
        if (adjCount[0] + adjCount[1]) > 0:
            adjs = createAdjArray((adjCount[0] + adjCount[1]))
            for adj in adjs:
                structure.append({'GT':0,'GTQ':adj}) # adjective
        structure.append({'GT':5,'GTQ':0}) # noun ex: cousin, brother
        
    structure.append({'GT':6,'GTQ':0}) # Name ex: Ellen 
    if count == 5 or count >= 7:
        structure.append({'GT':1,'GTQ':11}) #ly advery for the verb
        
    structure.append({'GT':9,'GTQ':17}) # Past Tense Verb 
    structure.append({'GT':2,'GTQ':0}) # ownerex: my, his
    
    if adjCount[0] > 0:
        adjs = createAdjArray(adjCount[0])
        for adj in adjs:
            structure.append({'GT':0,'GTQ':adj}) # adjective
            
    structure.append({'GT':5,'GTQ':0}) # noun ex: ball, apple
    return structure

def createAdjArray(num):
    qualifiers = []
    for t in getUniqueQualifiersForGrammarType(0):
        qualifiers.append(t[0])
    random.shuffle(qualifiers)
    if num <= len(qualifiers):
        retVal = qualifiers[:num]
        retVal.sort()
        return retVal
    else:
        return []
