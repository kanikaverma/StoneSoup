from flask import Flask, jsonify, render_template, redirect, request
import requests

app = Flask(__name__)
app.config["DEBUG"]=True

@app.route('/')
def hello():
	return render_template('search.html', recipes="initial")

@app.route('/search')
def search():
  return render_template('search.html', recipes="initial")

@app.route('/results', methods=["GET", "POST"])
def get_results():
  food_query = request.form['text']
  food_query = food_query.replace(" ", "+")
  food_query_processed = food_query.lower()
  request_string = "https://community-food2fork.p.mashape.com/search?key=fb087049410336a1a564b4d90772884a&q={}".format(food_query_processed)
  response = requests.get(request_string, headers = {
  "X-Mashape-Key": "wBtGgGCJ65mshgqXuQksMa9vpohbp1RzC3AjsnKXEHKeWKqZH3",
  "Accept": "application/json"
  }).json()
  recipes = response['recipes']
  return render_template('search.html', recipes=recipes)

@app.errorhandler(404)
def page_not_found(error):
	return "Sorry this pagenizzle hasn't been found my friend."

if __name__ == '__main__':
	app.run('0.0.0.0')
