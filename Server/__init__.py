# app.py
from flask import Flask, Response,request, jsonify,send_file, json
from Server.EditConf import EditConf
from Server.Solvate import Solvate

import subprocess
from .Calculation import Calculation
from .Submission import Submission
import os
import shutil
import logging
import uuid
from .db import get_db
import json

from werkzeug.exceptions import HTTPException


def create_app(test_config=None):

    app = Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    
    logging.basicConfig(level=logging.DEBUG)
    
    db.init_app(app)



    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass



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
        editconfparameters = dict(request.form)

        if "id" in editconfparameters:
            calculation = Calculation.calculations[int(editconfparameters.pop("id"))]
        else:
            calculation = Calculation()
            Calculation.calculations[calculation.getId()] = calculation


        directory = calculation.saveFiles(editconfparameters['file'],json.loads(editconfparameters['json'])['-f'])
        calculation2 = EditConf(json.loads(editconfparameters['json']))
        calculation2.createInputString()
        process = subprocess.Popen(["gmx"] + calculation2.getInputString(),cwd=directory)
        process.wait()

        return send_file(directory + json.loads(editconfparameters['json'])["-o"])

        return {"error": "Request must be JSON"}, 415

    @app.post("/pdb2gmx")
    def do_pdb2gmx():
        pdb2gmx = dict(request.form)

        if "id" in pdb2gmx:
            calculation = Calculation.calculations[int(pdb2gmx.pop("id"))]
        else:
            calculation = Calculation()
            Calculation.calculations[calculation.getId()] = calculation

        directory = calculation.saveFiles(pdb2gmx['file'],json.loads(pdb2gmx['json'])['-f'])
        calculation2 = EditConf(json.loads(pdb2gmx['json']))
        calculation2.createInputString()
        process = subprocess.Popen(["gmx"] + calculation2.getInputString(),cwd=directory)
        process.wait()

        return send_file(directory + json.loads(pdb2gmx['json'])["-o"])

        return {"error": "Request must be JSON"}, 415


    @app.get("/register")
    def get_register():

        username = uuid.uuid4().hex
        database= get_db()
        error = None
        if not username:
            error = 'Username is required.'

        if error is None:
            try:
                database.execute(
                    "INSERT INTO user (username) VALUES (?)",
                    ([str(username)]),
                )
                database.commit()
            except database.IntegrityError:
                error = f"User {username} is already registered."
            else:
                resp = Response(response="", status=200,  mimetype="text/plain")
                resp.headers['Qchemserv-Status'] = "OK"
                resp.headers['Qchemserv-Cookie'] = username

                return resp

            flash(error)

        return {"error": error}, 415


    @app.route("/submit", methods=('GET','POST'))
    def submit():
        if request.method == 'POST':
            username = request.args.get('cookie')
            print(username)
            if username != None:
                database = get_db()
                user = database.execute(
                    'SELECT * FROM user WHERE username = ?', (username,)
                ).fetchone()
                print(user)
                if user is None:
                    error = 'Incorrect username.'
                else:

                    parameters = dict(request.form)
                    print(request)
                    print(parameters)
                    print("it works though")
                    submission = Submission(json.loads(parameters['json']))
                    Calculation.calculations[submission.getCalculation().getId()] = submission.getCalculation()
                    directory = calculation.saveFiles(parameters['file'],json.loads(parameters['json'])['-f'])
                    submission.getGromacsCommand().createInputString()
                    process = subprocess.Popen(["gmx"] + submission.getGromacsCommand().getInputString(),cwd=directory)
                    
                    resp = Response(response="", status=200,  mimetype="text/plain")
                    resp.headers['Qchemserv-Status'] = "OK"
                    resp.headers['Qchemserv-Jobid'] = username

                    return resp

                    submission.getCalculation().getId()



            else:
                error = "No username supplied"

        return {"error": error}, 415






    @app.post("/solvate")
    def do_solvate():
        print("received solvate")
        #print(request.form)
        #print(request.keys)
        #print(request.args)
        #request.__dict__["json_module"]

        #if request.want_form_data_parsed:
        solvate = dict(request.form)
        #print("solvate contains          ")
        #print(solvate)
        #print(solvate['json'])
        if "id" in solvate:
            calculation = Calculation.calculations[int(solvate.pop("id"))]
        else:
            calculation = Calculation()
            Calculation.calculations[calculation.getId()] = calculation

        print("we did the if")

        directory = calculation.saveFiles(solvate['file'],json.loads(solvate['json'])['-cp'])
        directory = calculation.saveFiles(solvate['top'],json.loads(solvate['json'])['topology'])
        calculation2 = Solvate(json.loads(solvate['json']))
        calculation2.createInputString()
        process = subprocess.Popen(["gmx"] + calculation2.getInputString(),cwd=directory)
        process.wait()

        return send_file(directory + json.loads(solvate['json'])["-o"])

        return {"error": "Request must be JSON"}, 415


    return app

