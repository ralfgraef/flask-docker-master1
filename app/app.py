from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(length = 30), nullable = False, unique = True)
    price = db.Column(db.Integer(), nullable = False)
    barcode = db.Column(db.String(length = 12), nullable = False, unique = True)
    description = db.Column(db.String(length = 1024), nullable = False, unique = True)

app.config["UPLOAD_PATH"] = "/app/app/uploads"

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///market.db'

@app.route("/")
@app.route("/home")
def index():
    return render_template('index.html')

@app.route("/market")
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

@app.route("/upload", methods = ['GET', 'POST'])
def upload():
    if request.method =='POST':
        f = request.files ['file_name']
        f.save(os.path.join(app.config["UPLOAD_PATH"], f.filename))
        return render_template('upload.html', msg = "File has been uploaded!!!")
    return render_template('upload.html', msg = "Please choose a file!")

if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0")
