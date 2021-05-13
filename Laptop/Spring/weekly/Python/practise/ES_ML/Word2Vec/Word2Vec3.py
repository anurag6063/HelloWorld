# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 13:20:15 2018

@author: anuryadav
"""

import gensim
import os
import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem.snowball import SnowballStemmer

import pandas
import argparse

def getFileFromCL():
   
    return inputFiles

#inputFiles = getFileFromCL()
inputFiles = ['MB1.txt']


stemmer = SnowballStemmer("english")
stopwords = pd.read_csv('stopwords.txt')

class Sentences(object):
    def __init__(self, files):
        self.files = files
        print(self.files)
        
        self.vocabulary = set ([])
        
    def __iter__(self):
        for file in self.files:
            print('Reading file names: ', file)
            
            for line in open(file, encoding='latin1'):
                words = re.findall(r'(\b[A-Za-z][a-z]{2,15}\b)', line)
                words = [stemmer.stem(word.lower()) for word in words if not word.lower() in stopwords ]
#                words = [ stemmer.stem(word.lower()) for word in words if not word.lower() in stopWords]

                
                for word in words:
                    self.vocabulary.add(word)
                print('volcabulary contains', self.vocabulary, words)
                
                yield words
                

sentences = Sentences(['MB1.txt'])

if os.path.isfile('model-word2vec.bin'):
    print("Yes, model-word2vec.bin; Model exists. Will update the existing model with new file")
    model = gensim.models.Word2Vec.load('model-word2vec.bin')
    model.build_vocab(sentences,update=True)
    model.train(sentences)
    model.save('model-word2vec.bin')
else:
    print('No exsiting model found')
    model = gensim.models.Word2Vec(sentences, min_count=1)
    model.save('model-word2vec.bin')
#model = gensim.models.Word2Vec(sentences, min_count=1)


model.wv.vocab
model.wv.most_similar('conceiv')