import os, sys
import numpy as np
import pandas as pd
from nltk import pos_tag
from sklearn.cluster import KMeans
from textblob import Word, TextBlob
from nltk.tokenize import TweetTokenizer
from sklearn.feature_extraction.text import TfidfVectorizer

print("CS 5337 project written by Luis Garduno\n")


# -----------------------------------------------------------------------------
flag = None

if flag:
     # Remove logs/data if it exists
     os.remove('data_crawl.json') if os.path.isfile('data_crawl.json') else None
     os.remove('data_crawl.j1') if os.path.isfile('data_crawl.j1') else None

     # Run the crawler
     os.system('cd scrapy_crawler/spiders')
     os.system('scrapy crawl freemanmoore --logfile data_crawl.log -O data_crawl.json;')
     os.system('cd ../../')


df = pd.read_json('data_crawl.json')
df = df.loc[((df.format=='php')|(df.format=='txt')|(df.format=='html')),['url','format','title','text']]
df['title'] = df['title'].apply(lambda x: x[0] if len(x) > 0 else '')
print("Crawling complete, indexed", df.shape[0], "files.\n")

# -----------------------------------------------------------------------------

def lemmatization(words):
     lemmatized_words = []
     posConv = {'JJ':'a', 'JJR':'a', 'JJS':'a', 'RB':'r', 'RBR':'r', 'RBS':'r',
               'VB':'v', 'VBD':'v', 'VBG':'v', 'VBN':'v', 'VBP':'v', 'VBZ':'v',
               'NN':'n', 'NNS':'n', 'NNP':'n', 'NNPS':'n', 'n':'n', 'a':'a',
               'r':'r', 'v':'v', 's':'s'}

     for item in words:
          item = item.split()
          if len(item) > 1:
               lemPhrase =[]
               for word,tag in pos_tag(item):
                    lemPhrase.append(Word(word).lemmatize(posConv.get(tag)))
               lemmatized_words.append(' '.join(lemPhrase))
          else:
               word,tag = pos_tag(item)[0]
               lemmatized_words.append(Word(word).lemmatize(posConv.get(tag)))

     return lemmatized_words

df_txt = df.loc[:,['text']]
tokenizer = TweetTokenizer()
new_idx = list(range(0, df_txt.shape[0]))
df_txt['idx'] = new_idx
df_txt.set_index('idx', inplace=True)

