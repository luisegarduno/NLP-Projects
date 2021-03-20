from BigramModel import *

# name = ""
# dirName = '.'
# ext = '*'
# smooth = 0
# stopWordList = []
# otherWordList = []

# Version 1
# stopWords_File = open('StopWords.txt', 'r')
# stopWords = stopWords_File.read().lower().split()
# stopWords_File.close()

# Version 2
# from numpy import loadtxt
# lines = loadtxt("StopWords.txt", dtype=str, comments="#", delimiter="\n", unpack=False)

# Version 3
stopWords = []
stopWordsFile = open('StopWords.txt', 'r')
for line in stopWordsFile: stopWords.append(str(line.strip()).lower())

b = BigramModel(name="", dirName='.', ext='*', smooth=0, stopWordList=stopWords, otherWordList=[])
b.Calculate()
b.Save()
b.Load()
b.getProb("word1", "word2")
b.getProbList("word1", sortMethod=0)
b.getAll(sortMethod=0)
