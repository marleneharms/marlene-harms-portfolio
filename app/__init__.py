import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

indexData = {
    "img": "img/mateo.jpeg",
    "name": "Mateo Marinez",
    "intro": "Computer Science Student @ The University of Texas Rio Grande Valley"
}

placesData = {
    "map": "https://www.google.com/maps/d/embed?mid=1TpVtIh2KYkDkKg-R2-0ZEr8ml0NC8jk&ehbc=2E312F",
}


@app.route('/')
def index():
    return render_template('index.html', indexData=indexData)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html',)

@app.route('/places')
def places():
    return render_template('places.html', placesData=placesData)

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

 

