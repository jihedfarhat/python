from flask_app import app
from flask import render_template, redirect, request 
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/dojos')
def dojos_page():
    dojos = Dojo.get_dojos()
    return render_template("dojos.html", dojos = dojos)

@app.route('/add_dojo' , methods=['post'])
def create_dojo():
    dojo_data = request.form
    Dojo.create_dojo(dojo_data)
    return redirect('/dojos')

@app.route('/dojos/<int:dojo_id>')
def ninjas_page(dojo_id):
    ninjas = Ninja.get_by_dojo_id({'dojo_id': dojo_id})
    dojo = Dojo.get_dojo_by_id({'id': dojo_id})
    return render_template('dojo_show.html' , dojo = dojo , ninjas = ninjas)