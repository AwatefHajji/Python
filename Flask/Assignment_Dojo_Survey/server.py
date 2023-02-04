from flask import Flask,render_template,request,session
app=Flask(__name__)
app.secret_key = 'Info!!!'
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/result',methods=['POST'])
def info():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['lang'] = request.form['lang']
    session['comment'] = request.form['comment']
    print(session)
    return render_template('result.html')
if(__name__=='__main__'):
    app.run(debug=True)