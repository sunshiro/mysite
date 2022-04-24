
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request, session
import requests
from datetime import date

app = Flask(__name__)
app.url_map.strict_slashes = False
app.secret_key = b'dfgsdgvdcrevd4893r34tqyof'

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

@app.route('/stock_form')
def stock_form():
    return render_template('stock_form.html')

@app.route('/stock_show', methods = ['GET'])
def stock_show():
    symbol = request.args.get('symbol')
    result = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+symbol+'&apikey=MYOJM36ZUW7R9G59')
    jsondata = result.json()
    stock_data = jsondata['Time Series (Daily)']
    return render_template('stock_show.html', stock_symbol=symbol, stock_data=stock_data)

@app.route('/kratai-bin')
def vm_welcome():
    return render_template('vm_welcome.html')

@app.route('/kratai-bin/order')
def vm_order():
    return render_template('vm_order.html')

@app.route('/kratai-bin/confirm', methods = ['GET'])
def vm_confirm():
    session['numTumThai'] = int(request.args.get('txt_tum_thai'))
    session['numTumPoo'] = int(request.args.get('txt_tum_poo'))
    session['totalTumThai'] = '{0:.2f}'.format(100.0*session['numTumThai'])
    session['totalTumPoo'] = '{0:.2f}'.format(120.0*session['numTumPoo'])
    session['grandTotal'] = '{0:.2f}'.format(100.0*session['numTumThai']+120.0*session['numTumPoo'])
    return render_template('vm_confirm.html', numTumThai=session['numTumThai'], numTumPoo=session['numTumPoo'], totalTumThai=session['totalTumThai'], totalTumPoo=session['totalTumPoo'], grandTotal=session['grandTotal'])

@app.route('/kratai-bin/pay', methods = ['GET'])
def vm_pay():
    return render_template('vm_pay.html', grandTotal=session['grandTotal'])

@app.route('/kratai-bin/check_payment', methods = ['GET'])
def vm_check_payment():
    creditCardNum = request.args.get('txt_credit_card_num')
    nameOnCard = request.args.get('txt_name_on_card')
    if (len(creditCardNum) > 0) and (len(nameOnCard) > 0):
        return render_template('vm_collect.html', numTumThai=session['numTumThai'], numTumPoo=session['numTumPoo'])
    else:
        return render_template('vm_pay.html', grandTotal=session['grandTotal'], paymentError=True)

@app.route('/kratai-bin/check_collect', methods = ['GET'])
def vm_check_collect():
    numTumThaiRemain = int(request.args.get('numTumThaiRemain'))
    numTumPooRemain = int(request.args.get('numTumPooRemain'))
    if (numTumThaiRemain == 0) and (numTumPooRemain == 0):
        return render_template('vm_welcome.html')
    else:
        return render_template('vm_clear.html')