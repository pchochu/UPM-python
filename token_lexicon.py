import re

class token_lexicon(object):

    tokenLexicon = dict()

    def __init__(self, products, attributes):
        self.products = products
        self.attributes = attributes
        self.preprocess()
        self.tokenLexicon = self.createTokenLexicon()


    def createTokenLexicon(self):
        tokenLexicon = dict()
        count = self.countTokens()
        semantics = self.createSemantics(count)

        for key in count:
            tokenLexicon[key] = dict()
            tokenLexicon[key]['semantic'] = semantics[key]
            tokenLexicon[key]['count'] = count[key]
    
        return tokenLexicon

    def isModel(self, word):
        has_digit = False
        for c in word:
            if c.isdigit(): has_digit = True

            if has_digit:
                return True
        return False

    def isAttribute(self, word, attribute):
        word = word.replace(attribute, '')
        if word.isdigit():
            return True

    def getSemanticOfWord(self, word):
        for attribute in self.attributes:
            if word.lower().endswith(attribute) and self.isAttribute(word.lower(), attribute):
                return 'attribute'
        
        if self.isModel(word): 
            return 'model'

        return 'normal'
        

    def createSemantics(self, tokens):
        semantic = dict()
        for token in tokens:
            semantic[token] = self.getSemanticOfWord(token)
        return semantic

    def countTokens(self):
        count = dict()
        for product in self.products:
            for word in product.split():
                if word not in count:
                    count[word] = 1
                else:
                    count[word] = count[word] + 1
        
        return count

    def preprocess(self):
        self.removeMultipleWhiteSpaces()
        self.toLower()
        self.removePunctuation()
        self.removeDuplicateTokens()
        self.removeWhiteSpaceBeforeProductAttribute()   
        self.removePlus()     

    def removeMultipleWhiteSpaces(self):
        self.product = [re.sub(' +', ' ',item) for item in self.products]

    def toLower(self):
        self.products = [item.lower() for item in self.products]
    
    def removePunctuation(self):
        regex = r'[^A-Za-z0-9.,/\-\\+]+'
        self.products = [re.sub(regex, ' ', item) for item in self.products]

    def uniqueWordsInString(self, string):
        words = string.split()
        unique = " ".join(sorted(set(words), key=words.index))
        return unique

    def removeDuplicateTokens(self):
        self.products = [self.uniqueWordsInString(item) for item in self.products]

    def removeWhiteSpace(self, product):
        for attribute in self.attributes:
            if str(attribute) in product.split():
                product = product.replace(' ' + attribute, attribute)
        
        return product

    def removeWhiteSpaceBeforeProductAttribute(self):
        self.products = [self.removeWhiteSpace(item) for item in self.products]

    def removePlusStation(self, product):
        if '+ station' in product:
            return product.split('+')[0]
        
        return product

    def removePlus(self):
        self.products = [self.removePlusStation(item) for item in self.products]

