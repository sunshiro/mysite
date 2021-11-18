
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request
import requests
from datetime import date

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html', current_date = str(date.today()))