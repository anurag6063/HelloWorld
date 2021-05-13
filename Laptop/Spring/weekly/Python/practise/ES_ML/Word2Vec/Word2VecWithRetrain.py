# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 12:56:43 2018

@author: anuryadav
"""


# contails word2vec model
import gensim
from gensim.models import Word2Vec

# help in reading files from system
import os
import os.path

# regular expression to get words from line.
import re

# natural language processor
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem.snowball import SnowballStemmer

# pandas to load file
import pandas as pd

# to get best feature representation
from sklearn.decomposition import PCA

# to get list of files from command line
import argparse

# get a english stemmer to convert words into their original form
stemmer = SnowballStemmer('english')

# load file which contains words that should not be a part of word2vec model
removeWords = pd.read_csv('stopwords.txt').values



class WordsOfFile(object):
    def __init__(self, fileNames):
        self.fileNames = fileNames
        self.vocabulary = set([])        
        print('Files being read are: ', fileNames)
        
    def __iter__(self):
        for fileName in self.fileNames:
            print('Processing file: ', fileName)
            
            # reading each line of the file
            for line in open(fileName, encoding='latin1'):
                # get list of all words of length b/w 2 to 15
                words = re.findall(r'(\b[A-Za-z][a-z]{2,15}\b)', line)
                #skip all removeable words. reamining words should be stemmed.
                words = [stemmer.stem(word.lower()) for word in words if not word.lower() in removeWords]
                # add all the words in set. using generator as its more memory efficient
                for word in words:
                    self.vocabulary.add(word)
                    
                # yield the vocabulary. this will let you iterate over list of words just once but in every efficient way.
                yield words
        


wordsOfFile = WordsOfFile(['MB1.txt'])

gensim.models.Word2Vec([["hey"]],min_count=10)
