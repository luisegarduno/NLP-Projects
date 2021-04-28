from nltk.corpus import wordnet as wn


# -------------------------------------------------------------------------
def word_path_similarity(w1, w2, pos1=None, pos2=None, option=None):
    print("word_path_similarity ============================================")

    a = wn.synsets(w1)
    b = wn.synsets(w2)

    # Option : First (None)
    if option == None or option == 'first':
        c = wn.path_similarity(a[0],b[0])
        print("\tPath similarity =", c)

    # Option : Average
    if option == "avg":
        c, i = 0.0, 0.0
        for a_i in range(len(a)):
            for b_i in range(len(b)):
                p = wn.path_similarity(a[a_i],b[b_i])
                if p != None: c += p
                i += 1.0
        print("\tPath similarity =", c/i)

    # Option : Minimum
    if option == "min":
        print("hi")

    print()




# -------------------------------------------------------------------------
def word_lcs_similarity(w1, w2, pos1=None, pos2=None, option=None):
    print("word_lcs_similarity ============================================")

    a = wn.synsets(w1)
    b = wn.synsets(w2)

    # Option : First (None)
    if option == None or option == 'first':
        c = wn.lch_similarity(a[0],b[0])
        print("\tLch similarity =", c)

    # @todo Fix 'Average' for lcs_similarity

    # Option : Average
    if option == "avg":
        c, i = 0.0, 0.0
        print("A[", len(a), "] B[", len(b), "]")
        for a_i in range(len(a)):
            for b_i in range(len(b)):
                print(a[a_i]," | ", b[b_i] ," | ")
                p = wn.lch_similarity(a[a_i],b[b_i])
                if p != None: c += p
                i += 1.0
        print("\tLch similarity =", c/i)

    # Option : Minimum
    if option == "min":
        print("hi")

    print()




# -------------------------------------------------------------------------
def word_wup_similarity(w1, w2, pos1=None, pos2=None, option=None):
    print("word_wup_similarity ============================================")

    a = wn.synsets(w1)
    b = wn.synsets(w2)

    # Option : First (None)
    if option == None or option == 'first':
        c = wn.wup_similarity(a[0],b[0])
        print("\tWup similarity =", c)

    # Option : Average
    if option == "avg":
        c, i = 0.0, 0.0
        for a_i in range(len(a)):
            for b_i in range(len(b)):
                p = wn.wup_similarity(a[a_i],b[b_i])
                if p != None: c += p
                i += 1.0
        print("\tWup similarity =", c/i)

    # Option : Minimum
    if option == "min":
        print("hi")



    print()



# -------------------------------------------------------------------------
def word_res_similarity(ic, w1, w2, pos1=None, pos2=None, option=None):
    print("word_res_similarity ============================================")
    print("hi")
    print()




#################################################################################
############################## TESTING ##########################################
#################################################################################
w1 = "dog"
w2 = "cat"


one = word_path_similarity(w1, w2, option="avg")
# print(one)

two = word_lcs_similarity(w1, w2, option="avg")
# print(two)

three = word_wup_similarity(w1, w2, option="avg")
# print(three)

# four = word_res_similarity(ic, w1, w2)
# print(four)


