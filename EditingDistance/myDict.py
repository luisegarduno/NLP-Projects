#
# Created by Luis Garduno : 2/10/2021
#

def getDistance(str1, str2, idx1, idx2, deleteCost, subCostList) :

    # Return the remaining characters of other string
    if idx1 == 0 : return idx2
    if idx2 == 0 : return idx1

    # Check for recursive tree
    if subCostList[idx1][idx2] != (-1 * deleteCost) :
        return subCostList[idx1][idx2];

    # If characters are equal, execute recursive function for (idx1 - 1) , (idx2 - 1)
    if str1[idx1 - 1] == str2[idx2 - 1]  :
        if subCostList[idx1 - 1][idx2 - 1] == (-1 * deleteCost) :
            subCostList[idx1][idx2] = getDistance(str1, str2, idx1 - 1, idx2 - 1, deleteCost, subCostList)
            return subCostList[idx1][idx2]
        else :
            subCostList[idx1][idx2] = subCostList[idx1 - 1][idx2 - 1]
            return subCostList[idx1][idx2]

    # If characters are nt equal, Find the minimum cost using one of the 3 operations
    else :
        if subCostList[idx1 - 1][idx2] != (-1 * deleteCost) :
            m1 = subCostList[idx1 - 1][idx2]
        else :
            m1 = getDistance(str1, str2, idx1 - 1, idx2, deleteCost, subCostList)

        if subCostList[idx1][idx2 - 1] != (-1 * deleteCost) :
            m2 = subCostList[idx1][idx2 - 1]
        else :
            m2 = getDistance(str1, str2, idx1, idx2 - 1, deleteCost, subCostList)

        if subCostList[idx1 - 1][idx2 - 1] != (-1 * deleteCost) :
            m3 = subCostList[idx1 - 1][idx2 - 1]
        else :
            m3 = getDistance(str1, str2, idx1 - 1, idx2 - 1, deleteCost, subCostList)

        subCostList[idx1][idx2] = deleteCost  + min(m1, min(m2, m3))
        return subCostList[idx1][idx2]


def editDistance(str1, str2, deleteCost=1, defaultSubCost=2, subCostList={}):
    # Make both strings lowercase
    str1 = str1.lower()
    str2 = str2.lower()

    #deleteCost = deleteCost
    #defaultSubCost = defaultSubCost
    #subCostList = subCostList

    subCostList = [[(-1 * deleteCost) for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]

    return getDistance(str1, str2, len(str1), len(str2), deleteCost, subCostList)

class myDict:

    wordlist = []

    def __init__(self, w):
        self.wordlist = [x for x in w]

    def print(self):
        for x in self.wordlist:
            print(x)

    def search(self, str, maxDistance, deleteCost=1, defaultSubCost=2, subCostList={}):
        self.str = str
        self.maxDistance = maxDistance
        self.deleteCost = deleteCost
        self.defaultSubCost = defaultSubCost
        self.subCostList = subCostList

        return []
