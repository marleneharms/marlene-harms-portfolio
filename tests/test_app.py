from cmath import sin
from http import server
import unittest
import os

os.environ["TESTING"] = "true"

from app import app, post_time_line_post, timeline

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get('/')
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Document</title>" in html

        # TO DO Add more tests relating to the home page
        assert "<h5 class=\"card-title\">Nacho's Hobbies</h5>" in html
        assert "<h5 class=\"card-title\">Marlene's Hobbies</h5>" in html
        assert "<h5 class=\"card-title\">Mateo's Hobbies</h5>" in html


    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "time_line_posts" in json
        assert len(json["time_line_posts"]) == 0

        #TO DO Add more tests relating to the /api/timeline_post
        one_post = [{"name": "John Doe", "email": "john@example.com", "content": "Hello World, from John!"}]
        singleResponse = []
        
        #Checks that what is posted matches all the information that is meant to be posted
        
        singleResponse.append(self.client.post("/api/timeline_post", data=one_post[0]))
        singleResponse[0] = singleResponse[0].get_json()
        assert one_post[0]["name"] == singleResponse[0]["name"]
        assert one_post[0]['email'] == singleResponse[0]['email']
        assert one_post[0]['content'] == singleResponse[0]['content']

        #Checks whether retrieved information matches posted information
        serverResponse = self.client.get("/api/timeline_post")
        serverResponse = serverResponse.get_json()
        responseList = serverResponse["time_line_posts"]
        
        assert one_post[0]['name'] == responseList[0]['name']
        assert one_post[0]['email'] == responseList[0]['email']
        assert one_post[0]['content'] == responseList[0]['content']


        #TO DO Add more tests relating to the /timeline page
        response = self.client.get("/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<h1>Timeline</h1>" in html
        assert "<label>Content</label>" in html
        assert "<label>Email</label>" in html
        assert "<label>Name</label>" in html
        

    def test_malformed_timeline_post(self):
        #Post request missing name
        response = self.client.post("/api/timeline_post", data={"email": "john@example.com", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        #Post request with empty content
        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "john@example.com", "content": ""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        #Post request with malformed email
        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "not-an-email", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html
        print("Tests Ran Successfully - Maurice K.")






