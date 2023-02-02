from flask import Flask
from flask import render_template
app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello World!"

@app.route('/dojo')
def say():
    return "Dojo!"

@app.route('/say/<name>')
def say_hi(name):
    return f"Hi 🤗🥰🙂 {name} !"

@app.route('/repeat/<int:times>/<name>')
def repeat(times,name):
    return {name} * times

@app.errorhandler(404)
def page_not_found(e):

    return render_template('Sorry!'), 404

if __name__=='__main__':
    app.run(debug=True)