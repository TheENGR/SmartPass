import sqlite3
conn = sqlite3.connect('words.db')

c = conn.cursor()

# Create table

# Types:
#  (0) LowerCase
#  (1) UpperCase
#  (2) Numerics
#  (3) Symbol
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

c.execute('DROP TABLE words')
c.execute('CREATE TABLE IF NOT EXISTS words (Type int, Word text, Symbol text, GrammarType int, GrammarQualifier int)')

# Add Refrences
#c.execute("INSERT INTO words VALUES (2, 'life, the universe, and everything', '42', 5, 0)")

# Add Punctuation
c.execute("INSERT INTO words VALUES (3, '.', '.', 10, 0)")
c.execute("INSERT INTO words VALUES (3, '?', '?', 10, 0)")
c.execute("INSERT INTO words VALUES (3, '!', '!', 10, 0)")
c.execute("INSERT INTO words VALUES (3, '|', '|', 10, 0)")
c.execute("INSERT INTO words VALUES (3, ';', ';', 10, 0)")
c.execute("INSERT INTO words VALUES (1, '.', 'P', 10, 0)")
c.execute("INSERT INTO words VALUES (0, '?', 'q', 10, 0)")
c.execute("INSERT INTO words VALUES (1, '!', 'E', 10, 0)")
c.execute("INSERT INTO words VALUES (0, ';', 's', 10, 0)")

# Add How Adverbs
c.execute("INSERT INTO words VALUES (3, 'immediately', '1', 1, 11)")
c.execute("INSERT INTO words VALUES (3, 'secondly', '2', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'absentmindedly', 'a', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'awkwardly', 'a', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'beautifully', 'b', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'briskly', 'b', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'cheerfully', 'c', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'carefully', 'c', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'effortlessly', 'e', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'gracefully', 'g', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'grimly', 'g', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'happily', 'h', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'hungrily', 'h', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'lazily', 'l', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'loyally', 'l', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'quickly', 'q', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'ruthlessly', 'r', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'savagely', 's', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'sloppily', 's', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'affectionately', 'a', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'daringly', 'd', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'defiantly', 'd', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'dastardly', 'd', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'eagerly', 'e', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'enthusiastically', 'e', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'faithfully', 'f', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'ferociously', 'f', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'frantically', 'f', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'graciously', 'g', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'grudgingly', 'g', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'habitually', 'h', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'hauntingly', 'h', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'icily', 'i', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'infrequently', 'i', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'intelligently', 'i', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'jauntily', 'j', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'jubilantly', 'j', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'kindheartedly', 'k', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'knavishly', 'k', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'magically', 'm', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'mechanically', 'm', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'naturally', 'n', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'nervously', 'n', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'optimistically', 'o', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'obnoxiously', 'o', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'painlessly', 'p', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'powerfully', 'p', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'quaintly', 'q', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'quizzically', 'q', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'reassuringly', 'r', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'rapidly', 'r', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'sleepily', 's', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'shrilly', 's', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'truthfully', 't', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'terribly', 't', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'tenderly', 't', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'unabashedly', 'u', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'unemotionally', 'u', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'unfailingly', 'u', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'vainly', 'v', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'verbally', 'v', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'voluntarily', 'v', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'wickedly', 'w', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'wearily', 'w', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'wetly', 'w', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'youthfully', 'y', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'zanily', 'z', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'zestily', 'z', 1, 11)")
c.execute("INSERT INTO words VALUES (0, 'zealously', 'z', 1, 11)")

# Add Nouns
c.execute("INSERT INTO words VALUES (0, 'apple', 'a', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'bed', 'b', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'building', 'b', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'house', 'h', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'room', 'r', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'floor', 'f', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'sister', 's', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'brother', 'b', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'father', 'f', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'mother', 'm', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'cousin', 'c', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'picture', 'p', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'soap', 's', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'deer', 'd', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'trail', 't', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'home', 'h', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'debt', 'd', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'maid', 'm', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'song', 's', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'motion', 'm', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'company', 'c', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'spoon', 's', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'afterthought', 'a', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'door', 'd', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'ladybug', 'l', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'umbrella', 'u', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'celery', 'c', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'liquid', 'l', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'fork', 'f', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'office', 'o', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'impulse', 'i', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'kittens', 'k', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'flag', 'f', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'plastic', 'p', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'cover', 'c', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'spring', 's', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'boot', 'b', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'side', 's', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'book', 'b', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'sound', 's', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'relation', 'r', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'cactus', 'c', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'tooth', 't', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'scissors', 's', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'pokemon', 'p', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'wheel', 'w', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'river', 'r', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'friend', 'f', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'friends', 'f', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'limit', 'l', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'horse', 'h', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'earth', 'e', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'wax', 'w', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'quicksand', 'q', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'wing', 'w', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'wrist', 'w', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'volleyball', 'v', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'doctor', 'd', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'class', 'c', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'apparatus', 'a', 5, 0)")
c.execute("INSERT INTO words VALUES (0, 'computer', 'c', 5, 0)")

