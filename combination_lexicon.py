from db.conn import DB
import itertools

class combination_lexicon(object):

    def __init__(self, products):
        self.products = products
        self.db = DB()
        self.createCombinationLexicon()

    
    def createCombinationLexicon(self):
        combinationLexicon = dict()
        two_combinations = self.createKCombinations(2)
        three_combinations = self.createKCombinations(3)

        for combination in two_combinations:
            if(len(combination) > 0):
                combinationLexicon[str(combination[0])] = dict()
                combinationLexicon[str(combination[0])]['signature'] = self.computeSignatureOfKCombination(combination[0])

        for combination in three_combinations:
            if(len(combination) > 0):
                combinationLexicon[str(combination[0])] = dict()
                combinationLexicon[str(combination[0])]['signature'] = self.computeSignatureOfKCombination(combination[0])
        
        print(combinationLexicon)

    def computeSignatureOfKCombination(self, k_combination_list_of_words):
        signatureList = list()
        for word in k_combination_list_of_words:
            id = self.db.getIdOfTokenByToken(word.lower())
            signatureList.append(int(id))

        signatureList.sort()
        signature = '-'.join(map(str,signatureList))
        
        return signature

    def createKCombination(self, product, k_combination_number_of_words):
        listToReturn = list()
        for c in itertools.combinations(product, k_combination_number_of_words):
            listToReturn.append(c)

        return listToReturn


    def createKCombinations(self, k_combination_number_of_words):
        k_combinations = list()
        for product in self.products:
            k_combinations.append(self.createKCombination(product.split(), k_combination_number_of_words))
        
        return k_combinations