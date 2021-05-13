
# coding: utf-8

# In[1]:


from sklearn.feature_extraction.text import CountVectorizer

def getBagOfWords(corpus):
#     print(corpus)
    
    vectorize = CountVectorizer(stop_words='english',lowercase=True,analyzer='word')    
    vectorize.fit_transform(corpus).todense()
    
    return vectorize.vocabulary_


# In[2]:


def getBestTags(bow):    
    
    # sort by frequency
    wordsFreq = sorted(bow, key=bow.get,reverse=True)
    
#     print(wordsFreq)
    onlyAlphas = []
    
    # skip non alphas
    [onlyAlphas.append(word) for word in wordsFreq if word.isalpha()]
    
    print(onlyAlphas[0:5])    
    return onlyAlphas[0:5]
    


# In[ ]:


# connect to Es and get content and print each 

