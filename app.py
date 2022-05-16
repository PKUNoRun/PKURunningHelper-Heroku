#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# filename: runner.py

from flask import Flask, request, Response

app = Flask(__name__)

from .util import Logger
logger = Logger("runner")
import time
from .PKURunner import PKURunnerClient as Client
@app.route("/api", methods=["POST"])
def main():
    resp = {}
    success = False
    code = 200
    try:
        timestamp = time.time()
        if "timestamp" in request.form:
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
    return "welcome", 200

if __name__ == "__main__":
    app.run(debug=False)
