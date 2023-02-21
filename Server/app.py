# app.py
from flask import Flask, request, jsonify,send_file
from EditConf import EditConf
import subprocess
from calculation import Calculation
import os
import shutil

app = Flask(__name__)


@app.post("/stagecalculation")
def post_calculation():
    newcalculation = Calculation()
    Calculation.calculations[newcalculation.getId()] = newcalculation
    print(Calculation.calculations)
    return str(newcalculation.getId())


@app.post("/finishcalculation")
def remove_calculation():
    print("request contains =   " + request.json["id"])
    oldCalculation= Calculation.calculations[int(request.json["id"])]
    shutil.rmtree(oldCalculation.getDirectory())
    return "done", 200


@app.get("/editconf")
def get_countries():
    return jsonify(editconf)

@app.post("/editconf")
def do_editconf():

    if request.want_form_data_parsed:
        editconfparameters = dict(request.form)
        calculation = Calculation.calculations[int(editconfparameters.pop("id"))]
        directory = calculation.saveFiles(request.files['file'])
        print(editconfparameters)
        calculation2 = EditConf(editconfparameters)
        calculation2.createInputString()
        process = subprocess.Popen(["gmx"] + calculation2.getInputString(),cwd=directory)
        process.wait()

        return send_file(directory + editconfparameters["-o"]) 

    return {"error": "Request must be JSON"}, 415

