from flask import Flask, render_template,session,redirect
app = Flask(__name__)
app.secret_key="he was heer."
@app.route('/')          
def counter():
    if "num" not in session:
        session['num'] =1
    else:
        session['num']+=1
    return render_template("counter.html") 

@app.route('/destroy_session')          
def delete():
    session.clear()
    return redirect('/')
@app.route('/reset_btn', methods=['POST'])          
def reset():
    return redirect('/destroy_session')
@app.route('/add_btn', methods=['POST'])          
def add():
    print(session)
    session['num'] += 1
    print(session)
    return redirect('/')
    
if __name__=="__main__":      
    app.run(debug=True)    

