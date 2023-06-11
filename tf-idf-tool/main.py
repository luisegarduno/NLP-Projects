import sys
# import time
import os.path
# import subprocess
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer


# Current working directory
cwd = os.path.dirname(os.path.realpath(__file__))

title = '''
          88888888888 .d888    8888888     888  .d888      888                     888
              888    d88P"       888       888 d88P"       888                     888
              888    888         888       888 888         888                     888
              888    888888      888   .d88888 888888      888888 .d88b.   .d88b.  888
              888    888         888  d88" 888 888         888   d88""88b d88""88b 888
              888    888  888888 888  888  888 888         888   888  888 888  888 888
              888    888         888  Y88b 888 888         Y88b. Y88..88P Y88..88P 888
              888    888       8888888 "Y88888 888          "Y888 "Y88P"   "Y88P"  888

                             ~ Website : https://gardunos.tech
'''

# Clear screen + show title
def clr():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(title + "\n")
    print("\t\t-----------------------------------------------------------------\n\n")

# Print current strings/sentences
def showDict(docs):
    clr()
    print("\n====================================================\n")
    print("Entered strings/sentences:")
    doc_num = 1
    for i in docs:
        print("- [d{}] ".format(doc_num) + i)
        doc_num += 1
    print("\n====================================================\n\n")

clr()

docs = []
sent = input("Please enter a sentence/string: ")
docs.append(sent)

init_res = "y"
while init_res.lower() != "n" and init_res.lower() == "y":
    init_res = input("\t--> Add another sentence? (y/n): ")

    if init_res.lower() == "y":
        showDict(docs)
        sent = input("Please enter a sentence/string: ")
        docs.append(sent)

    if init_res.lower() != "y" and init_res.lower() != "n":
        print("Invalid input, please try again")
        clr()

showDict(docs)

# ================================
# Todo - See https://github.com/luisegarduno/MachineLearning_SummerPlan/blob/master/DocumentAnalysis.ipynb

count_vec = CountVectorizer()

bag_words = count_vec.fit_transform(docs)
vocab = count_vec.get_feature_names_out()
transposed_array = np.transpose(bag_words.toarray())

def printVocab():
    print("Vocabulary:\n", vocab) 
    print("==============================================\n")

'''
    name: tf_RawFrequency
    details: Calculates TF using Raw Frequency variation
                (tf_ij) Raw Frequency = f_ij
'''
def tf_RawFrequency():
    print("[TF] Raw Frequency (f_ij)")
    for i in range(len(vocab)):
        print(vocab[i], "\t", transposed_array[i])
    nextMove()

'''
    name: tf_LogNormalization
    parameters: transposed_array (passed in as type float)
    details: Calculates TF using Log Normalization variation
                (tf_ij) Log Normalization = 1 + log2(f_ij)
'''
def tf_LogNormalization(transposed_array):
    print("[TF] Log Normalization (1 + log2(f_ij))")
    for i in range(len(vocab)):

        for j in range(len(transposed_array[i])):
            if transposed_array[i][j] != 0:
                transposed_array[i][j] = 1 + np.log2(transposed_array[i][j])

        print(vocab[i], "\t", transposed_array[i])

    nextMove()

''' 
    name: idf_InverseFrequency
    details: calculates the IDF using Inverse Frequency variation.
                (idf_i) Inverse Frequency = log2(N/n_i)
'''
def idf_InverseFrequency():
    print("\nInverse Frequency (IDF)")
    # total number (N) of words
    N = len(docs)
    # total number (n) of times word (i) appears
    n_i = transposed_array.sum(axis=1)

    idf_i = np.log2(N / n_i)
    for idf in range(len(vocab)):
        print(vocab[idf], "\t", idf_i[idf])

    nextMove()

'''
    name: tf_idf_vector
    details: Calculates the TF-IDF vector statistic.
'''
def tf_idf_vector():
    tfidf_vect = TfidfVectorizer()
    tfidf_mat = tfidf_vect.fit_transform(docs)
    df = pd.DataFrame(data=tfidf_mat.toarray(), columns=tfidf_vect.get_feature_names_out())
    print(df)

    nextMove()

# Once statistic has been outputed, ask user what for next option 
def nextMove():
    print("==============================================\n")
    option = input("\nReturn to MainMenu ('y') or Exit ('q')? ")
    if option == 'y':
        clr()
        showDict(docs)
        printMenu()
    if option == 'q':
        sys.exit()
    else:
        print("Invalid option")

# Output MainMenu
def printMenu():
    option = ''
    print("Available Statistics:")
    print("1. [TF] Raw Frequency")
    print("2. [TF] Log Normalization")
    print("3. [IDF] Inverse Frequency")
    print("4. TF-IDF")
    print("q - quit")
    option = input("\nChoose a statistic to view (1-4):")

    clr()
    showDict(docs)

    if option == '1':
        tf_RawFrequency()
    if option == '2':
        tf_LogNormalization(transposed_array.astype(float))
    if option == '3':
        idf_InverseFrequency()
    if option == '4':
        tf_idf_vector()
    if option == 'q' or option == 'n':
        sys.exit()
    else:
        clr()
        showDict(docs)
        print("Invalid option\n\n")

printMenu()

# print(bag_words.toarray())
# print("Shape: ", bag_words.shape)
# print(bag_words[0])
# print("Size of vocabulary: ", len(count_vec.vocabulary_))
# print(count_vec.vocabulary_)
