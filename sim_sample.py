from flask import Flask, render_template, request, flash, redirect, url_for, session
from wtforms import Form, StringField, TextAreaField, RadioField, SelectField, validators, PasswordField


app = Flask(__name__)


#simcien
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')


@app.route('/nov')
def nov():
    return render_template('fliter_nov.html')

@app.route('/dbs')
def dbs():
    return render_template('fliter_dbs.html')

@app.route('/credit_summary')
def credit_summary():
    return render_template('credit_summary.html')

@app.route('/debit_summary')
def debit_summary():
    return render_template('debit_summary.html')




if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run()
