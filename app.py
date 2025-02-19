#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# filename: runner.py

from flask import Flask, request, render_template

app = Flask(__name__)

import os, sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from util import Logger
logger = Logger("runner")
import time
from PKURunner import PKURunnerClient as Client
@app.route("/api", methods=["POST"])
def main():
    resp = {}
    success = False
    code = 200
    try:
        timestamp = time.time()
        if "timestamp" in request.form:
            if len(request.form["timestamp"]) > 0:
                timestamp=float(request.form["timestamp"])
        client = Client(StudentID=request.form["StudentID"], Password=request.form["Password"])
        success, resp = client.run(distance=request.form["distance"], pace=request.form["pace"], stride_frequncy=request.form["stride_frequncy"], timestamp=timestamp)
    except Exception as err:
        logger.error("upload record failed !")
        resp = {"msg": err}
        code = 418
    else:
        logger.info("upload record success !")
    return resp, code

@app.route("/")
def homepage():
    return render_template('index.html'), 200

if __name__ == "__main__":
    app.run(debug=True)
