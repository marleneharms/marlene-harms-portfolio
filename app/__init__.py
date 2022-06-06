import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


placesData = {
    "marlene": "https://www.google.com/maps/d/u/0/embed?mid=1kwRac9a4QDa_pBgkNxwCidA5ocNJhyk&ehbc=2E312F",
    "mateo": "https://www.google.com/maps/d/embed?mid=1TpVtIh2KYkDkKg-R2-0ZEr8ml0NC8jk&ehbc=2E312F",
    "nacho": "https://www.google.com/maps/d/u/0/embed?mid=1wnVKNWLtvy_lz9heOEUvS6CPmEUl79E&usp=sharing"
}


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/hobbies')
def hobbies():
    nacho_hobbies = [{'desc': 'Nacho hobby 1'}, {'desc': 'Nacho hobby 2'}]
    mateo_hobbies = [{'desc': 'Mateo hobby 1'}, {'desc': 'Mateo hobby 2'}]
    marlene_hobbies = [{'desc': 'Marlene hobby 1'}, {'desc': 'Marlene hobby 2'}]

    return render_template('hobbies.html', title="Hobbies", url=os.getenv("URL"), nacho_hobbies=nacho_hobbies, mateo_hobbies=mateo_hobbies, marlene_hobbies=marlene_hobbies)