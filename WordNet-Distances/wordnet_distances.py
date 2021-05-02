from nltk.corpus import wordnet as wn
from nltk.corpus import genesis
from nltk.corpus import wordnet_ic

# -------------------------------------------------------------------------
def builder(w1, w2, pos1 = None, pos2 = None):
    a,b = [],[]

    if pos1 == None and pos2 == None: a,b = wn.synsets(w1), wn.synsets(w2)
    if pos1 == None and pos2 != None: a,b = wn.synsets(w1), wn.synsets(w2, pos=pos2)
    if pos1 != None and pos2 == None: a,b = wn.synsets(w1, pos=pos1), wn.synsets(w2)
    if pos1 != None and pos2 != None: a,b = wn.synsets(w1, pos=pos1), wn.synsets(w2, pos=pos2)

    return a,b

# -------------------------------------------------------------------------
def word_path_similarity(w1, w2, pos1=None, pos2=None, option=None):
    print("word_path_similarity ============================================")

    a,b = builder(w1,w2,pos1,pos2)

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
        c = []
        for a_i in range(len(a)):
            for b_i in range(len(b)):
                p = wn.path_similarity(a[a_i],b[b_i])
                if p != None: c.append(p)
        print("\tPath similarity =", min(c))

    print()



# -------------------------------------------------------------------------
def word_lcs_similarity(w1, w2, pos1=None, pos2=None, option=None):
    print("word_lcs_similarity ============================================")

    a,b = builder(w1,w2,pos1,pos2)

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
        c = []
        for a_i in range(len(a)):
            for b_i in range(len(b)):
                p = wn.path_similarity(a[a_i],b[b_i])
                if p != None: c.append(p)
                i += 1.0
        print("\tPath similarity =", min(c))

    print()



# -------------------------------------------------------------------------
def word_wup_similarity(w1, w2, pos1=None, pos2=None, option=None):
    print("word_wup_similarity ============================================")

    a,b = builder(w1,w2,pos1,pos2)

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
        c = []
        for a_i in range(len(a)):
            for b_i in range(len(b)):
                p = wn.path_similarity(a[a_i],b[b_i])
                if p != None: c.append(p)
        print("\tPath similarity =", min(c))

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

testing = "wup"

# Path Similarity : DONE ########################################################

""" Word Path Similarity : first """
if testing == "first_ps" or testing == "ps" or testing == "all":
    word_path_similarity(w1, w2, option="first")
    word_path_similarity(w1, w2, pos1='n', option="first")
    word_path_similarity(w1, w2, pos2='n', option="first")
    word_path_similarity(w1, w2, pos1='n', pos2='n', option="first")

""" Word Path Similarity : avg """
if testing == "avg_ps" or testing == "ps" or testing == "all":
    word_path_similarity(w1, w2, option="avg")
    word_path_similarity(w1, w2, pos1='n', option="avg")
    word_path_similarity(w1, w2, pos2='n', option="avg")
    word_path_similarity(w1, w2, pos1='n', pos2='n', option="avg")

""" Word Path Similarity : min """
if testing == "min_ps" or testing == "ps" or testing == "all":
    word_path_similarity(w1, w2, option="min")
    word_path_similarity(w1, w2, pos1='n', option="min")
    word_path_similarity(w1, w2, pos2='n', option="min")
    word_path_similarity(w1, w2, pos1='n', pos2='n', option="min")

# LCS Similarity : !Done ########################################################

""" Word Lcs Similarity : first """
if testing == "first_lcs" or testing == "lcs" or testing == "all":
    word_lcs_similarity(w1, w2, option="first")
    word_lcs_similarity(w1, w2, pos1='n', option="first")
    word_lcs_similarity(w1, w2, pos2='n', option="first")
    word_lcs_similarity(w1, w2, pos1='n', pos2='n', option="first")

""" Word Lcs Similarity : avg """
if testing == "avg_lcs" or testing == "lcs" or testing == "all":
    word_lcs_similarity(w1, w2, option="avg")
    word_lcs_similarity(w1, w2, pos1='n', option="avg")
    word_lcs_similarity(w1, w2, pos2='n', option="avg")
    word_lcs_similarity(w1, w2, pos1='n', pos2='n', option="avg")

""" Word Lcs Similarity : min """
if testing == "min_lcs" or testing == "lcs" or testing == "all":
    word_lcs_similarity(w1, w2, option="min")
    word_lcs_similarity(w1, w2, pos1='n', option="min")
    word_lcs_similarity(w1, w2, pos2='n', option="min")
    word_lcs_similarity(w1, w2, pos1='n', pos2='n', option="min")

# Wup Similarity : Done #########################################################

""" Word Wup Similarity : first """
if testing == "first_wup" or testing == "wup" or testing == "all":
    word_wup_similarity(w1, w2, option="first")
    word_wup_similarity(w1, w2, pos1='n', option="first")
    word_wup_similarity(w1, w2, pos2='n', option="first")
    word_wup_similarity(w1, w2, pos1='n', pos2='n', option="first")

""" Word Wup Similarity : avg """
if testing == "avg_wup" or testing == "wup" or testing == "all":
    word_wup_similarity(w1, w2, option="avg")
    word_wup_similarity(w1, w2, pos1='n', option="avg")
    word_wup_similarity(w1, w2, pos2='n', option="avg")
    word_wup_similarity(w1, w2, pos1='n', pos2='n', option="avg")

""" Word Wup Similarity : min """
if testing == "min_wup" or testing == "wup" or testing == "all":
    word_wup_similarity(w1, w2, option="min")
    word_wup_similarity(w1, w2, pos1='n', option="min")
    word_wup_similarity(w1, w2, pos2='n', option="min")
    word_wup_similarity(w1, w2, pos1='n', pos2='n', option="min")

# Res Similarity : !Done ########################################################

""" Word Res Similarity : first """
if testing == "first_res" or testing == "res" or testing == "all":
    ic = wn.ic(genesis, False, 0.0)
    word_res_similarity(ic, w1, w2, option="first")
    word_res_similarity(ic, w1, w2, pos1='n', option="first")
    word_res_similarity(ic, w1, w2, pos2='n', option="first")
    word_res_similarity(ic, w1, w2, pos1='n', pos2='n', option="first")

""" Word Res Similarity : avg """
if testing == "avg_res" or testing == "res" or testing == "all":
    ic = wn.ic(genesis, False, 0.0)
    word_res_similarity(ic, w1, w2, option="avg")
    word_res_similarity(ic, w1, w2, pos1='n', option="avg")
    word_res_similarity(ic, w1, w2, pos2='n', option="avg")
    word_res_similarity(ic, w1, w2, pos1='n', pos2='n', option="avg")

""" Word Res Similarity : min """
if testing == "min_res" or testing == "res" or testing == "all":
    ic = wn.ic(genesis, False, 0.0)
    word_res_similarity(ic, w1, w2, option="min")
    word_res_similarity(ic, w1, w2, pos1='n', option="min")
    word_res_similarity(ic, w1, w2, pos2='n', option="min")
    word_res_similarity(ic, w1, w2, pos1='n', pos2='n', option="min")


# four = word_res_similarity(ic, w1, w2)
# print(four)


