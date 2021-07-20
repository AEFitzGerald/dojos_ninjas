from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/dojos')
def home():
    dojos = Dojo.get_all_dojos()
    return render_template('dojos.html', dojos = dojos)

@app.route('/ninjas')
def ninja_form():
    dojos = Dojo.get_all_dojos()
    return render_template('ninjas.html', dojos = dojos)
    
@app.route('/dojo_create', methods= ['POST'])
def dojo_create():
    Dojo.create_dojo(request.form)
    return redirect(f"/show_dojo/{request.form['dojo_id']}")

@app.route('/show_dojo/<int:dojo_id>')
def display_one_dojo(dojo_id):
    data = {
        'id' : dojo_id
    }
    dojo = Dojo.get_dojo_by_id(data)
    return render_template('show_dojo.html', dojo = dojo)

@app.route('/ninja_create', methods= ['POST'])
def ninja_create():
    Ninja.create_ninja(request.form)
    return redirect(f"/show_dojo/{request.form['dojo_id']}")

