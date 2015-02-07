from flask import Flask, jsonify
import requests, unirest

app = Flask(__name__)
app.config["DEBUG"]=True

@app.route('/')
def hello():
	return "Hello We are cool! It's all happening right now!"

@app.route('/home')
def hellothere():
	return "<h1>Homepage boi<h1><h2>of Stone Soup</h2><p>Welcome to our Kitchen!</p>"

#dynamic routes with dynamicness! <define variable>
#<this is a variable> it can be overloaded into the function! wow!
@app.route('/home/<food_query>')
def getNews(food_query):
	response = unirest.get("https://community-food2fork.p.mashape.com/search?key=fb087049410336a1a564b4d90772884a&q=%s",
	                       headers = {
	"X-Mashape-Key": "wBtGgGCJ65mshgqXuQksMa9vpohbp1RzC3AjsnKXEHKeWKqZH3",
	"Accept": "application/json"
  }).json()
  	return jsonify(response.raw_body)

@app.errorhandler(404)
def page_not_found(error):
	return "Sorry this pagenizzle hasn't been found my friend."

if __name__ == '__main__':
	app.run('0.0.0.0')
