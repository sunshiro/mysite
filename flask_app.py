
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def homepage():
    result = requests.get("https://hello.ddc.moph.go.th")
    data = result.json()
    app.logger.info(data)
    return render_template('covid.html',covid_stat=data[0])

