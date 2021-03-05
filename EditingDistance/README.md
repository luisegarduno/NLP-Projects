# EditingDistance Algorithm.

## Part 1: editDistance

  _editDistance(str1, str2, deleteCost = 1, defaultSubCost = 2, subCostDict= {})_     
      
  The function take two strings, str1, str2, and return the editing distance between the two strings. You should convert the two
  strings to lowercase before calculating the distance.     
      
  The parameters are as follows:     
  - _str1, str2_: the two strings to be compared     
  - _deleteCost_: the cost of a deletion/insertion (we assume deletion cost and insertion cost are the same).     
  - _defaultSubCost_: the default cost of a substitution (which can be affected by the subCostList dictionary, see below)     
  - _subCostDict_: A dictionary storing the substitution cost between two characters.     
      For this dictionary     
      - key is a tuple of two characters. You can assume the first character is always before the second character.     
      - Value is the cost for substitution for that character.     
      - If a pair of characters is not in the subCostDict, then use defaultSubCost.     
  For example, consider the following call:     

  _editDistance(‘going’, ‘kick’, 2, 3 , d1)_     
  - _Where d1 = {(‘a’, ‘b’): 4, (‘b’, ‘d’): 1, (‘c’, ‘f’): 20, (‘c’, ‘d’): 10, (‘g’, ‘k’): 5.25}_
  
  This will return the editing distance between the string ‘apple’ and ‘ability’, with the following cost:     
  - Insertion/deletion cost : 2    
  - Substitution cost : 3, except the following     
      - From ‘a’ to ‘b’; and from ‘b’ to ‘a’ : 4
      - From ‘b’ to ‘d’ and from ‘d’ to ‘b’ : 1
      - From ‘c’ to ‘f’, and from ‘f’ to ‘c’: 20
      - From ‘c’ to ‘d’ and from ‘d’ to ‘c’: 10
      - From ‘g’ to ‘k’ and from ‘k’ to ‘g’: 5.25 (notice that non integer cost is allowed)

  Then in this case, we can write a recursive formula as this:     
  - _Edit_distance((‘going’, ‘kick’) = min (Edit_distance(‘goin’, ‘kick’) + 2, Edit_distance(‘going’, ‘kic’) + 2, Edit_distance(‘goin’, ‘kic’ + 5.25))_

    (Of course, you are to implement this using dynamic programming)     
     
     
## Part 2: Search  

  Once you have done the first part. You should implement a class call myDict, which store a list of words, and provide a function that match any
  given word to those in the dictionary that is ‘close’ (by editing distance). The details:
  
  Constructor
  - Read in a list of words, representing the words to be stored
       
  Methods
  - _print()_: print the list of the words
  - _search(str, maxDistance, deleteCost, defaultSubCost, subCostList)_: return all words in the object that has editing distance <= maxDistance with str.
    The other parameters are the parameters to be passed to the _editDistance()_ method. You should list the words in alphabetical order.
        
Notes:
- all words are to be converted to lower case before processing
- any non-alphabetical characters will not be in the subCostList array, and should be treated using default values (i.e. assign default cost for deletion/substitution)