# Add Articles & Determiners
c.execute("INSERT INTO words VALUES (0, 'a', 'a', 2, 0)")
c.execute("INSERT INTO words VALUES (0, 'an', 'a', 2, 0)")
c.execute("INSERT INTO words VALUES (0, 'the', 't', 2, 0)")
c.execute("INSERT INTO words VALUES (0, 'his', 'h', 2, 0)")
c.execute("INSERT INTO words VALUES (0, 'her', 'h', 2, 0)")
#c.execute("INSERT INTO words VALUES (0, 'mine', 'm', 2, 0)")
#c.execute("INSERT INTO words VALUES (0, 'theirs', 't', 2, 0)")
c.execute("INSERT INTO words VALUES (0, 'your', 'y', 2, 0)")
c.execute("INSERT INTO words VALUES (0, 'their', 't', 2, 0)")
c.execute("INSERT INTO words VALUES (0, 'our', 'o', 2, 0)")
#c.execute("INSERT INTO words VALUES (0, 'yours', 'y', 2, 0)")
#c.execute("INSERT INTO words VALUES (0, 'hers', 'h', 2, 0)")
c.execute("INSERT INTO words VALUES (0, 'its', 'i', 2, 0)")
c.execute("INSERT INTO words VALUES (0, 'ours', 'o', 2, 0)")
c.execute("INSERT INTO words VALUES (0, 'my', 'm', 2, 0)")
c.execute("INSERT INTO words VALUES (1, 'My', 'M', 2, 0)")
c.execute("INSERT INTO words VALUES (1, 'His', 'H', 2, 0)")
c.execute("INSERT INTO words VALUES (1, 'Her', 'H', 2, 0)")
c.execute("INSERT INTO words VALUES (1, 'Your', 'Y', 2, 0)")
c.execute("INSERT INTO words VALUES (1, 'Their', 'T', 2, 0)")
c.execute("INSERT INTO words VALUES (1, 'Our', 'O', 2, 0)")
c.execute("INSERT INTO words VALUES (1, 'Its', 'I', 2, 0)")
c.execute("INSERT INTO words VALUES (1, 'A', 'A', 2, 0)")
c.execute("INSERT INTO words VALUES (1, 'An', 'A', 2, 0)")
c.execute("INSERT INTO words VALUES (1, 'The', 'T', 2, 0)")
c.execute("INSERT INTO words VALUES (1, 'Bobby''s', 'B', 2, 0)")
c.execute("INSERT INTO words VALUES (1, 'Billy''s', 'B', 2, 0)")
c.execute("INSERT INTO words VALUES (1, 'Abby''s', 'A', 2, 0)")
c.execute("INSERT INTO words VALUES (1, 'Carl''s', 'C', 2, 0)")
c.execute("INSERT INTO words VALUES (1, 'Don''s', 'D', 2, 0)")
c.execute("INSERT INTO words VALUES (1, 'Enid''s', 'E', 2, 0)")
c.execute("INSERT INTO words VALUES (1, 'Frank''s', 'F', 2, 0)")
c.execute("INSERT INTO words VALUES (1, 'Gertrude''s', 'G', 2, 0)")
c.execute("INSERT INTO words VALUES (1, 'Harry''s', 'H', 2, 0)")
c.execute("INSERT INTO words VALUES (1, 'Ingrid''s', 'I', 2, 0)")
c.execute("INSERT INTO words VALUES (1, 'Jill''s', 'J', 2, 0)")
c.execute("INSERT INTO words VALUES (1, 'Kevin''s', 'K', 2, 0)")
c.execute("INSERT INTO words VALUES (1, 'Luke''s', 'L', 2, 0)")
c.execute("INSERT INTO words VALUES (1, 'Mark''s', 'M', 2, 0)")
c.execute("INSERT INTO words VALUES (1, 'Nancy''s', 'N', 2, 0)")
c.execute("INSERT INTO words VALUES (1, 'Obed''s', 'O', 2, 0)")
c.execute("INSERT INTO words VALUES (1, 'Paul''s', 'P', 2, 0)")
c.execute("INSERT INTO words VALUES (1, 'Quincy''s', 'Q', 2, 0)")
c.execute("INSERT INTO words VALUES (1, 'Ralph''s', 'R', 2, 0)")
c.execute("INSERT INTO words VALUES (1, 'Snape''s', 'S', 2, 0)")
c.execute("INSERT INTO words VALUES (1, 'Terry''s', 'T', 2, 0)")
c.execute("INSERT INTO words VALUES (1, 'Uriah''s', 'U', 2, 0)")
c.execute("INSERT INTO words VALUES (1, 'Vince''s', 'V', 2, 0)")
c.execute("INSERT INTO words VALUES (1, 'Will''s', 'W', 2, 0)")

