from flask import Flask, send_file, jsonify
from os import listdir

app = Flask(__name__)

@app.route('/')
def index():
    return "GET @ /images/<filename>"

@app.route('/images/<image>')
def send_image(image):
    if image in listdir('static/images'):
        return send_file('static/images/{}'.format(image), mimetype='image/png')
    return jsonify("Sorry, not found"), 404
