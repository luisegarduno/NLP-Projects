import os

class BigramModel:

    corpus_files = []

# -----------------------------------------------------------------------------------------------------

    def __init__(self, name="default", dirName='.', ext='*', smooth=0, stopWordList=[], otherWordList=[]):

        # - Name of the model. The name is used as the filename to store the model.
        self.name = name

        # - Directory that stores the corpus. Default is current directory
        #    if 'dirName'[0] == '/': 'dirName' = an absolute path.
        #    else: path is relative starting from the currrent directory.
        self.dirName = dirName

        # - The extension of all files that is consider part of the corpus.
        # - Default = '*' (all files in directory are considered)
        self.ext = ext
        if self.ext[0] == '*': self.corpus_files = [x for x in os.listdir(self.dirName)]
        else: self.corpus_files = [x for x in os.listdir(self.dirName) if x.endswith(self.ext)]

        # - The smoothing method that is used. Default = No smoothing.
        # - If smooth is a floating point number between 0 & 1 (strictly > 0, <= 1), then we apply add-k smoothing to the bigram probability.
        self.smooth = smooth

        # - List of words that'll be removed from the corpus before calculating the bigram probability. Default = empty
        self.stopWordList = [x.lower() for x in stopWordList]

        # - List of words that will be grouped & treated as a single word for calculating bigrams probabilities. 
        self.otherWordList = [y.lower() for y in otherWordList]


# -----------------------------------------------------------------------------------------------------

    def print(self):
        print('\n*--------------------------------*')
        print(" - Name:", self.name, "\n - Directory:", self.dirName, "\n - Extension:", self.ext, "\n - SmoothMethod:", self.smooth)
        print('\n - Valid Files: ', self.corpus_files)
        print('\n - StopWords:', self.stopWordList)
        print('*--------------------------------*')

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
        # - If either of the word is NOT in the corpus, it'll return -1.
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

