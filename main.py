from flask import Flask
from flask import render_template
import requests
import json


app = Flask(__name__)

## function
@app.route('/')
def joke():
    joke = requests.get('https://official-joke-api.appspot.com/random_joke').json()
    setup = joke['setup']
    punchline = joke['punchline']
    return render_template('index.html', setup=setup, punchline=punchline)


if __name__ == "__main__":
    app.run()
