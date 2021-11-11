
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    result = requests.get("https://hello.ddc.moph.go.th")
    data = result.json()
    return render_template('index.html',covid_stat=data[0])

