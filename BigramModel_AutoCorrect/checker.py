from BigramModel import *

# name          : Filename that will be used to store Bigram Model
# dirName       : Store corpus at this directory
# ext           : Extension of all files that is considered part of the corpus
# smooth        : the smoothing method that is used 
# stopWordList  : List of stop words to remove from corpus 
# otherWordList : List of words that'll be grouped as 1 word to calc bigram possibilites

# ----------------------------------------------------------------------------------------------

params = False

# DISABLE Parameters - True
name = "default"
dirName = '.'
ext = '*'
smooth = 0
stopWords = []
otherWordList = []

# ENABLE Parameters - False
if not params:
    name = "Bigram"
    dirName = 'test'
    ext = '.txt'
    smooth = 0
    stopWords = []
    stopWordsFile = open('StopWords.txt', 'r')
    for line in stopWordsFile: stopWords.append(str(line.strip()))
    otherWordList = []

# ----------------------------------------------------------------------------------------------

b = BigramModel(name=name, dirName=dirName, ext=ext, smooth=smooth, stopWordList=stopWords, otherWordList=[])
b.Calculate()
b.Save()
b.Load()
b.getProb("word1", "word2")
b.getProbList("word1", sortMethod=0)
b.getAll(sortMethod=0)
# b.print()
