
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def homepage():
    result = requests.get("http://data.fixer.io/api/latest?access_key=88e986137779229d0ead7334b6a91252")
    data = result.json()
    return render_template('currency.html',exchange=data)

