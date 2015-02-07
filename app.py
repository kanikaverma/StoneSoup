from flask import Flask, jsonify
import requests

app = Flask(__name__)
app.config["DEBUG"]=True
api = "dvx4yULlpPc1cRE1bcrpm68WCoKG2z9X"
auth = "api_key={" + api + "}"

@app.route('/')
def hello():
	return "Hello World! It's all happening right now!"

@app.route('/home')
def hellothere():
	return "<h1>Homepage boi<h1><h2>of College Chef</h2><p>Welcome to my Lair</p>"
#euniceemefakokore6c2i2
#dynamic routes with dynamicness! <define variable>
#<this is a variable> it can be overloaded into the function! wow!
@app.route('/home/<food_query>')

def getNews(food_query):
	dataType = 'json'
	url = "http://api.bigoven.com/recipes?any_kw=%s&pg=1&rpp=20&api_key=dvx4yULlpPc1cRE1bcrpm68WCoKG2z9X" % food_query
	return url
	
	response_dict = xmltodict.parse(requests.get(url))
	return jsonify(response_dict)
	#return requests.get(url)

@app.route('/sounds/<track_id>')
def getSongs(track_id):
	tracks = client.get('/tracks/title', q=track_id)
	return tracks

@app.errorhandler(404)
def page_not_found(error):
	return "Sorry this pagenizzle hasn't been found my friend."

if __name__ == '__main__':
	app.run('0.0.0.0')
