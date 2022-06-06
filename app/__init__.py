import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


placesData = {
    "marlene": "https://www.google.com/maps/d/u/0/embed?mid=1kwRac9a4QDa_pBgkNxwCidA5ocNJhyk&ehbc=2E312F",
    "mateo": "https://www.google.com/maps/d/embed?mid=1TpVtIh2KYkDkKg-R2-0ZEr8ml0NC8jk&ehbc=2E312F",
    "nacho": ""
}


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/places')
def places():
    return render_template('places.html', maps=placesData)


@app.route('/experience')
def experience():
    return render_template('experience.html')
