#app.py

from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

import repo

@app.route("/trolley/delete", methods=['POST','GET'])
def trolley_delete():
    if (request.method == 'POST'):
        repo.delete_trolley(request.form.get('name'))
        return "Thank you for submitting"
    return render_template("form.html")

@app.route("/trolley/update", methods=['POST','GET'])
def update_trolley():
    if (request.method == 'POST'):
        repo.update_trolley(request.form.get('name'), request.form.get('temp'))
        return "Thank you for submitting"
    return render_template("form.html")

@app.route("/trolley/create", methods=['POST','GET'])
def trolley_create():
    if (request.method == 'POST'):
        repo.create_trolley(request.form.get('name'), request.form.get('date'),
        request.form.get('time'), request.form.get('temp'))
        return "Thank you for submitting"
    return render_template("form.html")


@app.route("/trolley")
def trolley_read():
    return render_template("trolley.html", dlist=repo.f_date(), tlist=repo.get_high())

@app.route("/temp")
def temp_view():
    return render_template("temp.html")

@app.route("/dashboard")
def dashboard_view():
    return render_template("dashboard.html", total=repo.count_all(), cactive = repo.count_active(), xlabel=repo.f_date(), highestTemp=repo.get_high(), lowestTemp=repo.get_low())

#DateObj = datetime.strptime(date_string, "%Y-%m-%d") to convert into dateobj
#to plug in the data and labels, pull out all the data into a string and plug into the chart


if __name__ == "main":
    app.run()