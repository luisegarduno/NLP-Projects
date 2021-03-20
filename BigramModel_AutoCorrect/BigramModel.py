def parseList(wordList):
    print("hi")

class BigramModel:
    def __init__(self, name="default", dirName='.', ext='*', smooth=0, stopWordList=[], otherWordList=[]):
        self.name = name
        self.dirName = dirName
        self.ext = ext
        self.smooth = smooth
        self.stopWordList = stopWordList
        self.otherWordList = otherWordList

    def Calculate(self):
        # Actually calculate the bigram probabilities of the corpus and store it within the object
        print("Calculate(self)")

    def Save(self):
        # Save the calculated probabilities in a file. The filename will be the name of the bigram model. If the probabilities have not been calculated, then calculate it
        print("Save(self)")

    def Load(self):
        # Load the calculated probabilities from the file to the object. If the file does not exist, return an error message and quit.
        print("Load(self)")

    def getProb(self, w1, w2):
        # Return the probability of the bigram (w1, w2). If either of the word is in the corpus, it will return -1.
        print("--> getProb(self, w1, w2)")

    def getProbList(self, w1, sortMethod=0):
        # Return all the bigrams with w1 as the first word. It should return a list, each item of the list is a tuple (word, prob). If sortMethod = 1, the tuples are sorted alphabetically, if sortMethod = 2, the tuples are returned in decreasing order of probability (ties are broken arbitrarily). Otherwise the list need not be sorted in any order. If w1 does not exist it will return an empty list. 
        print("--> getProbList(self, w1, sortMethod=0)")

    def getAll(self, sortMethod=0):
        # Return all the bigrams and their probabilities as a list. Each item in the list is a tuple (word1,word2, prob). sortMethod is as above, except when sortMethod = 1, the tuples are sorted alphabetically by the first word of the tuple, and when sortMethod = 3, the tuples are sorted by the second word of the tuple. 
        print("--> getAll(self, sortMethod=0)")


