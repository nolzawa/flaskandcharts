#app.py

from flask import Flask, render_template, request
import json
from datetime import datetime

app = Flask(__name__)

import repo

@app.route("/trolley/<strdate>")
def test_date(strdate):
    #convert to dt obj
    dd = datetime.strptime(strdate, '%Y-%m-%d')
    print(type(dd))
    print(type(strdate))
    print(dd.year)
    print(dd.month)
    print(dd.day)
    return render_template("trolley.html", dlist=repo.f_date(dd))

@app.route("/trolley/delete", methods=['POST','GET'])
def trolley_delete():
    if (request.method == 'POST'):
        repo.delete_trolley(request.form.get('name'))
        return "Thank you for submitting"
    return render_template("form.html")

@app.route("/trolley/update", methods=['POST','GET'])
def update_trolley():
    if (request.method == 'POST'):
        repo.update_trolley(request.form.get('name'), request.form.get('date'))
        return "Thank you for updating"
    return render_template("update.html")

@app.route("/trolley/create", methods=['POST','GET'])
def trolley_create():
    if (request.method == 'POST'):
        repo.create_trolley(request.form.get('name'), request.form.get('date'), request.form.get('temp'))
        return "Thank you for submitting"
    return render_template("form.html")


@app.route("/trolley")
def trolley_read():
    return render_template("trolley.html", dlist=repo.f_date())

@app.route("/temp")
def temp_view():
    return render_template("temp.html")

@app.route("/dashboard")
def dashboard_view():
    t1_list = []
    t2_list = []

    dd = datetime.strptime('2020-08-11', '%Y-%m-%d')
    for i in repo.f_date():
        if i['name'] == 'trolley1':
            t1_list.append(i['temp'])
        if i['name'] == 'trolley2':
            t2_list.append(i['temp'])



    #print(t1_list)
    #print(t2_list)


    return render_template("dashboard.html", t1=t1_list, t2=t2_list, total=repo.count_all(), cactive = repo.count_active(), xlabel=repo.f_date(dd), highestTemp=repo.get_high(), lowestTemp=repo.get_low())

#DateObj = datetime.strptime(date_string, "%Y-%m-%d") to convert into dateobj
#to plug in the data and labels, pull out all the data into a string and plug into the chart


if __name__ == "main":
    app.run()
