from flask import Flask
from flask import jsonify
from content_based_recommender import resultsList

app = Flask(__name__)

@app.route('/')
def hello_world():
   results = resultsList()
   return jsonify({"payload" : results})

if __name__ == '__main__':
   app.run()