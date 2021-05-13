
from gensim.models import Word2Vec
from flask import Flask
app = Flask(__name__)


model = Word2Vec.load('word2VecModel.bin')

@app.before_first_request
def loadModel():
	global model
	print('Loaded model', model)
	
@app.route('/context/of/<term>')
def hello_world(term):
	
	listTupleSimilar = model.wv.most_similar(term)
	unzippedTupleSimilar = zip( *listTupleSimilar )
	listSimilar = list(unzippedTupleSimilar)
	similars = listSimilar[0]
	
	return ','.join(similars)