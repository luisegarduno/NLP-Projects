The goal of this project is to implement a bigram model for a set of documents, and thenuse it (and other tools) to perform automatic text correction.

All text being used need to be converted to lower case before processing.

## Part 1: Bigram Model     
You are to implement a class call BigramModel. The class will take in the name of a directory, and the name of a file extension. It will then search the specific directory and use all the files that meet the file extension option to build the bigram model.     

The class specification is as follows:     
_Constructor_     
BigramModel(name = “default”, dirName= ‘.’, ext = ‘*’, smooth =0, stopWordList= [], otherWordList = [])     

Create a bigram model for a given corpus. It take the following parameters:     
- name: name of the model. The name is used as the filename to store the model     
- dirName: the directory that store the corpus. If dname starts with a “/”, then dname is an absolute path. Otherwise the path is relative starting from the current directory. (Default is the current directory)     
- ext: the extension of all files that is consider part of the corpus. Only files that have the specified extension will be read and processed. Default is “*’, which mean all files in the directory will be considered     
- smooth: the smoothing method that is used. Default Is no smoothing. If smooth is a floating point number between 0 and 1 (strictly greater than 0, less than or equal to 1), then we apply add-k smoothing to the bigram probability.     
- stopWordList: a list of words that will be removed from the corpus before calculating the bigram probability. Default is empty     
- otherWordList: a list of words that will be grouped and treated as a single word for calculating bigrams probabilities.     

Notice that you should also remove all words that does not start with a letter of the alphabet. Also you should account for beginning and end of sentences. For all methods below, we use the ^ and $ symbol to denote beginning and end of sentence respectively. Also,if your otherWordListis non-empty, the user can use the symbol * to denote other words.     

_Methods_     
- Calculate()     
  Actually calculate the bigram probabilities of the corpus and store it within the object     
- Save()     
  Save the calculated probabilities in a file. The filename will be the name of the bigram model. If the probabilities have not been calculated, then calculate it
- Load()     
  Load the calculated probabilities from the file to the object. If the file does not exist, return an error message and quit.     
- getProb(w1, w2)     
  Return the probability of the bigram (w1, w2). If either of the word is in the corpus, it will return -1.     
- getProbList(w1, sortMethod = 0)     
  Return all the bigrams with w1 as the first word. It should return a list, each item of the list is a tuple (word, prob). If sortMethod = 1, the tuples are sorted alphabetically, if sortMethod = 2, the tuples are returned in decreasing order of probability(ties are broken arbitrarily). Otherwise the list need not be sorted in any order.If w1 does not exist it will return an empty list.     
- getAll(sortMethod = 0)     
  Return all the bigrams and their probabilities as a list. Each item in the list is a tuple (word1, word2, prob). sortMethod is as above, except when sortMethod = 1, the tuples are sorted alphabetically by the first word of the tuple, and when sortMethod = 3, the tuples are sorted by the second word of the tuple.     
  
(all the get methods should print an message and exit if the probability has not been calculated)     

## Part 2 : Automatic correction     
You are to build a class call AutoCorrectText that given a text, correct it automatically. Your class should provide the following two methods.     
_Constructor_     
AutoCorrectText()     
- Create an autoCorrectText object. MethodCorrect(text)     
- The text is astring that is to be checked and corrected. The output shouldbe a list of tuples (pos, w1, w2):     
  - pos: is the location of the word to be corrected. Starting position is 0, and each punctuation count as a word –but there is no need to correct punctuations
  - w1: is the original word     
  - w2: is the corrected word     


Your CorrectText class should adhere to the following rules:     
_Dictionary_: You should use the NLTK words corpus to be the list of correct words. You can access that via the following code:     
  from nltk.corpus import words     
  l = words.words()     
(words.words()will return the list of words). Notice some ofthose words in the list starts with an uppercase letter,you will need to convert that to lower case.



_Your programs:_     
You can use your previous programs (myDict.py and BigramModel.py). You are free to set up parameters for each of those code (e.g. corpus, subCostList).     

_Tools from NLTK:_
You are allowed to use a variety of resources for this task, including:     
- Any corpus     
- Any tokenizer(including tools to break articles into sentences)     
- Any lemmatizer / stemmer     
- Any part of speech tagger     
If you want to use any other things available in NLTK, e-mail first (notice that I may NOT approve that).     

_Numpy_     
You are allowed to use numpy, but not any othernon-standardmodules (except those from nltk that is mentioned above)     
