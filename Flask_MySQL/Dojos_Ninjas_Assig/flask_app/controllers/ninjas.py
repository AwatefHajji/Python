from flask_app import app
from flask import Flask,render_template,redirect,request,session
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo
#displaye form for add ninja
# ============ Display Route ============
@app.route("/ninjas")
def show_form():
    all_dojos=Dojo.get_all_from_DB()
    return render_template("new_ninja.html",all_dojos=all_dojos)
# ============ Action Route ============
@app.route('/add_ninja',methods=['POST'])
def create_ninja():
    Ninja.add_new_ninja(request.form)

    return redirect("/dojos")

#!displaye form for EDIT ninja
# !============ Display Route ===========
@app.route("/edit/<int:id_ninja>")
def show_form_edit(id_ninja):
    data={'id':id_ninja}
    this_ninja=Ninja.get_one_ninja(data)
    return render_template("edit_ninja.html",this_ninja=this_ninja)
# *********action route after edit the ninja
@app.route('/edit_ninja',methods=['POST'])
def edit_user():
    data={
         "id": request.form["id"],
       "first_name":request.form["first_name"],
       "last_name":request.form["last_name"],
       "age":request.form["age"]
       }
    Ninja.edit_ninja(data=data)
    return redirect('/dojos')


    
