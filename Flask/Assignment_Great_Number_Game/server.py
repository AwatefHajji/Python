from flask import Flask, render_template,session,redirect,request
import random 
app = Flask(__name__)
app.secret_key="he was heer."
@app.route('/')
def rend():
    session['key']=random.randint(1, 100)
    print(session)
    return render_template('index.html')
@app.route('/gess', methods=['POST'])
def gess1():
    print(session['key'])
    print(request.form['guess'])
    if session['key'] == int(request.form['guess']):
             return redirect('/Bravo')
    elif session['key'] < int(request.form['guess']):
             return redirect('/tooHigh')
    else:
         return redirect('/tooLow')
@app.route('/tooLow')
def gess2():
    return render_template('tooLow.html')
@app.route('/tooHigh')
def gess3():
    return render_template('tooHigh.html')
@app.route('/Bravo')
def gess4():
    return render_template('bravo.html')
@app.route ('/replay', methods=['POST'])
def replay():
    return render_template('index.html')
if __name__=="__main__":
    app.run(debug=True)

