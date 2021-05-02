from nltk.corpus import genesis
from nltk.corpus import wordnet_ic
from nltk.corpus import wordnet as wn

# -------------------------------------------------------------------------
def check(a, b, verbose=True):

    # Check if length of either arrays is 0
    if len(a) == 0 or len(b) == 0:
        if len(a) == 0 and verbose==True: print("Path similarity: Invalid size for w1, returning...")
        if len(b) == 0 and verbose==True: print("Path similarity: Invalid size for w2, returning...")
        return 0

    else: return 1

# -------------------------------------------------------------------------
def builder(w1, w2, pos1 = None, pos2 = None):
    a,b = [],[]

    # If pos1 or pos2 is 'None' (empty)
    if pos1 == None or pos2 == None:
        if pos1 == None: a = wn.synsets(w1)
        if pos2 == None: b = wn.synsets(w2)

    # If pos1 or pos2 = 'v', 'n', or 'r'
    if pos1 == 'v' or pos1 == 'n' or pos1 == 'r' or pos2 == 'v' or pos2 == 'n' or pos2 == 'r':
        if pos1 == 'v' or pos1 == 'n' or pos1 == 'r': a = wn.synsets(w1, pos=pos1)
        if pos2 == 'v' or pos2 == 'n' or pos2 == 'r': b = wn.synsets(w2, pos=pos2)

    # If pos1 or pos2 wants to use both types of adjectives 
    if pos1 == 'A' or pos2 == 'A':
        if pos1 == 'A': a = wn.synsets(w1, pos='a')
        if pos2 == 'A': b = wn.synsets(w2, pos='a')

    # If pos1 or pos2 = 'a'
    if pos1 == 'a' or pos2 == 'a':
        if pos1 == 'a':
            a_a = wn.synsets(w1, pos='a')
            for i in range(len(a_a)):
                if a_a[i].pos() == 'a': a.append(a_a[i])

        if pos2 == 'a':
            b_a = wn.synsets(w2, pos='a')
            for i in range(len(b_a)):
                if b_a[i].pos() == 'a': b.append(b_a[i])

    # If pos1 or pos2 = 's'
    if pos1 == 's' or pos2 == 's':
        if pos1 == 's':
            a_s = wn.synsets(w1, pos='s')
            for i in range(len(a_s)):
                if a_s[i].pos() == 's': a.append(a_s[i])

        if pos2 == 's':
            b_s = wn.synsets(w2, pos='s')
            for i in range(len(b_s)):
                if b_s[i].pos() == 's': b.append(b_s[i])

    return a,b

# -------------------------------------------------------------------------
def word_path_similarity(w1, w2, pos1=None, pos2=None, option=None):
    a,b = builder(w1,w2,pos1,pos2)
    if check(a,b) == 0: return 0

    else:
        # Option : First (None)
        if option == None or option == 'first': c = a[0].path_similarity(b[0])

        # Option : Average
        if option == "avg":
            c, i = 0.0, 0.0
            for a_i in range(len(a)):
                for b_i in range(len(b)):
                    p = a[a_i].path_similarity(b[b_i])
                    if p != None: c += p
                    i += 1.0
            c /= i

        # Option : Minimum
        if option == "min":
            c = []
            for a_i in range(len(a)):
                for b_i in range(len(b)):
                    p = a[a_i].path_similarity(b[b_i])
                    if p != None: c.append(p)
            c = min(c)

        print(f"Path similarity : {c}")
        return c

# -------------------------------------------------------------------------
def word_lcs_similarity(w1, w2, pos1=None, pos2=None, option=None):
    pos_flag = False
    a,b = builder(w1,w2,pos1,pos2)
    if check(a,b) == 0: return 0

    else:
        # Option : First (None)
        if option == None or option == 'first': c = a[0].lch_similarity(b[0])

        # Option : Average
        if option == "avg":
            c, i = 0.0, 0.0
            for a_i in range(len(a)):
                for b_i in range(len(b)):
                    try:
                        p = a[a_i].lch_similarity(b[b_i])
                        if p != None: c += p
                        i += 1.0
                    except:
                        pos_flag = True
            c /= i

        # Option : Minimum
        if option == "min":
            c = []
            for a_i in range(len(a)):
                for b_i in range(len(b)):
                    try:
                        p = a[a_i].lch_similarity(b[b_i])
                        if p != None: c.append(p)
                    except:
                        pos_flag = True
            c = min(c)

        if pos_flag == True: print("** Lch similarity : Ignoring pairs with mismatched pos values...")
        print(f"Lch similarity : {c}")
        return c

# -------------------------------------------------------------------------
def word_wup_similarity(w1, w2, pos1=None, pos2=None, option=None):
    a,b = builder(w1,w2,pos1,pos2)
    if check(a,b) == 0: return 0

    else:
        # Option : First (None)
        if option == None or option == 'first': c = a[0].wup_similarity(b[0])

        # Option : Average
        if option == "avg":
            c, i = 0.0, 0.0
            for a_i in range(len(a)):
                for b_i in range(len(b)):
                    p = a[a_i].wup_similarity(b[b_i])
                    if p != None: c += p
                    i += 1.0
            c /= i

        # Option : Minimum
        if option == "min":
            c = []
            for a_i in range(len(a)):
                for b_i in range(len(b)):
                    p = a[a_i].wup_similarity(b[b_i])
                    if p != None: c.append(p)
            c = min(c)

        print(f"Wup similarity : {c}")
        return c

