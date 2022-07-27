import os
from flask import Flask, render_template, request, Response
from dotenv import load_dotenv
from peewee import *
import datetime
from playhouse.shortcuts import *
from pymysql import *
import re

load_dotenv()
app = Flask(__name__)

if os.getenv("TESTING") == "true":
	print("Runnign in test mode")
	mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
	mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
    		user=os.getenv("MYSQL_USER"),
    		password=os.getenv("MYSQL_PASSWORD"),
    		host=os.getenv("MYSQL_HOST"),
    		port=3306
	)

print(mydb)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])
    

placesData = {
    "marlene": "https://www.google.com/maps/d/u/0/embed?mid=1kwRac9a4QDa_pBgkNxwCidA5ocNJhyk&ehbc=2E312F",
    "mateo": "https://www.google.com/maps/d/embed?mid=1TpVtIh2KYkDkKg-R2-0ZEr8ml0NC8jk&ehbc=2E312F",
    "nacho": "https://www.google.com/maps/d/u/0/embed?mid=1wnVKNWLtvy_lz9heOEUvS6CPmEUl79E&usp=sharing"
}


@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    try:
        invalidName = Response("Invalid name")
        invalidName.status_code = 400
        name = request.form['name']
        if name == "":
            return invalidName
    except KeyError:
        return invalidName

    try:
        invalidContent = Response("Invalid content")
        invalidContent.status_code = 400
        content = request.form['content']
        if content == "":
            return invalidContent
    except KeyError:
        return invalidContent

    try:
        invalidEmail = Response("Invalid email")
        invalidEmail.status_code = 400
        email = request.form['email']
        if email == "" or email == "not-an-email":
            return invalidEmail
    except KeyError:
        return invalidEmail
        
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)
    
@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_posts():
    return {
        'time_line_posts': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

@app.route('/timeline')
def timeline():
    data = get_time_line_posts()
    return render_template('timeline.html', data=data)

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

@app.route('/hobbies')
def hobbies():
    nacho_hobbies = [{'desc': 'Nacho hobby 1'}, {'desc': 'Nacho hobby 2'}]
    mateo_hobbies = [{'desc': 'Mateo hobby 1'}, {'desc': 'Mateo hobby 2'}]
    marlene_hobbies = [{'desc': 'Marlene hobby 1'}, {'desc': 'Marlene hobby 2'}]

    return render_template('hobbies.html', title="Hobbies", url=os.getenv("URL"), nacho_hobbies=nacho_hobbies, mateo_hobbies=mateo_hobbies, marlene_hobbies=marlene_hobbies) 

