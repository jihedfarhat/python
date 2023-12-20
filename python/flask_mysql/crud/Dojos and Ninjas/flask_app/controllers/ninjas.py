from flask_app import app
from flask import Flask , request, render_template,redirect
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def add_ninjas_page():
    dojos = Dojo.get_dojos()
    return render_template('ninjas.html' , dojos = dojos)

@app.route('/add_ninja' , methods = ['post'])
def create_ninja():
    Ninja.create_ninja(request.form)
    return redirect(f'/dojos/{request.form.get("dojo_id")}')
