from nltk.corpus import wordnet as wn
from nltk.corpus import genesis
from nltk.corpus import wordnet_ic

# -------------------------------------------------------------------------
def builder(w1, w2, pos1 = None, pos2 = None):
    a,b = [],[]

    # @todo Add "A" character as option
    # @body "A" character will combine both "a" & "s" adjective's options

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
    # print("word_path_similarity ============================================")

    a,b = builder(w1,w2,pos1,pos2)

    if len(a) == 0 or len(b) == 0:
        if len(a) == 0: print("\tPath similarity: Invalid size for w1, returning...")
        if len(b) == 0: print("\tPath similarity: Invalid size for w2, returning...")

        return 0

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

        print(f"\tPath similarity : {c}\n")

        return c

# -------------------------------------------------------------------------
def word_lcs_similarity(w1, w2, pos1=None, pos2=None, option=None):
    # print("word_lcs_similarity ============================================")

    a,b = builder(w1,w2,pos1,pos2)
    pos_flag = False

    if len(a) == 0 or len(b) == 0:
        if len(a) == 0: print("\tLch similarity: Invalid size for w1, returning...")
        if len(b) == 0: print("\tLch similarity: Invalid size for w2, returning...")

        return 0

    else:
        # Option : First (None)
        if option == None or option == 'first': c = a[0].lch_similarity(b[0])

        # @todo Fix 'Average' for lcs_similarity
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

        # @todo Fix 'Minimum' for lcs_similarity
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

        if pos_flag == True: print("\t** Lch similarity : Ignoring pairs with mismatched pos values...")

        print(f"\tLch similarity : {c}\n")

        return c

# -------------------------------------------------------------------------
def word_wup_similarity(w1, w2, pos1=None, pos2=None, option=None):
    # print("word_wup_similarity ============================================")

    a,b = builder(w1,w2,pos1,pos2)

    if len(a) == 0 or len(b) == 0:
        if len(a) == 0: print("\tWup similarity: Invalid size for w1, returning...")
        if len(b) == 0: print("\tWup similarity: Invalid size for w2, returning...")

        return 0

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

        print(f"\tWup similarity : {c}\n")

        return c

# -------------------------------------------------------------------------
def word_res_similarity(ic, w1, w2, pos1=None, pos2=None, option=None):
    # print("word_res_similarity ============================================")

    a,b = builder(w1,w2,pos1,pos2)
    pos_flag = False

    if len(a) == 0 or len(b) == 0:
        if len(a) == 0: print("\tResnik similarity: Invalid size for w1, returning...")
        if len(b) == 0: print("\tResnik similarity: Invalid size for w2, returning...")

        return 0

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

        if pos_flag == True: print("\t** Resnik similarity : Ignoring pairs with mismatched pos values...")
        print(f"\tResnik similarity : {c}\n")

        return c


#################################################################################
############################## TESTING ##########################################
#################################################################################
w1 = "dog"
w2 = "cat"

testing = "all"

# Path Similarity : DONE ########################################################

""" Word Path Similarity : first (DONE) """
if testing == "first_ps" or testing == "ps" or testing == "all":
    a = word_path_similarity(w1, w2, option="first")
    print(a)
    b = word_path_similarity(w1, w2, pos1='n', option="first")
    print(b)
    c = word_path_similarity(w1, w2, pos2='n', option="first")
    print(c)
    d = word_path_similarity(w1, w2, pos1='n', pos2='n', option="first")
    print(d)


""" Word Path Similarity : avg (DONE) """
if testing == "avg_ps" or testing == "ps" or testing == "all":
    a = word_path_similarity(w1, w2, option="avg")
    print(a)
    b = word_path_similarity(w1, w2, pos1='n', option="avg")
    print(b)
    c = word_path_similarity(w1, w2, pos2='n', option="avg")
    print(c)
    d = word_path_similarity(w1, w2, pos1='n', pos2='n', option="avg")
    print(d)

""" Word Path Similarity : min (DONE) """
if testing == "min_ps" or testing == "ps" or testing == "all":
    a = word_path_similarity(w1, w2, option="min")
    print(a)
    b = word_path_similarity(w1, w2, pos1='n', option="min")
    print(b)
    c = word_path_similarity(w1, w2, pos2='n', option="min")
    print(c)
    d = word_path_similarity(w1, w2, pos1='n', pos2='n', option="min")
    print(d)

# LCS Similarity : !Done ########################################################

