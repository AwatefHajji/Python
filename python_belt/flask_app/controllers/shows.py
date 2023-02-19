from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models import show_model
from flask_app.models import user_model
#!=============Display new_show Page to add show ==============
@app.route('/shows/new')
def new_show():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('new_show.html')
#!==============Action Route for add show=================
@app.route('/shows/create', methods=['POST'])
def add_show():
    if 'user_id' not in session:
        return redirect('/')
    if not show_model.Show.validate_show(request.form):
        return redirect('/shows/new')
    data = {
        **request.form,
        'user_id': session['user_id']
    }
    print("-"*20, data, "-"*20)
    show_model.Show.create_show(data)
    return redirect('/dashboard')
#!=============Display edit_show Page to update show ==============
@app.route('/shows/edit/<int:show_id>')
def edit(show_id):
    if 'user_id' not in session:#to secure
        return redirect('/')
    show = show_model.Show.get_by_id({'id':show_id})
    return render_template('edit_show.html',show=show)
#!==============Action Route for update=================
@app.route('/shows/update',methods=['POST'])
def update():
    if 'user_id' not in session:#to secure
        return redirect('/')

    if not show_model.Show.validate_show(request.form):# check if show existing
        id=request.form['id']
        return redirect(f"/shows/edit/{id}")
    show_model.Show.update(request.form)
    return redirect('/dashboard')
#!=============Display show Page to show show ==============
@app.route('/shows/<int:show_id>')
def show_show(show_id):
    if 'user_id' not in session:
        return redirect('/')
    
    show = show_model.Show.get_by_id({'id':show_id})
    logged_user=user_model.User.get_by_id({'id':session['user_id' ]})
    
    return render_template('show_show.html', show=show, logged_user=logged_user)

#!==============Action Route for delete=================
@app.route('/shows/delete/<int:show_id>')
def delete_show(show_id):
    if 'user_id' not in session:
        return redirect('/')
    show_model.Show.delete({'id':show_id})
    return redirect('/dashboard')
