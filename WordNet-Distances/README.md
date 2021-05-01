# WordNet Distances

NLTK provides support for WordNet. In additional to the Wordnetcorpus you can download, it provides an API
that allow you to search for synsets, and also provide functions for the Wordnet similarity/distance measure.
The following URLs provide refenrences as well as examples:

Reference: [nltk.corpus.reader.wordnet -- NLTK 3.6.2 documentation](https://www.nltk.org/_modules/nltk/corpus/reader/wordnet.html)

Example: [WordNet Interface (nltk.org)](http://www.nltk.org/howto/wordnet.html)

(Notice that you should import nltk.corpus.wordnet (not nltk.corpus.reader.wordnet))

I also have a small program to give you some idea on how to use some of the functions.

This program will extend the similarity measures provided by Wordnet. Those similarity measures are based
on the similarity of two senses. However, sometimes you only know the wordbut not the sense, and you still
want to make use of those similarities...
- <code>word_path_similarity(w1, w2, pos1 = None, pos2 = None,  option = None)</code>
  
  Given two words, generate all pairs of x.path_similarity(y), where x is a sense of w1 and y is a sense of w2.
  Then return the value base on what is supplied to the option:
  - default (option not provided): return the maximum value.
  - <code>option = "first"</code>: only consider the first sense of each word (i.e. returned by the synset function)
    and return that value (in this case you don’t need to loop through all values).
  - <code>option = "avg"</code>: return the average value of the path similarity between every pair of senses.
  - <code>option = "min"</code>: return the minimum value of the path.
  
  The pos1 and pos2 parameters determine whether you want to only look at certain part of speech for w1 and w2
  respectvely. In WordNet, the pos is denoted as follows:
  - _v_ for verb
  - _n_ for noun
  - _r_ for adverb
  - adjectrives are sub-divided into two classes a & s.
  So <code>pos</code> can be one of the five characters _"vnras"_. We also allow _"A"_ as a character to allow one to select
  both kind of adjectives.
- <code>word_lcs_similarity(w1, w2, pos1 = None, pos2 = None,  option = None)</code>
- <code>word_wup_similarity(w1, w2, pos1 = None, pos2 = None,  option = None)</code>
  
  Similar to above, but use lcs (wup) similarity instead of path similarity. Notice that for lcs if the part
  of speech of the synset 
- <code>word_res_similarity(ic, w1, w2, pos1 = None, pos2 = None,  option = None)</code>
  
  Similar to above, but use Resnik similarity. The first paraemeter _(ic)_ is the information content needed by the <code>res_similarity()</code> function.
  
  
# Part 2

When calculating the similarity measures above, we need to calculate similarity of various pairs of synsets. However for synsets other than nouns,
while there are hypernyms trees for other part-of-speech in Wordnet, there is no singletree that cover everything, so the calculation may not
yield anything useful.

Sp in this extra credit, you are to modify the functions above by introducingnew methods to calculate similarity of synsets.

For each of the functions in the base case, we still consider calculating the similarity of each pair of synsets. However, in this case we only
consider synset that has the same part of speech (for adjectives, we consider _'a'_ and _'s'_ to be the same).

So for every pair of synsets that have the same part of speech. We calculate the similarity value as follows:
- If both ofthem are nouns, then we use the basic <code>path_similarity()</code>, <code>lch_similarity()</code> etc. provided by WordNet API to calculate
  the similarity. Otherwise, we use the notion of derivationally related forms provided by WordNet.Derivationally related forms is something like the root
  of a word. Notice that in Wordnet API, derivationally related terms are only defined on lemmas, not synset. However, we can generate the set of
  derivationally related synsets of _a_ synset _h_ using the following set:
  - Use the <code>lemmas()</code> method to generate the list of leammas for _h_.
  - For each lemma, call the <code>derivationally_related_forms()</code> method to generate a list related derivationally related forms (it will be a list of lemmas).
  - For each lemma, call the <code>synset()</code> method to generate the corresponding synset.
  
  So given two non-noun synsets _(p, q)_ that have the same part of speech, we define the similarity (_path, lch_ etc.) of that synset by compare all pairs of synset
  generated from the steps above (one for _p_ and one for _q_) and return the value (_max, min,. average, first_ etc.) according to the main function’s parameter.
  
  Notice that if a (non-noun) synset does not have any derivationally related forms, you should ignore that synset in the calcualtion

Your task is to modify the similarity measures defined in the base caseto account for that. You should name your functions 
<code>extra_word_path_similairty()</code>, <code>extra_word_lcs_similarity()</code> etc. 
