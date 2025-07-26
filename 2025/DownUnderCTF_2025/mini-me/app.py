from flask import Flask, render_template, send_from_directory, request, redirect, make_response
from dotenv import load_dotenv

import os
load_dotenv()
API_SECRET_KEY = os.getenv("API_SECRET_KEY")
FLAG = os.getenv("FLAG")

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.after_request
def add_header(response):
    response.cache_control.no_store = True
    response.cache_control.must_revalidate = True
    return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    return redirect("/confidential.html")

@app.route("/confidential.html")
def confidential():
    return render_template("confidential.html")


@app.route("/admin/flag", methods=["POST"])
def flag():
    key = request.headers.get("X-API-Key")
    if key == API_SECRET_KEY:
        return FLAG
    return "Unauthorized", 403
