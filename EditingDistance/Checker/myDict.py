#
# Created by Luis Garduno : 2/10/2021
#

def getDistance(X, Y, i, j, cost, D):

    # Check if either of the strings are a base case, if so return value 
    if i == 0: return j
    if j == 0: return i

    # Check for recursive tree
    if D[i][j] != (-1 * cost):
        return D[i][j]

    # If characters are equal, execute recursive function for (i - 1) , (j - 1)
    if X[i - 1] == Y[j - 1]:
        if D[i - 1][j - 1] == (-1 * cost):
            D[i][j] = getDistance(X, Y, i - 1, j - 1, cost, D)
            return D[i][j]
        else:
            D[i][j] = D[i - 1][j - 1]
            return D[i][j]

    # If characters aren't equal, find the minimum cost using one of the 3 options 
    else:
        # Option 1 -----------> D(i - 1, j) + 1 
        if D[i - 1][j] != (-1 * cost):
            m1 = D[i - 1][j]
        else:
            m1 = getDistance(X, Y, i - 1, j, cost, D)

        # Option 2 -----------> D(i, j - 1) + 1 
        if D[i][j - 1] != (-1 * cost):
            m2 = D[i][j - 1]
        else:
            m2 = getDistance(X, Y, i, j - 1, cost, D)

        # Option 3 -----------> D(i - 1, j - 1) + 
        if D[i - 1][j - 1] != (-1 * cost):
            m3 = D[i - 1][j - 1]
        else:
            m3 = getDistance(X, Y, i - 1, j - 1, cost, D)

        # Get minimum value
        D[i][j] = cost + min(m1, min(m2, m3))
        return D[i][j]

def editDistance(str1, str2, deleteCost=1, defaultSubCost=2, subCostList={}):
    # Make both strings lowercase
    str1 = str1.lower()
    str2 = str2.lower()

    # Create a distance matrix distance [n + 1, m + 1]
    subCostList = [[(-(deleteCost) * defaultSubCost) for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]

    return getDistance(str1, str2, len(str1), len(str2), defaultSubCost, subCostList)

class myDict:

    wordlist = []

    def __init__(self, w):
        self.wordlist = [x for x in w]

    def print(self):
        for x in self.wordlist:
            print(x)

    def search(self, strs, maxDistance, deleteCost=1, defaultSubCost=2, subCostList={}):
        self.strs = strs.lower()
        self.maxDistance = maxDistance
        self.deleteCost = deleteCost
        self.defaultSubCost = defaultSubCost
        self.subCostList = subCostList

        close_words = []
        for i in self.wordlist:
            val = editDistance(strs, i.lower(), defaultSubCost=self.defaultSubCost, subCostList=self.subCostList)
            if val <= maxDistance:
                close_words.append(i.lower())
        return close_words
