import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/hobbies')
def hobbies():
    nacho_hobbies = [{'desc': 'Nacho hobby 1'}, {'desc': 'Nacho hobby 2'}]
    mateo_hobbies = [{'desc': 'Mateo hobby 1'}, {'desc': 'Mateo hobby 2'}]
    marlene_hobbies = [{'desc': 'Marlene hobby 1'}, {'desc': 'Marlene hobby 2'}]

    return render_template('hobbies.html', title="Hobbies", url=os.getenv("URL"), nacho_hobbies=nacho_hobbies, mateo_hobbies=mateo_hobbies, marlene_hobbies=marlene_hobbies)