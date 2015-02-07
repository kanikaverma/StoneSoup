from flask import Flask, jsonify
import requests

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
	response = requests.get("https://community-food2fork.p.mashape.com/search?key=fb087049410336a1a564b4d90772884a&q=%s"% food_query,
	                       headers = {
	"X-Mashape-Key": "wBtGgGCJ65mshgqXuQksMa9vpohbp1RzC3AjsnKXEHKeWKqZH3",
	"Accept": "application/json"
  }).json()

	recipeList=""
	for x in response["recipes"]:
		recipeList+="<a href=\""+x["source_url"]+"\">"+x["title"]+"</a><br><img src=\""+x["image_url"]+"\"/>"+"<br><button id=\""+x["recipe_id"]+"\">Shopping List</button>""<br><br>"
	
	recipe_id=response["recipes"][0]["recipe_id"]
	recipe_url=response["recipes"][0]["source_url"]
	recipe_title=response["recipes"][0]["title"]
	print recipe_title
	print recipe_id
	print recipe_url

  	return recipeList




@app.errorhandler(404)
def page_not_found(error):
	return "Sorry this pagenizzle hasn't been found my friend."

if __name__ == '__main__':
	app.run('0.0.0.0')
