from flask_app import app
from flask import Flask,render_template,redirect,request,session
from flask_app.models.dojo import Dojo
@app.route('/')
def dojos():
    return redirect('/dojos')

@app.route('/dojos')
def display():
    all_dojos=Dojo.get_all_from_DB()
    return render_template('dojos.html',all_dojos=all_dojos)

@app.route('/new_dojo',methods=['POST'])
def create():
    data={
        "name" : request.form["name"]
    }
    Dojo.add_new_dojo(data)
    return redirect("/dojos")
# show dojo with ninjas
@app.route("/dojo/<int:id_dojo>")
def show_ninjas_dojo(id_dojo):
    data={"id":id_dojo}
    this_dojo_ninjas = Dojo.get_all_dojo_s_ninja(data)
    print(this_dojo_ninjas)
    return render_template("dojo_show.html",this_dojo_ninjas=this_dojo_ninjas)


