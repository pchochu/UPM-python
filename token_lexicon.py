import re

class token_lexicon(object):

    def __init__(self, products, attributes):
        self.products = products
        self.attributes = attributes
        self.preprocess()

    def preprocess(self):
        self.removeMultipleWhiteSpaces()
        self.toLower()
        self.removePunctuation()
        self.removeDuplicateTokens()
        self.removeWhiteSpaceBeforeProductAttribute()        

    def removeMultipleWhiteSpaces(self):
        self.product = [re.sub(' +', ' ',item) for item in self.products]

    def toLower(self):
        self.products = [item.lower() for item in self.products]
    
    def removePunctuation(self):
        regex = '[^A-Za-z0-9.,/-]+'
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

