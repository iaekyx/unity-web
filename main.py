import sqlite3
from app import app
import db_config as db
from flask import Flask
from datetime import datetime
from flask import flash, render_template, jsonify, redirect, url_for, request
from flask_bootstrap import Bootstrap4
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from gevent import pywsgi
from db_config import query, exec_, commit_
from datetime import datetime, time, timedelta
import calendar

app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////database.db'

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.i18n')

username = ''
password = ''
stuname = ''


@app.route('/', methods=['GET', 'POST'])
@app.route('/uploads.html', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        try:
            if request.values.get("upload") == "pic1":
                file = request.files["pic1"]
            elif request.values.get("upload") == "pic2":
                file = request.files["pic2"]
            elif request.values.get("upload") == "pic3":
                file = request.files["pic3"]

            if file.filename == '':
                return '<script> alert("Error: No file selected.");</script>'+ render_template('uploads.html')

            target_dir = "./static/"
            file.save(target_dir + file.filename)

            return '<script> alert("File uploaded successfully.");</script>' + render_template('uploads.html')
        except KeyError:
            return '<script> alert("Error: No file uploaded.");</script>' + render_template('uploads.html')
    else:
        return render_template('uploads.html')

if __name__ == '__main__':
    # server = pywsgi.WSGIServer(('127.0.0.1', 5000), app)
    # server.serve_forever()
    app.run(host='127.0.0.1', port=5000, debug=True)