# Add Numbers
c.execute("INSERT INTO words VALUES (2, 'zero', '0', 0, 0)")
c.execute("INSERT INTO words VALUES (2, 'one', '1', 0, 0)")
c.execute("INSERT INTO words VALUES (2, 'two', '2', 0, 0)")
c.execute("INSERT INTO words VALUES (2, 'three', '3', 0, 0)")
c.execute("INSERT INTO words VALUES (2, 'four', '4', 0, 0)")
c.execute("INSERT INTO words VALUES (2, 'five', '5', 0, 0)")
c.execute("INSERT INTO words VALUES (2, 'six', '6', 0, 0)")
c.execute("INSERT INTO words VALUES (2, 'seven', '7', 0, 0)")
c.execute("INSERT INTO words VALUES (2, 'eight', '8', 0, 0)")
c.execute("INSERT INTO words VALUES (2, 'nine', '9', 0, 0)")
c.execute("INSERT INTO words VALUES (0, 'ten', 't', 0, 0)")
c.execute("INSERT INTO words VALUES (0, 'eleven', 'e', 0, 0)")
c.execute("INSERT INTO words VALUES (0, 'twelve', 't', 0, 0)")

# Add Conjunctions
c.execute("INSERT INTO words VALUES (0, 'for', 'f', 3, 0)")
c.execute("INSERT INTO words VALUES (2, 'for', '4', 3, 0)")
c.execute("INSERT INTO words VALUES (0, 'and', 'a', 3, 0)")
c.execute("INSERT INTO words VALUES (3, 'and', '&', 3, 0)")
c.execute("INSERT INTO words VALUES (0, 'nor', 'n', 3, 0)")
c.execute("INSERT INTO words VALUES (3, 'nor', '!|', 3, 0)")
c.execute("INSERT INTO words VALUES (0, 'but', 'b', 3, 0)")
c.execute("INSERT INTO words VALUES (0, 'or', 'o', 3, 0)")
c.execute("INSERT INTO words VALUES (3, 'or', '|', 3, 0)")
c.execute("INSERT INTO words VALUES (0, 'yet', 'y', 3, 0)")
c.execute("INSERT INTO words VALUES (0, 'so', 's', 3, 0)")

# Add Past Tense Verbs
c.execute("INSERT INTO words VALUES (0, 'added', 'a', 9, 17)")
c.execute("INSERT INTO words VALUES (3, 'added', '+', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'afforded', 'a', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'answered', 'a', 9, 17)")
c.execute("INSERT INTO words VALUES (3, 'answered', '=', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'banged', 'b', 9, 17)")
c.execute("INSERT INTO words VALUES (3, 'banged', '!', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'begged', 'b', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'borrowed', 'b', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'claped', 'c', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'contained', 'c', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'detected', 'd', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'developed', 'd', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'drowned', 'd', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'educated', 'e', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'emptied', 'e', 9, 17)")
c.execute("INSERT INTO words VALUES (2, 'emptied', '0', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'existed', 'e', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'fastened', 'f', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'flashed', 'f', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'greased', 'g', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'guaranteed', 'g', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'hammered', 'h', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'equaled', 'e', 9, 17)")
c.execute("INSERT INTO words VALUES (3, 'equaled', '=', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'interrupted', 'i', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'imagined', 'i', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'jumped', 'j', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'kissed', 'k', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'knocked', 'k', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'learned', 'l', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'listened', 'l', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'managed', 'm', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'measured', 'm', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'multiplied', 'm', 9, 17)")
c.execute("INSERT INTO words VALUES (3, 'multiplied', '*', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'noticed', 'n', 9, 17)")
c.execute("INSERT INTO words VALUES (3, 'numbered', '#', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'numbered', 'n', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'objected', 'o', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'overflowed', 'o', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'placed', 'p', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'protected', 'p', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'divided', 'd', 9, 17)")
c.execute("INSERT INTO words VALUES (3, 'divided', '/', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'questioned', 'q', 9, 17)")
c.execute("INSERT INTO words VALUES (3, 'questioned', '?', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'released', 'r', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'removed', 'r', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'removed', 'r', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'satisfied', 's', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'smelled', 's', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'squashed', 's', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'supplied', 's', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'teased', 't', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'transported', 't', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'turned', 't', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'unfastened', 'u', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'unlocked', 'u', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'visited', 'v', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'wandered', 'w', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'whispered', 'w', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'x-rayed', 'x', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'yawned', 'y', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'yelled', 'y', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'ziped', 'z', 9, 17)")
c.execute("INSERT INTO words VALUES (0, 'zoomed', 'z', 9, 17)")

