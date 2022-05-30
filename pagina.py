import re 

import sqlite3

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')

def home():

    return render_template ('home.html')


@app.route('/inicio')

def inicio():

    return render_template ('inicio.html')


if __name__  ==  '__main__' : 
     app.run(debug=True)

