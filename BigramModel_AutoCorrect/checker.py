from BigramModel import *


# ----------------------------------------------------------------------------------------------

params = False

# DISABLE Parameters
name = ""
dirName = '.'
ext = '*'
smooth = 0
stopWords = []
otherWordList = []

# ENABLE Parameters
if not params:
    # Stop Words
    stopWords = []
    stopWordsFile = open('StopWords.txt', 'r')
    for line in stopWordsFile: stopWords.append(str(line.strip()).lower())

# ----------------------------------------------------------------------------------------------




b = BigramModel(name="", dirName='.', ext='*', smooth=0, stopWordList=stopWords, otherWordList=[])
b.Calculate()
b.Save()
b.Load()
b.getProb("word1", "word2")
b.getProbList("word1", sortMethod=0)
b.getAll(sortMethod=0)
