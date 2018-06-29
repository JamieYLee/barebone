#need to import the app variable itself
from app import app
from flask import render_template # needed to render html files

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')
