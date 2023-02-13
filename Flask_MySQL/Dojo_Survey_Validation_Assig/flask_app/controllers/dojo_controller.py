from flask_app import app
from flask_app.models.dojo_model import Dojo
from flask import render_template, redirect, request, session, flash
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/result',methods=['POST'])
def info():
    # print(request.form)
    # session['name'] = request.form['name']
    # session['location'] = request.form['location']
    # session['lang'] = request.form['lang']
    # session['comment'] = request.form['comment']
    #!validation
    if not Dojo.validate_reg(request.form):
        return redirect("/")

    return render_template('result.html')