# Add Prepositions
c.execute("INSERT INTO words VALUES (0, 'aboard', 'a', 7, 0)")
c.execute("INSERT INTO words VALUES (3, '~about', '~', 7, 0)")
c.execute("INSERT INTO words VALUES (3, '@at', '@', 7, 0)")
c.execute("INSERT INTO words VALUES (0, 'aboard', 'a', 7, 0)")
c.execute("INSERT INTO words VALUES (0, 'at', 'a', 7, 0)")
c.execute("INSERT INTO words VALUES (0, 'bebeath', 'b', 7, 0)")
c.execute("INSERT INTO words VALUES (3, 'beneath', '_', 7, 0)")
c.execute("INSERT INTO words VALUES (3, 'except', '!', 7, 0)")
c.execute("INSERT INTO words VALUES (0, 'except', 'e', 7, 0)")
c.execute("INSERT INTO words VALUES (0, 'in', 'i', 7, 0)")
c.execute("INSERT INTO words VALUES (0, 'like', 'l', 7, 0)")
c.execute("INSERT INTO words VALUES (0, 'from', 'f', 7, 0)")
c.execute("INSERT INTO words VALUES (0, 'during', 'd', 7, 0)")
c.execute("INSERT INTO words VALUES (3, 'minus', '-', 7, 0)")
c.execute("INSERT INTO words VALUES (0, 'minus', 'm', 7, 0)")
c.execute("INSERT INTO words VALUES (0, 'near', 'n', 7, 0)")
c.execute("INSERT INTO words VALUES (0, 'over', 'o', 7, 0)")
c.execute("INSERT INTO words VALUES (3, 'plus', '+', 7, 0)")
c.execute("INSERT INTO words VALUES (0, 'plus', 'p', 7, 0)")
c.execute("INSERT INTO words VALUES (0, 'since', 's', 7, 0)")
c.execute("INSERT INTO words VALUES (3, 'than', 't', 7, 0)")
c.execute("INSERT INTO words VALUES (3, 'greater than', '>', 7, 0)")
c.execute("INSERT INTO words VALUES (3, 'less than', '<', 7, 0)")
c.execute("INSERT INTO words VALUES (0, 'under', 'u', 7, 0)")
c.execute("INSERT INTO words VALUES (0, 'via', 'v', 7, 0)")
c.execute("INSERT INTO words VALUES (0, 'upon', 'u', 7, 0)")
c.execute("INSERT INTO words VALUES (0, 'with', 'w', 7, 0)")

# Add Quantity
c.execute("INSERT INTO words VALUES (0, 'abundant', 'a', 0, 0)")
c.execute("INSERT INTO words VALUES (0, 'bunch', 'b', 0, 0)")
c.execute("INSERT INTO words VALUES (0, 'couple', 'c', 0, 0)")
c.execute("INSERT INTO words VALUES (0, 'double', 'd', 0, 0)")
c.execute("INSERT INTO words VALUES (0, 'empty', 'e', 0, 0)")
c.execute("INSERT INTO words VALUES (0, 'few', 'f', 0, 0)")
c.execute("INSERT INTO words VALUES (0, 'great', 'g', 0, 0)")
c.execute("INSERT INTO words VALUES (0, 'huge', 'h', 0, 0)")
c.execute("INSERT INTO words VALUES (0, 'insufficient', 'i', 0, 0)")
#c.execute("INSERT INTO words VALUES (0, '', 'j', 0, 0)")
#c.execute("INSERT INTO words VALUES (0, '', 'k', 0, 0)")
c.execute("INSERT INTO words VALUES (0, 'light', 'l', 0, 0)")
c.execute("INSERT INTO words VALUES (0, 'many', 'm', 0, 0)")
c.execute("INSERT INTO words VALUES (0, 'numerous', 'n', 0, 0)")
#c.execute("INSERT INTO words VALUES (0, '', 'o', 0, 0)")
c.execute("INSERT INTO words VALUES (0, 'plenty', 'p', 0, 0)")
#c.execute("INSERT INTO words VALUES (0, '', 'q', 0, 0)")
#c.execute("INSERT INTO words VALUES (0, '', 'r', 0, 0)")
c.execute("INSERT INTO words VALUES (0, 'several', 's', 0, 0)")
#c.execute("INSERT INTO words VALUES (0, '', 't', 0, 0)")
#c.execute("INSERT INTO words VALUES (0, '', 'u', 0, 0)")
#c.execute("INSERT INTO words VALUES (0, '', 'v', 0, 0)")
c.execute("INSERT INTO words VALUES (0, 'whole', 'w', 0, 0)")
#c.execute("INSERT INTO words VALUES (0, '', 'x', 0, 0)")
#c.execute("INSERT INTO words VALUES (0, '', 'y', 0, 0)")
#c.execute("INSERT INTO words VALUES (0, '', 'z', 0, 0)")

