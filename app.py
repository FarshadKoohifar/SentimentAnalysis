from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("layout.html")

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('static/img', path)