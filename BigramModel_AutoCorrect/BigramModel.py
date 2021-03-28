import os
import copy

class BigramModel:

    corpus = [{"word": '', "frequency": 0}]
    corpus.pop()
    corpus_files = []
    full_dirName = ''

    word_list = []
    wordFreq = [{"word": '', "frequency": 0}]
    wordFreq.pop()
    word_list_StartEnd = []

# -----------------------------------------------------------------------------------------------------

    def __init__(self, name="default", dirName='.', ext='*', smooth=0, stopWordList=[], otherWordList=[]):

        # - Name of the model. The name is used as the filename to store the model.
        self.name = name

        # - Directory that stores the corpus. Default is current directory
        #    if 'dirName'[0] == '/': 'dirName' = an absolute path.
        #    else: path is relative starting from the currrent directory.
        self.dirName = dirName
        if self.dirName[0] == '/': self.full_dirName = self.dirName
        if self.dirName[0] == '.': self.full_dirName = os.path.dirname(os.path.realpath(__file__))
        if self.dirName[0] != '.' and self.dirName[0] != '/': self.full_dirName = os.path.dirname(os.path.realpath(__file__)) + "/" + self.dirName

        # - The extension of all files that is consider part of the corpus.
        # - Default = '*' (all files in directory are considered)
        self.ext = ext
        if self.ext[0] == '*': self.corpus_files = [x for x in os.listdir(self.dirName)]
        else: self.corpus_files = [x for x in os.listdir(self.dirName) if x.endswith(self.ext)]

        # - The smoothing method that is used. Default = No smoothing.
        # - If smooth is a floating point number between 0 & 1 (strictly > 0, <= 1), then we apply add-k smoothing to the bigram probability.
        self.smooth = smooth

        # - List of words that'll be removed from the corpus before calculating the bigram probability. Default = empty
        self.stopWordList = [self.parser(x.lower()) for x in stopWordList]

        # - List of words that will be grouped & treated as a single word for calculating bigrams probabilities. 
        self.otherWordList = [self.parser(y.lower()) for y in otherWordList]

# -----------------------------------------------------------------------------------------------------

    def print(self):
        print('\n*--------------------------------*')
        print(" - Name:", self.name, "\n - Directory:", self.dirName, "\n - Extension:", self.ext, "\n - SmoothMethod:", self.smooth)
        print('\n - Valid Files: ', self.corpus_files)
        print('\n - StopWords:', self.stopWordList)
        print('*--------------------------------*')


# -----------------------------------------------------------------------------------------------------

    def Calculate(self):
        bigramFrequencyList = {}
        allSentences = []

        # - Actually calculate the bigram probabilities of the corpus & store it within the object
        for fileName in self.corpus_files:
            # Get full directory location
            full_location = self.full_dirName + "/" + fileName
            try:
                with open(full_location) as file:
                    print("\nCalculate --> File Found: " + str(fileName) + "!\n")

                    # paragraph = file.readlines()
                    for sentence in file.readlines():
                        word_sentence = ""
                        for word in sentence.split():
                            word_sentence += word + " "
                            #if self.parser(word.lower()) not in self.word_list:
                                # self.word_list.append(self.parser(word.lower()))
                            if word[len(word) - 1] in ['.', '?', '!']:
                                print("Sentence: ", word_sentence)
                                sentences = self.getSentences(word_sentence)
                                wordFreqs = self.getWordFreq(word_sentence)
                                #print(wordFreqs, '\n')
                                word_sentence = ""

                    # Read every single line of file
                    # for i in file.readlines():
                    #     sentences = self.getSentences(i.readline())
                    #     wordFreqs = self.getWordFreq(i)
                    #     print("Words:" , wordFreqs)
                        # print(self.makeBigramFreqList(i))
                        # Get list of sentences within document 
                        #sentence = self.getSentences(i)
                        #allSentences.append(aSentence)

                        #if len(sentence) == 0: return []

                        # for word in sentence.split():
                        #print("Sentence: " + sentence)  # Print Sentence

                    #print("Sentence: " + sentence)  # Print Sentence

                    # print("\n----------------------------------------")
                    # print(self.makeBigramFreqList(sentence))
                    # print("\n----------------------------------------")

                    # sentences = []
                    # current_sentence = ""
                    #sentences = self.getSentences(sentence)
                    # for i in sentences: print("---> ", i)

                    # if len(sentences) == 0: return []

                    # For each word within each sentence
                    # for word in sentence.split():
                        # Check if word exists in list of words
                        # if self.parser(word.lower()) not in self.word_list:
                            # add to wordlist
                            # self.word_list.append(self.parser(word.lower()))

                            # Check if string is the last word in sentence
                            # if word[len(word) - 1] == '.': print(word + " is an Ending word")
                            # Check if string has an upp
                            # if word.isupper() == True: print(word + " is a Starter word")

                        # print(word, " --> ", self.parser(word.lower()))
                file.close()
                self.corpus.sort(key=self.alphabetically)
                print("-----------------------------------------------------")

            except FileNotFoundError:
                print("Calculate --> File not found! (" + str(full_location) + ")")

        self.corpus.sort(key=self.alphabetically)
        for i in self.corpus: print(i)

