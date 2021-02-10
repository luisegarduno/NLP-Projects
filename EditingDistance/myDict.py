# 
# Created by Luis Garduno : 2/10/2021
#


def editDistance(str1, str2, deleteCost = 1, defaultSubCost = 2, subCostList = {}):
    str1 = str1.lower()
    str2 = str2.lower()
    deleteCost = deleteCost
    defaultSubCost = defaultSubCost
    subCostList = subCostList
    return 0


class myDict:

    wordlist = {}

    def __init__(self, w):
        self.wordlist = {x for x in w}

    def print(self):
        for x in self.wordlist:
            print(x)

    def search(self, str, maxDistance, deleteCost = 1, defaultSubCost = 2, subCostList = {}):
        self.str = str
        self.maxDistance = maxDistance
        self.deleteCost = deleteCost
        self.defaultSubCost = defaultSubCost
        self.subCostList = subCostList

        return {}



