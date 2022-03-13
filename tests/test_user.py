import unittest

from sqlalchemy import union
from app.models import Comments, Pitches, User

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(password = 'banana')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)
        
    def test_no_access_password(self):
            with self.assertRaises(AttributeError):
                self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('banana'))
        
        


class TestPitches(unittest.TestCase):
    def setUp(self):
        self.new_pitches=Pitches(pitches='something amazing is cooking')
        
    def tearDown(self):
        Pitches.query.delete()
        
    def test_save_pitches(self):
        self.new_pitches.save_pitches()
        self.assertTrue(len(Pitches.query.all())>0)



class TestComments(unittest.TestCase):
    def setUp(self):
        self.new_comments= Comments(comment='Whats up')

    def tearDown(self):
        Comments.query.delete()
        User.query.delete()
        
    def test_save_comments(self):
        self.new_comments.save_comments()
        self.assertTrue(len(Comments.query.all())>0)