from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)
app.config["DEBUG"]=True

@app.route('/')
def hello():
	return "Hello We are cool! It's all happening right now!"

@app.route('/home')
def hellothere():
	return "<h1>StoneSoup<h1><h2>Welcome to our kitchen!</h2><p>Here's what you should make today!</p>"

#dynamic routes with dynamicness! <define variable>
#<this is a variable> it can be overloaded into the function! wow!
@app.route('/home/<food_query>')
def getNews(food_query):
	response = requests.get("https://community-food2fork.p.mashape.com/search?key=fb087049410336a1a564b4d90772884a&q=%s"% food_query,
	                       headers = {
	"X-Mashape-Key": "wBtGgGCJ65mshgqXuQksMa9vpohbp1RzC3AjsnKXEHKeWKqZH3",
	"Accept": "application/json"
  }).json()

	recipeList="<html><head><link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css\"><title size=\"20\">StoneSoup</title></head><body bgcolor=\"7fffd4\"><center><h1>StoneSoup<h1><h2>Welcome to our kitchen!</h2><p>Here's what you should make today!</p>"
	for x in response["recipes"]:
		recipeList+="<h3><a href=\""+x["source_url"]+"\">"+x["title"]+"</a></h3><br><img src=\""+x["image_url"]+"\"/>"+"<br><br>"
	

	recipeList+="</center></body></html>"
	return recipeList
  	#return render_template("StoneSoup.html", recipeList = recipeList)




@app.errorhandler(404)
def page_not_found(error):
	return "Sorry this pagenizzle hasn't been found my friend."

if __name__ == '__main__':
	app.run('0.0.0.0')
