import requests
import json
from flask import Flask, render_template

app = Flask(__name__)

API_KEY = '9429328f62684df38dd98548f024193b' 
BBC_NEWS_URL = f'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={API_KEY}'

@app.route('/')
def index():
    response = requests.get(BBC_NEWS_URL)
    data = response.json()

    with open('output.json', 'w') as f:
        json.dump(data, f, indent=4)

    articles = data.get('articles', [])
    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
