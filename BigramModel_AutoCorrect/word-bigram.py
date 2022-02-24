import os.path
import nltk

# Current working directory
cwd = os.path.dirname(os.path.realpath(__file__))

def bgs(w):
    spaced = ''
    for ch in w:
        spaced = spaced + ch + ' '

    tokenized = spaced.split(" ")
    myList = list(nltk.bigrams(tokenized))

    Bigrams = []
    for i in myList:
        Bigrams.append((''.join([wd+'' for wd in i])).strip())

    if 'th' in Bigrams and 'at' in Bigrams:
        print("Word: " + w + "\t\tBigrams: ", Bigrams)
        return True
    return False

# Check to see if program has been ran before
if os.path.isfile('test/top-1k-words.txt'):
    dex = []
    os.system('cls' if os.name == 'nt' else 'clear')

    with open('test/top-1k-words.txt', 'r+') as file:
        word = "hi"
        while str.lower(word) != "yourself":
            word = file.readline()
            word = word.replace('\n', '')
            dex.append(word)
    file.close()

winners = []
for i in range(0,len(dex)):
    if bgs(dex[i]):
        winners.append(dex[i]);

print("# of words containing bigram 'TH' & 'AT': ", len(winners))