# -----------------------------------------------------------------------------
class search_engine(object):
     def __init__(self, n_docs = 0, docs ='blank', query = None, vectorizer = None,
               titleDict = None, vector_space = None, title_vector = None,
               vector_df = None, vocabulary = None, title_weight = False):
          self.n_docs = n_docs
          self.docs = docs
          self.query = query
          self.vectorizer = vectorizer
          self.titleDict = titleDict
          self.title_vector = title_vector
          self.vector_space = vector_space
          self.vector_df = vector_df
          self.vocabulary = vocabulary
          self.title_weight = title_weight
          self.query_expanded = False

     @staticmethod
     def find_index(inputs, item):
          return [i for i, j in enumerate(inputs) if j == item]

     def docInput(self, df_docs, scheme='ntc'):
          self.docs = df_docs
          self.n_docs= df_docs.shape[0]
          df_txt= self.docs.loc[:,['title']]
          df_lower = df_txt.applymap(lambda x: x.lower())
          dfTK = df_lower.applymap(lambda x: tokenizer.tokenize(x))
          df_lemmatize = dfTK.applymap(lambda x: lemmatization(x))
          self.docs['Title'] = df_lemmatize.loc[:,'title'].apply(lambda x: ' '.join(x)) 
          all_text = self.docs[['Title','text']].apply(lambda x: ' '.join(x), axis=1)

          title_text = self.docs['Title'].values.tolist()
          txtOverview = all_text.values.tolist()
          vectorizer = TfidfVectorizer(max_df=1.0, max_features=1000, min_df=0.0, stop_words='english',
                                        use_idf=True, norm='l2', smooth_idf=False)
          titleDict = TfidfVectorizer(max_df=1.0, max_features=1000, min_df=0.0, stop_words= None,
                                        use_idf=False, norm=None, smooth_idf = False)
          X = vectorizer.fit_transform(txtOverview)
          y = titleDict.fit_transform(title_text)
          self.titleDict = titleDict
          self.vectorizer = vectorizer
          self.vocabulary = list(vectorizer.vocabulary_.keys())
          self.title_vector = y
          self.vector_space = X
          docs=['doc'+str(i+1) for i in range(0,X.shape[0])]
          self.vector_df = pd.DataFrame(data=X.toarray(), index=docs, columns=vectorizer.get_feature_names_out())
          return self.vector_df

     def search(self, query, K):
          if query != 'stop':
               self.query = query
               query_vector = self.vectorizer.transform([query]).toarray()
               scoreList = np.zeros([1, self.n_docs])[0]
               if self.title_weight:
                    qTitle_Dict = self.titleDict.transform([query]).toarray()
                    title_score = np.transpose(self.title_vector@np.transpose(qTitle_Dict))[0]
                    title_nzero_indices = np.nonzero(title_score)
                    scoreList[title_nzero_indices] = 0.25
               scoreList += np.transpose(self.vector_space@np.transpose(query_vector))[0]
               score_nzero = scoreList[scoreList > 0]
               if len(score_nzero) < K/2:
                    if self.query_expanded:
                         if len(score_nzero) > 0:
                              self.qResults(K, scoreList, score_nzero)
                         else:
                              print('No relevant docs found {0}'.format(len(score_nzero)))
                              self.query_expanded = False
                    else:
                         print('{0} docs match, displaying top K={1}'.format(len(score_nzero), K))
                         print(100*"=")
                         self.qResults(K, scoreList, score_nzero)
               else:
                    print('{1} docs match, displaying top K={0}'.format(K, len(score_nzero)))
                    print(100*"=")
                    self.qResults(K, scoreList, score_nzero)

     def qResults(self, K, scoreList, score_nzero):
          K = min([K,len(score_nzero)])
          topDoc = np.argsort(-scoreList)[:K]
          for (i,idx) in enumerate(topDoc):
               if(i != 0):
                    print('\n{0}\t{1:.4f}\t{2}\t{3}'.format(
                         i+1,
                         scoreList[idx],
                         self.docs.iloc[idx]['url'],
                         self.docs.iloc[idx]['title']
                    ))
               if(i == 0):
                    print('{0}\t{1:.4f}\t{2}\t{3}'.format(
                         i+1,
                         scoreList[idx],
                         self.docs.iloc[idx]['url'],
                         self.docs.iloc[idx]['title']
                    ))
               self.query_expanded = False

     def thesaurus(self):
          return {
               'beautiful': ['nice', 'fancy'], 'chapter': ['chpt'],
               'chpt': ['chapter'], 'responsible': ['owner', 'accountable'],
               'freemanmoore': ['freeman', 'moore'], 'dept': ['department'],
               'brown': ['beige', 'tan', 'auburn'], 'tues': ['Tuesday'],
               'sole': ['owner', 'single', 'shoe', 'boot'],
               'homework': ['hmwk', 'home', 'work'], 'novel': ['book', 'unique'],
               'computer': ['cse'], 'story': ['novel', 'book'],
               'hocuspocus': ['magic', 'abracadabra'], 'thisworks': ['this', 'work']}


engine = search_engine(title_weight=True)
vector_df = engine.docInput(df)

count = 0
aQuery = input('Query: ')
while aQuery != 'stop':
     engine.search(aQuery,K=5)

     print(100*"=")
     aQuery = input('\nQuery: ')
     count+=1

if count == 1:
     print("\n" + str(count) + " query processed.")
else:
     print("\n" + str(count) + " queries processed")
