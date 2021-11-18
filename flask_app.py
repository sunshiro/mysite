
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request
import requests
from datetime import date

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html',current_date=str(date.today()))

@app.route('/currency')
def currency_form():
    return render_template('form.html')

@app.route('/result', methods = ['GET'])
def currency_result():
    result = requests.get("http://data.fixer.io/api/latest?access_key=88e986137779229d0ead7334b6a91252")
    jsondata = result.json()
    eur_thb = jsondata['rates']['THB']
    eur = request.args.get('amount')
    thb = float(eur)*float(eur_thb)
    return render_template('result.html',amount_eur=eur,amount_thb=thb)

@app.route('/show_stock', methods = ['GET'])
def show_stock():
    symbol = request.args.get('symbol')
    result = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+symbol+'&apikey=MYOJM36ZUW7R9G59')
    jsondata = result.json()
    timeseries = jsondata['Time Series (Daily)']
    s = ''
    for d in timeseries:
        s += d+', '
        s += timeseries[d]['1. open']+', '
        s += timeseries[d]['2. high']+', '
        s += timeseries[d]['3. low']+', '
        s += timeseries[d]['4. close']+', '
        s += timeseries[d]['5. volume']+'<br>'

    return render_template('show_stock.html',stock_symbol=symbol,stock_table=s)