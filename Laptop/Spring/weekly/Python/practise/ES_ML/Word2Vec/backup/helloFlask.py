from flask import Flask
app = Flask(__name__)

name = 'yadav'

@app.before_first_request
def loadModel():
	global name
	print('loading model', name)
	name = 'anurag'
	print(name)
	
	
@app.route('/context/of/<term>')
def hello_world(term):
	term= 'hello'
	print (name)
	return name