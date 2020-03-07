from db.conn import DB
from token_lexicon import token_lexicon
from combination_lexicon import combination_lexicon

db = DB()
# db.createDatabase()

mobiles = db.getCellphones()
attributes = db.getAttributes()

cellphones = list()
for mobile in mobiles:
    cellphones.append(mobile[2])

attributesList = list()
for attribute in attributes:
    attributesList.append(attribute[1])

tl = token_lexicon(cellphones, attributesList)
products = tl.products
# db.insertIntoTokenLexicon(tl.tokenLexicon)
cl = combination_lexicon(products)

del db