# -------------------------------------------------------------------------
def word_res_similarity(ic, w1, w2, pos1=None, pos2=None, option=None):
    pos_flag = False
    a,b = builder(w1,w2,pos1,pos2)
    if check(a,b) == 0: return 0

    else:
        # Option : First (None)
        if option == None or option == 'first':
            c = a[0].res_similarity(b[0], ic)

        # Option : Average
        if option == "avg":
            c, i = 0.0, 0.0
            for a_i in range(len(a)):
                for b_i in range(len(b)):
                    try:
                        p = a[a_i].res_similarity(b[b_i], ic)
                        if p != None: c += p
                        i += 1.0
                    except:
                        pos_flag = True
            c /= i

        # Option : Minimum
        if option == "min":
            c = []
            for a_i in range(len(a)):
                for b_i in range(len(b)):
                    try:
                        p = a[a_i].res_similarity(b[b_i], ic)
                        if p != None: c.append(p)
                    except:
                        pos_flag = True
            c = min(c)

        if pos_flag == True: print("** Resnik similarity : Ignoring pairs with mismatched pos values...")
        print(f"Resnik similarity : {c}")
        return c

# -------------------------------------------------------------------------
def extra_word_path_similarity(w1, w2, pos1 = None, pos2 = None, option = None):

    a_n, b_n  = builder(w1, w2, pos1 = 'n', pos2 = 'n')
    if check(a_n, b_n) == 0: print("NOUN == 0")
    else: prob_ps = word_path_similarity(w1, w2, pos1='n', pos2='n', option=option)


    a_v, b_v = builder(w1, w2, pos1 = 'v', pos2 = 'v')
    if check(a_v, b_v) == 0: print("VERB == 0")

    a_r, b_r = builder(w1, w2, pos1 = 'r', pos2 = 'r')
    if check(a_r, b_r) == 0: print("ADVERB == 0")

    a_a, b_a = builder(w1, w2, pos1 = 'a', pos2 = 'a')
    if check(a_a, b_a) == 0: print("ADJECTIVE[a] == 0")

    a_s, b_s  = builder(w1, w2, pos1 = 's', pos2 = 's')
    if check(a_s, b_s) == 0: print("ADJECTIVE[s] == 0")


# -------------------------------------------------------------------------
def extra_word_lcs_similarity(w1, w2, pos1 = None, pos2 = None, option = None):
    a_n, b_n  = builder(w1, w2, pos1 = 'n', pos2 = 'n')
    if check(a_n, b_n) == 0: print("NOUN == 0")
    else: prob_lcs = word_lcs_similarity(w1, w2, pos1='n', pos2='n', option=option)

# -------------------------------------------------------------------------
def extra_word_wup_similarity(w1, w2, pos1 = None, pos2 = None, option = None):
    a_n, b_n  = builder(w1, w2, pos1 = 'n', pos2 = 'n')
    if check(a_n, b_n) == 0: print("NOUN == 0")
    else: prob_wup = word_wup_similarity(w1, w2, pos1='n', pos2='n', option=option)

# -------------------------------------------------------------------------
def extra_word_res_similarity(ic, w1, w2, pos1 = None, pos2 = None, option = None):
    a_n, b_n  = builder(w1, w2, pos1 = 'n', pos2 = 'n')
    if check(a_n, b_n) == 0: print("NOUN == 0")
    else: word_res_similarity(ic, w1, w2, pos1='n', pos2='n', option=option)

#################################################################################
############################## TESTING ##########################################
#################################################################################
w1, w2 = "dog", "cat"
ic = wn.ic(genesis, False, 0.0)

testing = "none"

if testing == "first" or testing == "all":
    print("------------------ Testing : pos1='n' | pos2='n' | option='first' ------------------")

    """ Path Similarity """
    a = word_path_similarity(w1, w2, pos1='n', pos2='n', option="first")

    """ Lcs Similarity """
    b = word_lcs_similarity(w1, w2, pos1='n', pos2='n', option="first")

    """ Wup Similarity """
    c = word_wup_similarity(w1, w2, pos1='n', pos2='n', option="first")

    """ Res Similarity """
    d = word_res_similarity(ic, w1, w2, pos1='n', pos2='n', option="first")

if testing == "avg" or testing == "all":
    print("------------------ Testing : pos1='n' | pos2='n' | option='avg' ------------------")

    """ Path Similarity """
    a = word_path_similarity(w1, w2, pos1='n', pos2='n', option="avg")

    """ Lcs Similarity """
    b = word_lcs_similarity(w1, w2, pos1='n', pos2='n', option="avg")

    """ Wup Similarity """
    c = word_wup_similarity(w1, w2, pos1='n', pos2='n', option="avg")

    """ Res Similarity """
    d = word_res_similarity(ic, w1, w2, pos1='n', pos2='n', option="avg")

if testing == "min" or testing == "all":
    print("------------------ Testing : pos1='n' | pos2='n' | option='min' ------------------")

    """ Path Similarity """
    a = word_path_similarity(w1, w2, pos1='n', pos2='n', option="min")

    """ Lcs Similarity """
    b = word_lcs_similarity(w1, w2, pos1='n', pos2='n', option="min")

    """ Wup Similarity """
    c = word_wup_similarity(w1, w2, pos1='n', pos2='n', option="min")

    """ Res Similarity """
    d = word_res_similarity(ic, w1, w2, pos1='n', pos2='n', option="min")
