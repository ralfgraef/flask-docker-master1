from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config["UPLOAD_PATH"] = "/app/app/uploads"


@app.route("/")
@app.route("/home")
def index():
    return render_template('index.html')

@app.route("/market")
def market_page():
    items = [
    {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
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
