from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('static/img', path)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)


@app.route('/bootstrap-4.3.1-dist/<path:path>')
def send_bs(path):
    return send_from_directory('static/bootstrap-4.3.1-dist', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)