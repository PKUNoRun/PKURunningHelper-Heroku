#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# filename: runner.py

import time
from flask import Flask, request, Response

from util import Logger

import json

logger = Logger("runner")

from PKURunner import PKURunnerClient as Client

app = Flask("PKURunningHelper-Heroku")

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

@app.route("/index.html", methods=["GET"])
def index():
    return "welcome", 200