""" Word Lcs Similarity : first (DONE) """
if testing == "first_lcs" or testing == "lcs" or testing == "all":
    a = word_lcs_similarity(w1, w2, option="first")
    print(a)
    b = word_lcs_similarity(w1, w2, pos1='n', option="first")
    print(b)
    c = word_lcs_similarity(w1, w2, pos2='n', option="first")
    print(c)
    d = word_lcs_similarity(w1, w2, pos1='n', pos2='n', option="first")
    print(d)

""" Word Lcs Similarity : avg """
if testing == "avg_lcs" or testing == "lcs" or testing == "all":
    a = word_lcs_similarity(w1, w2, option="avg")
    print(a)
    b = word_lcs_similarity(w1, w2, pos1='n', option="avg")
    print(b)
    c = word_lcs_similarity(w1, w2, pos2='n', option="avg")
    print(c)
    d = word_lcs_similarity(w1, w2, pos1='n', pos2='n', option="avg")
    print(d)

""" Word Lcs Similarity : min """
if testing == "min_lcs" or testing == "lcs" or testing == "all":
    a = word_lcs_similarity(w1, w2, option="min")
    print(a)
    b = word_lcs_similarity(w1, w2, pos1='n', option="min")
    print(b)
    c = word_lcs_similarity(w1, w2, pos2='n', option="min")
    print(c)
    d = word_lcs_similarity(w1, w2, pos1='n', pos2='n', option="min")
    print(d)

# Wup Similarity : Done #########################################################

""" Word Wup Similarity : first (DONE) """
if testing == "first_wup" or testing == "wup" or testing == "all":
    a = word_wup_similarity(w1, w2, option="first")
    print(a)
    b = word_wup_similarity(w1, w2, pos1='n', option="first")
    print(b)
    c = word_wup_similarity(w1, w2, pos2='n', option="first")
    print(c)
    d = word_wup_similarity(w1, w2, pos1='n', pos2='n', option="first")
    print(d)

""" Word Wup Similarity : avg (DONE) """
if testing == "avg_wup" or testing == "wup" or testing == "all":
    a = word_wup_similarity(w1, w2, option="avg")
    print(a)
    b = word_wup_similarity(w1, w2, pos1='n', option="avg")
    print(b)
    c = word_wup_similarity(w1, w2, pos2='n', option="avg")
    print(c)
    d = word_wup_similarity(w1, w2, pos1='n', pos2='n', option="avg")
    print(d)

""" Word Wup Similarity : min (DONE) """
if testing == "min_wup" or testing == "wup" or testing == "all":
    a = word_wup_similarity(w1, w2, option="min")
    print(a)
    b = word_wup_similarity(w1, w2, pos1='n', option="min")
    print(b)
    c = word_wup_similarity(w1, w2, pos2='n', option="min")
    print(c)
    d = word_wup_similarity(w1, w2, pos1='n', pos2='n', option="min")
    print(d)

# Res Similarity : !Done ########################################################

""" Word Res Similarity : first """
if testing == "first_res" or testing == "res" or testing == "all":
    ic = wn.ic(genesis, False, 0.0)
    a = word_res_similarity(ic, w1, w2, option="first")
    print(a)
    b = word_res_similarity(ic, w1, w2, pos1='n', option="first")
    print(b)
    c = word_res_similarity(ic, w1, w2, pos2='n', option="first")
    print(c)
    d = word_res_similarity(ic, w1, w2, pos1='n', pos2='n', option="first")
    print(d)

""" Word Res Similarity : avg """
if testing == "avg_res" or testing == "res" or testing == "all":
    ic = wn.ic(genesis, False, 0.0)
    a = word_res_similarity(ic, w1, w2, option="avg")
    print(a)
    b = word_res_similarity(ic, w1, w2, pos1='n', option="avg")
    print(b)
    c = word_res_similarity(ic, w1, w2, pos2='n', option="avg")
    print(c)
    d = word_res_similarity(ic, w1, w2, pos1='n', pos2='n', option="avg")
    print(d)

""" Word Res Similarity : min """
if testing == "min_res" or testing == "res" or testing == "all":
    ic = wn.ic(genesis, False, 0.0)
    a = word_res_similarity(ic, w1, w2, option="min")
    print(a)
    b = word_res_similarity(ic, w1, w2, pos1='n', option="min")
    print(b)
    c = word_res_similarity(ic, w1, w2, pos2='n', option="min")
    print(c)
    d = word_res_similarity(ic, w1, w2, pos1='n', pos2='n', option="min")
    print(d)
