from flask import Flask, jsonify
import requests

app = Flask(__name__)
app.config["DEBUG"]=True

@app.route('/')
def hello():
	return "Hello World! It's all happening right now!"

@app.route('/home')
def hellothere():
	return "<h1>Homepage boi<h1><h2>of Stone Soup</h2><p>Welcome to our Kitchen!</p>"

#dynamic routes with dynamicness! <define variable>
#<this is a variable> it can be overloaded into the function! wow!
@app.route('/home/<food_query>')
def getNews(food_query):
	url = "http://food2fork.com/api/search/%s" % food_query
	response_dict = requests.get(url)
	return response_dict
	#return requests.get(url)

@app.errorhandler(404)
def page_not_found(error):
	return "Sorry this pagenizzle hasn't been found my friend."

if __name__ == '__main__':
	app.run('0.0.0.0')