# -----------------------------------------------------------------------------------------------------

    def Save(self):
        # - Save the calculated probabilities in a file.
        # - The filename will be the name of the bigram model.
        # - If the probabilities have not been calculated, then calculate it
        print("Save --> Saving as", self.name)

# -----------------------------------------------------------------------------------------------------

    def Load(self):
        # - Load the calculated probabilities from the file to the object.
        # - If the file does not exist, return an error message & quit.
        try:
            # if os.path.isfile(self.name):
            with open(self.name) as file:
                print("")
            file.close()
            print("Load --> '" + str(self.name) + "' Model found!")

        except FileNotFoundError:
            print("Load --> Model not found or incorrect file path!")

# -----------------------------------------------------------------------------------------------------

    def getProb(self, w1, w2):
        # - Return the probability of the bigram (w1, w2).
        # - If either of the word is NOT in the corpus, it'll return -1.
        if w1 not in self.corpus:
            print("Word '", w1, "' not found!")
            return -1
        if w2 not in self.corpus:
            print("Word '", w2, "' not found!")
            return -1

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

# -----------------------------------------------------------------------------------------------------

    def getBigramFreq(self, paragraph):
        bigramFreq = {}
        sentences = self.getSentences(paragraph)
        wordFreqs = self.getWordFreq(paragraph)
        for w1 in wordFreqs:
            for w2 in wordFreqs:
                bigramFreq[(w1 + " " + w2)] = 0

        for sentence in sentences:
            tokenPair = []
            sentenceTokens = sentence.split()
            for token in sentenceTokens:
                token = self.parser(token.lower())
                if token not in self.stopWordList and len(token.strip()) > 0:
                    tokenPair.append(token)
                    if len(tokenPair) == 2:
                        pairKey = tokenPair[0] + ' ' + tokenPair[1]
                        if pairKey in bigramFreq: bigramFreq[pairKey] += 1
                        else: bigramFreq[pairKey] = 1
                    tokenPair = []
                    tokenPair.append(token)

        bigramStats = self.getStats(bigramFreq)
        bigram_1 = copy.deepcopy(bigramStats)
        for i in range(0,len(bigramStats)-1):
            if bigramStats[i] != 0: bigram_1[i] = float((i + 1) * bigramStats[i+1]) / bigramStats[i]
            else: bigram_1[i] = 0

        for bigram in bigramFreq.keys():
            bigram_0 = bigramFreq[bigram]
            bigramFreq[bigram] = bigram_1[bigram_0]
        return bigramFrequency

# -----------------------------------------------------------------------------------------------------

    def getSentences(self,sentence):
        sentences = []
        current_sentence = ""

        for word in sentence.split():
            if word != "\n":
                endChar = word[len(word) - 1:]
                if endChar in ['.', '?', '!']:
                    current_sentence += word + '\n'
                    sentences.append(current_sentence)
                    current_sentence = ""
                else: current_sentence += word + " "
        return sentences

# -----------------------------------------------------------------------------------------------------

    def getWordFreq(self, paragraph):
        sentences = []
        current_sentence = ""
        for w in paragraph.split():
            if w != '\n':
                endChar = w[len(w) - 1:]
                if endChar in [".", "?", "!"]:
                    current_sentence += w + "\n"
                    sentences.append(current_sentence)
                    current_sentence = ""
                else: current_sentence += w + " "

        if len(sentences) == 0: return []

        tokenFreq = {}
        for sentence in sentences:
            sentenceTokens = sentence.split()
            for token in sentenceTokens:
                token = self.parser(token.lower())
                if token not in self.stopWordList and len(token.strip()) > 0:
                    if token in tokenFreq: tokenFreq[token] += 1
                    else: tokenFreq[token] = 1

                    idx = 0
                    found = False
                    while idx != len(self.corpus):
                        if self.corpus[idx]["word"] == token:
                            self.corpus[idx]["frequency"] += 1
                            found = True
                        idx += 1

                    if found == False: self.corpus.append({"word": token, "frequency": 1})
        return tokenFreq

# -----------------------------------------------------------------------------------------------------

    def getStats(self, bigramFreq):
        stats = []

        maxFreq = 0
        for bigram in bigramFreq.keys():
            count = bigramFreq[bigram]
            if count > maxFreq: maxFreq = count

        for i in range(0,maxFreq+1):
            freq = 0
            for bigram in bigramFreq.keys():
                count = bigramFreq[bigram]
                if count == i: freq += 1
                stats.append(freq)
        return stats

# -----------------------------------------------------------------------------------------------------

    def parser(self, w):
        punctuation = ["!","(",")","-","[","]",":",";",'"',"'",".",",","?"]
        new_w = w

        for i in punctuation:
            while new_w.find(i) >= 0:
                idx = new_w.find(i)
                new_w = new_w[:idx] + new_w[idx+1:]
        return new_w

# -----------------------------------------------------------------------------------------------------
    def alphabetically(self,w):
        return w["word"]