# Add Quality
c.execute("INSERT INTO words VALUES (0, 'amazing', 'a', 0, 1)")
c.execute("INSERT INTO words VALUES (0, 'bizarre', 'b', 0, 1)")
c.execute("INSERT INTO words VALUES (0, 'crude', 'c', 0, 1)")
c.execute("INSERT INTO words VALUES (0, 'dwarfed', 'd', 0, 1)")
c.execute("INSERT INTO words VALUES (0, 'exceptional', 'e', 0, 1)")
c.execute("INSERT INTO words VALUES (0, 'feeble', 'f', 0, 1)")
c.execute("INSERT INTO words VALUES (0, 'gnarly', 'g', 0, 1)")
c.execute("INSERT INTO words VALUES (0, 'humble', 'h', 0, 1)")
c.execute("INSERT INTO words VALUES (0, 'insufficient', 'i', 0, 1)")
c.execute("INSERT INTO words VALUES (0, 'junior', 'j', 0, 1)")
#c.execute("INSERT INTO words VALUES (0, '', 'k', 0, 1)")
c.execute("INSERT INTO words VALUES (0, 'lowly', 'l', 0, 1)")
c.execute("INSERT INTO words VALUES (0, 'modest', 'm', 0, 1)")
c.execute("INSERT INTO words VALUES (0, 'normal', 'n', 0, 1)")
c.execute("INSERT INTO words VALUES (0, 'outstanding', 'o', 0, 1)")
c.execute("INSERT INTO words VALUES (0, 'premium', 'p', 0, 1)")
#c.execute("INSERT INTO words VALUES (0, '', 'q', 0, 1)")
c.execute("INSERT INTO words VALUES (0, 'rotten', 'r', 0, 1)")
c.execute("INSERT INTO words VALUES (0, 'shabby', 's', 0, 1)")
c.execute("INSERT INTO words VALUES (0, 'transcendent', 't', 0, 1)")
c.execute("INSERT INTO words VALUES (0, 'unparalleled', 'u', 0, 1)")
c.execute("INSERT INTO words VALUES (0, 'valueless', 'v', 0, 1)")
c.execute("INSERT INTO words VALUES (0, 'worthless', 'w', 0, 1)")
#c.execute("INSERT INTO words VALUES (0, '', 'x', 0, 1)")
#c.execute("INSERT INTO words VALUES (0, '', 'y', 0, 1)")
#c.execute("INSERT INTO words VALUES (0, '', 'z', 0, 1)")

