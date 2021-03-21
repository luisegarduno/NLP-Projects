def parseList(wordList):
    print("hi")

class BigramModel:
# -----------------------------------------------------------------------------------------------------

    def __init__(self, name="default", dirName='.', ext='*', smooth=0, stopWordList=[], otherWordList=[]):

        # name: name of the model. The name is used as the filename to store the model
        self.name = name

        # - Directory that stores the corpus.
        # - If 'dirName' starts w/ “/”, then dirName is an absolute path.
        # - Otherwise the path is relative starting from the curr dir. (Default=current dir)
        self.dirName = dirName

        # - The extension of all files that is consider part of the corpus.
        # - Only files that have the specified extension will be read & processed.
        # - Default = “*’, which mean all files in the directory will be considered
        self.ext = ext

        # - The smoothing method that is used.
        # - Default Is no smoothing.
        # - If smooth is a floating point number between 0 & 1 (strictly > 0, <= 1), then we apply add-k smoothing to the bigram probability.
        self.smooth = smooth

        # - List of words that will be removed from the corpus before calculating the bigram probability.
        # - Default is empty
        self.stopWordList = stopWordList

        # - List of words that will be grouped & treated as a single word for calculating bigrams probabilities. 
        self.otherWordList = otherWordList


# -----------------------------------------------------------------------------------------------------

    def Calculate(self):
        # - Actually calculate the bigram probabilities of the corpus & store it within the object
        print("Calculate(self)")


# -----------------------------------------------------------------------------------------------------

    def Save(self):
        # - Save the calculated probabilities in a file.
        # - The filename will be the name of the bigram model.
        # - If the probabilities have not been calculated, then calculate it
        print("Save(self)")

# -----------------------------------------------------------------------------------------------------

    def Load(self):
        # - Load the calculated probabilities from the file to the object.
        # - If the file does not exist, return an error message & quit.
        print("Load(self)")

# -----------------------------------------------------------------------------------------------------

    def getProb(self, w1, w2):
        # - Return the probability of the bigram (w1, w2).
        # - If either of the word is in the corpus, it'll return -1.
        print("--> getProb(self, w1, w2)")

# -----------------------------------------------------------------------------------------------------

    def getProbList(self, w1, sortMethod=0):
        # - Return all the bigrams w/ w1 as the 1st word.
        # - It should return a list, each item of the list is a tuple (word, prob).
        # -- if sortMethod=1, the tuples are sorted alphabetically,
        # -- if sortMethod=2, the tuples are returned in decreasing order of probability (ties are broken arbitrarily).
        # - Otherwise the list need not be sorted in any order. If w1 does not exist it will return an empty list. 
        print("--> getProbList(self, w1, sortMethod=0)")

# -----------------------------------------------------------------------------------------------------

    def getAll(self, sortMethod=0):
        # - Return all the bigrams and their probabilities as a list.
        # - Each item in the list is a tuple (word1,word2, prob).
        # - sortMethod is as above, except when:
        # -- when sortMethod=1 : the tuples are sorted alphabetically by the 1st word of the tuple
        # -- when sortMethod=3 : the tuples are sorted by the 2nd word of the tuple. 
        print("--> getAll(self, sortMethod=0)")

