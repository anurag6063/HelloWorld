
# coding: utf-8

# In[19]:


from sklearn.feature_extraction.text import CountVectorizer

vectorize = CountVectorizer(stop_words='english',lowercase=True,analyzer='word')    

def getBagOfWords(corpus):
#     print(corpus)
    vectorize.fit(corpus)
#     vectorize.fit_transform(corpus).todense()
    
    return vectorize.vocabulary_


# In[12]:


def getBestTags(bow):    
    
    # sort by frequency
    wordsFreq = sorted(bow, key=bow.get,reverse=True)
    
#     print(wordsFreq)
    onlyAlphas = []
    
    # skip non alphas
    [onlyAlphas.append(word) for word in wordsFreq if word.isalpha()]
    
    print(onlyAlphas[0:5])    
    return onlyAlphas[0:5]
    


# In[13]:


# connect to Es and get content and print each 

from elasticsearch import Elasticsearch


# In[14]:


es = Elasticsearch(
    ['localhost'],
    scheme="http",
    port=9200,
)


# In[15]:


# source https://marcobonzanini.com/2015/02/02/how-to-query-elasticsearch-with-python/

def searchElasticsearchAndTagDoc(term):
    
    result = es.search(index="search_box_v1", doc_type="box_poc", body={ "size": 200,    "query": {     "simple_query_string": {       "query": term,       "fields": ["contentBox"]     }   } })
    for doc in result['hits']['hits']:
        #     print( doc['_id'], ' ' , doc['_source']['contentBox'])  
        corpus = []
        corpus.append(doc['_source']['contentBox'])
        getBestTags(getBagOfWords(corpus))


# In[24]:


searchElasticsearchAndTagDoc("h")


# In[27]:


vectorize.vocabulary_


# In[26]:


getBagOfWords(["123"])

