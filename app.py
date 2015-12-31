from flask import Flask, jsonify, render_template, redirect, request
import requests

app = Flask(__name__)
app.config["DEBUG"]=True

@app.route('/')
def hello():
	return render_template('index.html')

@app.route('/search')
def search():
  return render_template('search.html')

@app.route('/results', methods=["GET", "POST"])
def get_results():
  food_query = request.form['text']
  food_query_processed = food_query.lower()
  return redirect('/home/'+ food_query_processed)

#dynamic routes with dynamicness! <define variable>
#<this is a variable> it can be overloaded into the function! wow!
@app.route('/home/<food_query>')
def getNews(food_query):
  response = requests.get("https://community-food2fork.p.mashape.com/search?key=fb087049410336a1a564b4d90772884a&q=%s"% food_query, headers = {
  "X-Mashape-Key": "wBtGgGCJ65mshgqXuQksMa9vpohbp1RzC3AjsnKXEHKeWKqZH3",
  "Accept": "application/json"
  }).json()
  recipes = response['recipes']
  return render_template("results.html", recipes=recipes)

@app.errorhandler(404)
def page_not_found(error):
	return "Sorry this pagenizzle hasn't been found my friend."

if __name__ == '__main__':
	app.run('0.0.0.0')