# Add Size
c.execute("INSERT INTO words VALUES (0, 'ample', 'a', 0, 2)")
c.execute("INSERT INTO words VALUES (0, 'big', 'b', 0, 2)")
c.execute("INSERT INTO words VALUES (0, 'corpulent', 'c', 0, 2)")
c.execute("INSERT INTO words VALUES (0, 'diminutive', 'd', 0, 2)")
c.execute("INSERT INTO words VALUES (0, 'expansive', 'e', 0, 2)")
c.execute("INSERT INTO words VALUES (0, 'fat', 'f', 0, 2)")
c.execute("INSERT INTO words VALUES (0, 'gigantic', 'g', 0, 2)")
c.execute("INSERT INTO words VALUES (0, 'heavy', 'h', 0, 2)")
c.execute("INSERT INTO words VALUES (0, 'infinitesimal', 'i', 0, 2)")
c.execute("INSERT INTO words VALUES (0, 'jumbo', 'j', 0, 2)")
c.execute("INSERT INTO words VALUES (0, 'knee-high', 'k', 0, 2)")
c.execute("INSERT INTO words VALUES (0, 'large', 'l', 0, 2)")
c.execute("INSERT INTO words VALUES (1, 'Lilliputian', 'l', 0, 2)") # THIS IS SPECIAL BUT I LIKE IT
c.execute("INSERT INTO words VALUES (0, 'miniature', 'm', 0, 2)")
c.execute("INSERT INTO words VALUES (0, 'narrow', 'n', 0, 2)")
c.execute("INSERT INTO words VALUES (0, 'oversized', 'o', 0, 2)")
c.execute("INSERT INTO words VALUES (0, 'plump', 'p', 0, 2)")
c.execute("INSERT INTO words VALUES (0, 'quaint', 'q', 0, 2)")
c.execute("INSERT INTO words VALUES (0, 'rotund', 'r', 0, 2)")
c.execute("INSERT INTO words VALUES (0, 'small', 's', 0, 2)")
c.execute("INSERT INTO words VALUES (0, 'towering', 't', 0, 2)")
c.execute("INSERT INTO words VALUES (0, 'undersized', 'u', 0, 2)")
c.execute("INSERT INTO words VALUES (0, 'vast', 'v', 0, 2)")
c.execute("INSERT INTO words VALUES (0, 'wide', 'w', 0, 2)")
#c.execute("INSERT INTO words VALUES (0, '', 'x', 0, 2)")
#c.execute("INSERT INTO words VALUES (0, '', 'y', 0, 2)")
#c.execute("INSERT INTO words VALUES (0, '', 'z', 0, 2)")

# Add Shapes
c.execute("INSERT INTO words VALUES (0, 'arced', 'a', 0, 4)")
c.execute("INSERT INTO words VALUES (0, 'bilateral', 'b', 0, 4)")
c.execute("INSERT INTO words VALUES (0, 'conical', 'c', 0, 4)")
c.execute("INSERT INTO words VALUES (0, 'dodecahedron', 'd', 0, 4)")
c.execute("INSERT INTO words VALUES (0, 'ellipsoid', 'e', 0, 4)")
c.execute("INSERT INTO words VALUES (0, 'flat', 'f', 0, 4)")
c.execute("INSERT INTO words VALUES (0, 'gnomon', 'g', 0, 4)")
c.execute("INSERT INTO words VALUES (0, 'hexagonal', 'h', 0, 4)")
c.execute("INSERT INTO words VALUES (0, 'icosahedron', 'i', 0, 4)")
#c.execute("INSERT INTO words VALUES (0, '', 'j', 0, 4)")
c.execute("INSERT INTO words VALUES (0, 'kite', 'k', 0, 4)")
c.execute("INSERT INTO words VALUES (0, 'linear', 'l', 0, 4)")
c.execute("INSERT INTO words VALUES (0, 'mobius', 'm', 0, 4)")
c.execute("INSERT INTO words VALUES (0, 'nonagon', 'n', 0, 4)")
c.execute("INSERT INTO words VALUES (0, 'oval', 'o', 0, 4)")
c.execute("INSERT INTO words VALUES (0, 'pointed', 'p', 0, 4)")
c.execute("INSERT INTO words VALUES (0, 'quadrilateral', 'q', 0, 4)")
c.execute("INSERT INTO words VALUES (0, 'round', 'r', 0, 4)")
c.execute("INSERT INTO words VALUES (0, 'square', 's', 0, 4)")
c.execute("INSERT INTO words VALUES (0, 'triangular', 't', 0, 4)")
#c.execute("INSERT INTO words VALUES (0, '', 'u', 0, 4)")
#c.execute("INSERT INTO words VALUES (0, '', 'v', 0, 4)")
c.execute("INSERT INTO words VALUES (0, 'wedge', 'w', 0, 4)")
c.execute("INSERT INTO words VALUES (0, 'cross', 'x', 0, 4)")
#c.execute("INSERT INTO words VALUES (0, '', 'y', 0, 4)")
#c.execute("INSERT INTO words VALUES (0, '', 'z', 0, 4)")
c.execute("INSERT INTO words VALUES (3, 'hash', '#', 0, 4)")
c.execute("INSERT INTO words VALUES (3, 'arrow', '<', 0, 4)")
c.execute("INSERT INTO words VALUES (3, 'linear', '|', 0, 4)")
c.execute("INSERT INTO words VALUES (3, 'star', '*', 0, 4)")
c.execute("INSERT INTO words VALUES (3, 'point', '.', 0, 4)")
c.execute("INSERT INTO words VALUES (3, 'swirl', '@', 0, 4)")
c.execute("INSERT INTO words VALUES (2, 'oval', '0', 0, 4)")

