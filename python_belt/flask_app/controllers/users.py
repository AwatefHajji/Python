from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models import user_model
from flask_app.models import show_model
from flask_bcrypt import Bcrypt
bcrypt= Bcrypt(app)
#!=============Display Index Page==============
@app.route('/')
def index():
    return render_template("index.html")
#!==============Action Route for registration=================
@app.route('/user/register', methods=['POST'])
def register():
    #!verification de validation and hashed password befor saved in db
    if user_model.User.validate_user(request.form):
        # print("-"*20,request.form ['password'],"-"*20)
        # *create the hash
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        # print("*"*20,hashed_password,"*"*20)
        #?new data after hashing password
        data = {
            **request.form,
            "password": pw_hash,
        }
        user_id = user_model.User.create_user(data)
        print("-"*20,user_id,"-"*20)
        #?saved user id in session for the garde route and...
        session['user_id']= user_id

        return redirect('/dashboard')
    
    return redirect('/')

#!==============Action route for Login with validation (email + password) ======================
@app.route('/user/login',methods=['POST'])
def login():
    user_from_db= user_model.User.get_by_email(request.form)

    if not user_from_db:
        flash("Invalid credentials !", "login")
        return redirect('/')
    if not bcrypt.check_password_hash(user_from_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid credentials !", "login")
        return redirect('/')
    session['user_id']=user_from_db.id
    return redirect('/dashboard')

#!==========display route after registration ===========
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    logged_user = user_model.User.get_by_id({'id':session['user_id']})
    print(f"++++++++++++++++++++++{logged_user}+++++++++++++++++++++++")
    all_shows =show_model.Show.get_all_user_show()
    print(f"++++++++++++++++++++++{all_shows}///////////////////////////////////")
    all_users = user_model.User.get_all()
    
    return render_template("dashboard.html",logged_user=logged_user, all_users=all_users,all_shows=all_shows)
#!===================action route for logout===============
@app.route('/user/logout')
def logout():
    session.clear()
    return redirect('/')