# app.py
from flask import Flask, request, jsonify,send_file, json
from EditConf import EditConf
import subprocess
from calculation import Calculation
import os
import shutil
import logging
from werkzeug.exceptions import HTTPException



app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

"""
@app.errorhandler(HTTPException)
def handle_exception(e):
  
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response
"""
@app.get("/stagecalculation")
def post_calculation():
    newcalculation = Calculation()
    Calculation.calculations[newcalculation.getId()] = newcalculation
    print(Calculation.calculations)
    print(str(newcalculation.getId()))
    d = {"id": str(newcalculation.getId())}
    print(d)
    return jsonify(d)


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
    print("received editconf")
    #print(request.form)
    #print(request.keys)
    #print(request.args)
    #request.__dict__["json_module"]

    #if request.want_form_data_parsed:
    editconfparameters = dict(request.form)
    print("edit conf contains          ")
    print(editconfparameters['json'])
    if "id" in editconfparameters:
        calculation = Calculation.calculations[int(editconfparameters.pop("id"))]
    else:
        calculation = Calculation()
        Calculation.calculations[calculation.getId()] = calculation

    print("we did the if")

    directory = calculation.saveFiles(editconfparameters['file'],json.loads(editconfparameters['json'])['-f'])
    print(directory)
    print(editconfparameters)
    calculation2 = EditConf(json.loads(editconfparameters['json']))
    calculation2.createInputString()
    process = subprocess.Popen(["gmx"] + calculation2.getInputString(),cwd=directory)
    process.wait()

    return send_file(directory + json.loads(editconfparameters['json'])["-o"])

    return {"error": "Request must be JSON"}, 415