# Add Age
c.execute("INSERT INTO words VALUES (0, 'adolescent', 'a', 0, 5)")
c.execute("INSERT INTO words VALUES (0, 'bygone', 'b', 0, 5)")
c.execute("INSERT INTO words VALUES (0, 'childish', 'c', 0, 5)")
c.execute("INSERT INTO words VALUES (0, 'decrepit', 'd', 0, 5)")
c.execute("INSERT INTO words VALUES (0, 'elderly', 'e', 0, 5)")
c.execute("INSERT INTO words VALUES (0, 'fledgling', 'f', 0, 5)")
c.execute("INSERT INTO words VALUES (0, 'grizzled', 'g', 0, 5)")
c.execute("INSERT INTO words VALUES (0, 'half-grown', 'h', 0, 5)")
c.execute("INSERT INTO words VALUES (0, 'infant', 'i', 0, 5)")
#c.execute("INSERT INTO words VALUES (0, '', 'j', 0, 5)")
#c.execute("INSERT INTO words VALUES (0, '', 'k', 0, 5)")
c.execute("INSERT INTO words VALUES (0, 'little', 'l', 0, 5)")
c.execute("INSERT INTO words VALUES (0, 'mature', 'm', 0, 5)")
c.execute("INSERT INTO words VALUES (0, 'newborn', 'n', 0, 5)")
c.execute("INSERT INTO words VALUES (0, 'old', 'o', 0, 5)")
c.execute("INSERT INTO words VALUES (0, 'primordial', 'p', 0, 5)")
#c.execute("INSERT INTO words VALUES (0, '', 'q', 0, 5)")
c.execute("INSERT INTO words VALUES (0, 'relic', 'r', 0, 5)")
c.execute("INSERT INTO words VALUES (0, 'senile', 's', 0, 5)")
c.execute("INSERT INTO words VALUES (0, 'timeworn', 't', 0, 5)")
c.execute("INSERT INTO words VALUES (0, 'undeveloped', 'u', 0, 5)")
c.execute("INSERT INTO words VALUES (0, 'veteran', 'v', 0, 5)")
c.execute("INSERT INTO words VALUES (0, 'wasted', 'w', 0, 5)")
#c.execute("INSERT INTO words VALUES (0, '', 'x', 0, 5)")
c.execute("INSERT INTO words VALUES (0, 'young', 'y', 0, 5)")
#c.execute("INSERT INTO words VALUES (0, '', 'z', 0, 5)")

# Add Colors
c.execute("INSERT INTO words VALUES (0, 'aquamarine', 'a', 0, 6)")
c.execute("INSERT INTO words VALUES (0, 'brass', 'b', 0, 6)")
c.execute("INSERT INTO words VALUES (0, 'cerulean', 'c', 0, 6)")
c.execute("INSERT INTO words VALUES (0, 'denim', 'd', 0, 6)")
c.execute("INSERT INTO words VALUES (0, 'emerald', 'e', 0, 6)")
c.execute("INSERT INTO words VALUES (0, 'fuchsia', 'f', 0, 6)")
c.execute("INSERT INTO words VALUES (0, 'gold', 'g', 0, 6)")
c.execute("INSERT INTO words VALUES (0, 'heliotrope', 'h', 0, 6)")
c.execute("INSERT INTO words VALUES (0, 'indigo', 'i', 0, 6)")
c.execute("INSERT INTO words VALUES (0, 'jade', 'j', 0, 6)")
c.execute("INSERT INTO words VALUES (0, 'khaki', 'k', 0, 6)")
c.execute("INSERT INTO words VALUES (0, 'lime', 'l', 0, 6)")
c.execute("INSERT INTO words VALUES (0, 'mustard', 'm', 0, 6)")
c.execute("INSERT INTO words VALUES (0, 'navy', 'n', 0, 6)")
c.execute("INSERT INTO words VALUES (0, 'olive', 'o', 0, 6)")
c.execute("INSERT INTO words VALUES (0, 'peach', 'p', 0, 6)")
c.execute("INSERT INTO words VALUES (0, 'quartz', 'q', 0, 6)")
c.execute("INSERT INTO words VALUES (0, 'red', 'r', 0, 6)")
c.execute("INSERT INTO words VALUES (0, 'scarlet', 's', 0, 6)")
c.execute("INSERT INTO words VALUES (0, 'teal', 't', 0, 6)")
c.execute("INSERT INTO words VALUES (0, 'ultramarine', 'u', 0, 6)")
c.execute("INSERT INTO words VALUES (0, 'violet', 'v', 0, 6)")
c.execute("INSERT INTO words VALUES (0, 'white', 'w', 0, 6)")
c.execute("INSERT INTO words VALUES (0, 'xanathic', 'x', 0, 6)")
c.execute("INSERT INTO words VALUES (0, 'yellow', 'y', 0, 6)")
c.execute("INSERT INTO words VALUES (0, 'zucchini', 'z', 0, 6)")

