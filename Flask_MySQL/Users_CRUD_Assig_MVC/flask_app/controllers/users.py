from flask_app import app
from flask import Flask,render_template,redirect,request,session
from flask_app.models.users import User
@app.route('/')
def users():
    return redirect('/users')
@app.route('/users')
def hello():
    users=User.get_all_from_DB()
    return render_template('read_user.html',users=users)
#displaye form for add user
# ============ Display Route ============
@app.route("/users/new")
def show_form():
    return render_template("create_user.html")
# remplir formulaire et l'envoyer
# ============ Action Route ============
@app.route('/create',methods=['POST'])
def create():
    
    #!whene we just used the session to save the users created by the utilisateur
    # print(request.form)
    # session['first_name']=request.form['first_name']
    # session['last_name']=request.form['last_name']
    # session['email']=request.form['email']
    # print(session)
    #!whene we want to save the form in the DB
    #? First we make a data dictionary from our request.form coming from our template.
    #? The keys in data need to line up exactly with the variables in our query string.

     data={
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"]}
     print(f"!!!!!!!!!!!!!! {type(data['first_name'])}")
     User.save(data=data)
     return redirect('/users')

# ********read one user**********

@app.route('/users/<int:id_user_show>/show')
def read_user(id_user_show):
    
    data={'id':id_user_show }
    user_show=User.get_one_from_DB(data)
   
    return render_template("read_one_user.html",user_show=user_show)
# ********Edit one user**********
# !show the form where we do the modification
@app.route('/users/<int:id_user_edit>/edit')
def show_form_edit(id_user_edit):
    data={'id':id_user_edit}
    user_edit=User.get_one_from_DB(data)
    return render_template("edit.html",user_edit=user_edit)
# *********action route after edit the user
@app.route('/edit',methods=['POST'])
def edit_user():
    
    data={
         "id": request.form["id"],
       "first_name":request.form["first_name"],
       "last_name":request.form["last_name"],
       "email":request.form["email"]
       }
    User.Edit_one_user(data=data)
    return redirect('/users')
# ***************delete user**************
@app.route('/users/<int:id_user_delete>/delete')
def delete_user(id_user_delete):
    data={'id':id_user_delete}
    User.delete(data)
    return redirect('/users')
