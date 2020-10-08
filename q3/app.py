#app.py

from flask import Flask, render_template, request
import csv
import json

from datetime import datetime

app = Flask(__name__)

import repo


#upload csv file
@app.route("/")
def index():
    return render_template("upload.html")

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    
    file = request.files['csvfile'] #variable for uploded file
    
    #fstring = file.read()

    cfile = open(file, newline='')
    reader =csv.reader(cfile)

    data = []
    for row in reader:
        name = str(row[0])
        date = datetime.strptime(row[1], '%YYYY-%m-%dTHH:MM:ZZ')
        temp = int(row[2])

        data.append(name, date, temp)
        repo.create_trolley(name, date, temp)

    return render_template("upload.html")


    #input_file = csv.DictReader(open(file))
    #for row in input_file:
    #    name = row[0]
     #   date = row[1]
      #  temp = row[2]

       # repo.create_trolley(name, date, temp)

        #return("Updated to DB")
    #return file#showed that upload handled properly
    

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

@app.route("/trolley/record", methods=['POST','GET'])
def trolley_create():
    if (request.method == 'POST'):
        repo.create_trolley(request.form.get('name'), request.form.get('date'), request.form.get('temp'))
        return "Thank you for submitting"
    return render_template("form.html")


@app.route("/trolley")
def trolley_read():
    return render_template("trolley.html", dlist=repo.all_trolley())


@app.route("/dashboard")
def dashboard_view():
    data = repo.f_date()
    return render_template("dashboard.html", total=repo.count_all(), cactive = repo.count_active(), xlabel=data, highestTemp=repo.get_high(), lowestTemp=repo.get_low())

#DateObj = datetime.strptime(date_string, "%Y-%m-%d") to convert into dateobj
#to plug in the data and labels, pull out all the data into a string and plug into the chart


if __name__ == "main":
    app.run(Debug=True)