# Add Names (Proper Nouns)
c.execute("INSERT INTO words VALUES (1, 'Beth', 'B', 6, 0)")
c.execute("INSERT INTO words VALUES (1, 'Bill', 'B', 6, 0)")
c.execute("INSERT INTO words VALUES (1, 'Aaron', 'A', 6, 0)")
c.execute("INSERT INTO words VALUES (1, 'Erin', 'E', 6, 0)")
c.execute("INSERT INTO words VALUES (1, 'Caleb', 'C', 6, 0)")
c.execute("INSERT INTO words VALUES (1, 'Devin', 'D', 6, 0)")
c.execute("INSERT INTO words VALUES (1, 'Ellen', 'E', 6, 0)")
c.execute("INSERT INTO words VALUES (1, 'Fred', 'F', 6, 0)")
c.execute("INSERT INTO words VALUES (1, 'Gregory', 'G', 6, 0)")
c.execute("INSERT INTO words VALUES (1, 'Hillary', 'H', 6, 0)")
c.execute("INSERT INTO words VALUES (1, 'Inigo', 'I', 6, 0)")
c.execute("INSERT INTO words VALUES (1, 'John', 'J', 6, 0)")
c.execute("INSERT INTO words VALUES (1, 'Kelly', 'K', 6, 0)")
c.execute("INSERT INTO words VALUES (1, 'Lizzy', 'L', 6, 0)")
c.execute("INSERT INTO words VALUES (1, 'Mary', 'M', 6, 0)")
c.execute("INSERT INTO words VALUES (1, 'Neptune', 'N', 6, 0)")
c.execute("INSERT INTO words VALUES (1, 'Nathan', 'N', 6, 0)")
c.execute("INSERT INTO words VALUES (1, 'Oscar', 'O', 6, 0)")
c.execute("INSERT INTO words VALUES (1, 'Petunia', 'P', 6, 0)")
c.execute("INSERT INTO words VALUES (1, 'Quin', 'Q', 6, 0)")
c.execute("INSERT INTO words VALUES (1, 'Roy', 'R', 6, 0)")
c.execute("INSERT INTO words VALUES (1, 'Steve', 'S', 6, 0)")
c.execute("INSERT INTO words VALUES (1, 'Trevor', 'T', 6, 0)")
c.execute("INSERT INTO words VALUES (1, 'Urusla', 'U', 6, 0)")
c.execute("INSERT INTO words VALUES (1, 'Valerie', 'V', 6, 0)")
c.execute("INSERT INTO words VALUES (1, 'Will', 'W', 6, 0)")
c.execute("INSERT INTO words VALUES (1, 'Xanathar', 'X', 6, 0)")
c.execute("INSERT INTO words VALUES (1, 'Yuri', 'Y', 6, 0)")
c.execute("INSERT INTO words VALUES (1, 'Zurum', 'Z', 6, 0)")
c.execute("INSERT INTO words VALUES (1, 'Wes', 'W', 6, 0)")
c.execute("INSERT INTO words VALUES (1, 'Grace', 'G', 6, 0)")
c.execute("INSERT INTO words VALUES (1, 'Charlotte', 'C', 6, 0)")
c.execute("INSERT INTO words VALUES (1, 'Drew', 'D', 6, 0)")
c.execute("INSERT INTO words VALUES (1, 'Jake', 'J', 6, 0)")
c.execute("INSERT INTO words VALUES (1, 'Thomas', 'T', 6, 0)")
c.execute("INSERT INTO words VALUES (1, 'Sujith', 'S', 6, 0)")
c.execute("INSERT INTO words VALUES (1, 'Mariana', 'M', 6, 0)")
c.execute("INSERT INTO words VALUES (1, 'Krista', 'K', 6, 0)")
c.execute("INSERT INTO words VALUES (1, 'Jen', 'J', 6, 0)")
c.execute("INSERT INTO words VALUES (1, 'James', 'J', 6, 0)")
c.execute("INSERT INTO words VALUES (1, 'Jameson', 'J', 6, 0)")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
