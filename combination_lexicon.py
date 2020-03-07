from db.conn import DB
import itertools

class combination_lexicon(object):

    combinationLexicon = dict()

    def __init__(self, products):
        self.products = products
        self.db = DB()
        self.createCombinationLexicon()

    
    def createCombinationLexicon(self):
        two_combinations = self.createKCombinations(2)
        three_combinations = self.createKCombinations(3)
        self.countFrequenciesAndCreateSignatures(two_combinations)
        self.countFrequenciesAndCreateSignatures(three_combinations)
        self.countDistance(2)
        self.countDistance(3)

    def countFrequenciesAndCreateSignatures(self, combinations):
        for titleCombinations in combinations:
            if(len(titleCombinations) > 0):

                for combination in titleCombinations:
                    signature = self.computeSignatureOfKCombination(combination)

                    if signature in self.combinationLexicon:
                        self.combinationLexicon[signature]['count'] = self.combinationLexicon[signature]['count'] + 1
                    else:
                        self.combinationLexicon[signature] = dict()
                        self.combinationLexicon[signature]['combination'] = str(combination)
                        self.combinationLexicon[signature]['count'] = 1
                        self.combinationLexicon[signature]['distance'] = 0

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

    def countDistance(self, k_combination_number_of_words):
        
        for product in self.products:
            productSplit = product.split()
            k_combinations = self.createKCombination(productSplit, k_combination_number_of_words)
            
            for combination in k_combinations:
                signature = self.computeSignatureOfKCombination(combination)
                s = 0
                for word in combination:
                    add = self.euclidean(combination.index(word), productSplit.index(word))
                    s = s + add
                
                self.combinationLexicon[signature]['distance'] = self.combinationLexicon[signature]['distance'] + s

    def euclidean(self, num1, num2):
        return (num1 - num2)**2
                    
