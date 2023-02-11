from flask import Flask,render_template,request,redirect 
from users import User             
app = Flask(__name__)   
@app.route('/')
def users():
    return redirect('/users')
@app.route('/users')
def display():
    users=User.get_all()
    return render_template("readAll.html",users=users)

@app.route('/users/show')
def display_one():
    users=User.get_one()
    return render_template("read_one.html",users=users)
# ============ Display Route ============
@app.route("/users/new")
def show_form():
    return render_template("create.html")
# ============ action Route ============
@app.route('/creat',methods=['POST'])
def create_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
         "email": request.form["email"]
            }
    users = User.save(data)
    return redirect('/users')







 
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

