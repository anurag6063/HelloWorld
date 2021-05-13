
# coding: utf-8

# # Creating Word2Vec model
# ## Objective: Load given file remove stopwords, create/update a model and save as binary file.
# 
# 

# 1. Import the required packages.
# 2. create a class: vocabulary and files to be parsed.
# 3. Create iterator that can read each line and removes stopwords.
#	Use stemmer to stem english words.
#	The length of the word should be b/w 2 to 15.
#	All the words in the file 'stopwords.txt' will be removed.   
# 4. 

# In[52]:


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


# In[53]:


parser =argparse.ArgumentParser(description='Pass list of file names to be converted in word2Vec')
parser =argparse.ArgumentParser(description='Pass list of file names to be converted in word2Vec')

parser.add_argument("-l", "--list", nargs='+', type=str, dest = 'file', help='Enter list of files')
args = parser.parse_args()

fileList = args.file
files = fileList[0]
inputFiles = files.split(' ')
print(files.split(' '))


# In[40]:


# get a english stemmer to convert words into their original form
stemmer = SnowballStemmer('english')

# load file which contains words that should not be a part of word2vec model
removeWords = pd.read_csv('stopwords.txt').values


# Create class to capture file and its text.
# 

# In[41]:


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
		


# Load the file and pass it to the WordsOfFile class. 
# 
#	 This will initialize vocabulary and run iterator on it.
#	 We can pass multiple files too. keep the size small of you want to see the model generated after each file. 
#	 
# 

# In[42]:


wordsOfFile = WordsOfFile(['MB1.txt'])

model = gensim.models.Word2Vec(wordsOfFile, min_count=100)


# Send this words in file to gensim. It will create a vector represntation of each word.

# In[43]:

if os.path.isfile("word2VecModel.bin"):
	print("Yes, word2VecModel.bin Model exists. Will update the existing model with new file")
	model = Word2Vec.load("word2VecModel.bin")
	model.build_vocab(wordsOfFile,update=True)
	model.train(wordsOfFile)
	model.save('word2VecModel.bin')
else:
	print("No, model found. Creating a new Word2Vec model.")
	word2VecModel = gensim.models.FastText(wordsOfFile, min_count=100, size=5, workers=4, min_alpha=2.0, max_n=7)
	
	# save the model to the disk in binary format.
	word2VecModel.save('word2VecModel.bin')
	


# In[44]:



print("All the words have been extracted and converted in Word2Vec and saved as binary file at the location from where the program is being run")

