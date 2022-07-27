from calendar import c
import unittest
from peewee import *

from app import TimelinePost, get_time_line_posts

MODELS = [TimelinePost]

test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):

        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()

    def test_timeline_post(self):

        #Make first post
        first_post = TimelinePost.create(name='John Doe', email='john@example.com', content='Hello world, I\'m John!')
        assert first_post.id == 1

        #Make second post
        second_post = TimelinePost.create(name='Jane Doe', email='jane@example.com', content='Hello world, I\'m Jane!')
        assert second_post.id == 2

        #Store posts in list 
        created_post_list = [first_post, second_post]

        #Retrieve posts from DB using imported function from initial python script 
        fetched_posts = get_time_line_posts()['time_line_posts']
        array_fetched = []

        #Adds the retrieved posts into new array ordered normally, as the DB flips the index order
        for i in range((len(fetched_posts)-1), -1, -1):
            array_fetched.append(fetched_posts[i])


        #Will now iterate through all of the created posts and compare them to the content added in the DB
        for i in range(len(created_post_list)):

            assert created_post_list[i].name == array_fetched[i]['name']
            assert created_post_list[i].email == array_fetched[i]['email']
            assert created_post_list[i].content == array_fetched[i]['content']
            assert created_post_list[i].created_at == array_fetched[i]['created_at']
