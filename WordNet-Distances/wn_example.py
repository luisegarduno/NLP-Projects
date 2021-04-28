from nltk.corpus import wordnet as wn
from nltk.corpus import genesis
from nltk.corpus import brown
from nltk.corpus import gutenberg

print("All synsets of 'clear'")
x = wn.synsets('clear')
print(wn.synsets('clear'))

# Pick a synset out of the list
s0 = x[1]
print("Single synset : ", s0)
print("name : ", s0.name())
print("lexname : ", s0.lexname())
print("lemma_names : " , s0.lemma_names())
print("lemmas", s0.lemmas())
print("pos : ", s0.pos())
print("root hypernyms : ", s0.root_hypernyms())
print("min depth (from root) : ", s0.min_depth())
print("max depth (from root) : ", s0.max_depth())

# relationships
# other relationships can be found by using the relationship name as functions)
print("hypernyms : ", s0.hypernyms())
print("hyponyms : ", s0.hyponyms())

print("hypernym tree (from root to node): ", s0.hypernym_paths())


# this allows you to form any path from a synset via any relations
hyp = lambda s:s.hypernyms()
print("tree (from node to root) : ", s0.tree(hyp))


print("\n\n\n");
# create a synset from a string (n is noun, a/s is ajdective, v is verb, 
my_syn = wn.synset('dog.n.01')
print("Single synset : ", my_syn)
print("name : ", my_syn.name())
print("lexname : ", my_syn.lexname())
print("lemma_names : " , my_syn.lemma_names())
print("lemmas", my_syn.lemmas())
print("pos : ", my_syn.pos())
print("root hypernyms : ", my_syn.root_hypernyms())
print("min depth (from root) : ", my_syn.min_depth())
print("max depth (from root) : ", my_syn.max_depth())

# relationships
# other relationships can be found by using the relationship name as functions)
print("hypernyms : ", my_syn.hypernyms())
print("hyponyms : ", my_syn.hyponyms())

print("hypernym tree (from root to node): ", my_syn.hypernym_paths())


# this allows you to form any path from a synset via any relations
hyp = lambda s:s.hypernyms()
print("tree (from node to root) : ", my_syn.tree(hyp))

print("\n\n\n");

# similarity
print("Path similarity : ", s0.path_similarity(my_syn))
print("Lch similarity : ", s0.lch_similarity(my_syn))
print("Wup similarity : ", s0.wup_similarity(my_syn))


# import corpus for infomration content 
genesis_ic = wn.ic(genesis,  False, 0.0)
brown_ic = wn.ic(brown, False, 0.0)
gutenberg_ic = wn.ic(gutenberg, False, 0.0)
print("Resnik sim with ic (genesis) ", s0.res_similarity(my_syn, genesis_ic))
print("Resnik sim with ic (brown) ", s0.res_similarity(my_syn, brown_ic))
print("Resnik sim with ic (brown) ", s0.res_similarity(my_syn, gutenberg_ic))



# verbs

run1 = wn.synset('run.v.01')
catch1 = wn.synset('catch.v.01')
draw1 = wn.synset('draw.v.03')
print("Path similarity : ", run1.path_similarity(catch1))
print("Lch similarity : ", run1.lch_similarity(catch1))
print("Wup similarity : ", run1.wup_similarity(catch1))

print("Path similarity : ", run1.path_similarity(draw1))
print("Lch similarity : ", run1.lch_similarity(draw1))
print("Wup similarity : ", run1.wup_similarity(draw1))

