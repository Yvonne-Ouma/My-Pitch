import unittest
from app.models import Comment,User
from app import db

class CommentModelTest(unittest.TestCase):

    def setUp(self):  
        
        self.new_comment = Comment( id=96,title = "eeh", comment = "good for blogers",pitch_id=1)

    def tearDown(self):
        Comment.query.delete()
        User.query.delete()
        
    def test_check_instance_variable(self):
        self.assertEquals(self.new_comment.title,'eeh')
        self.assertEquals(self.new_comment.comment,'good for blogers')

    def test_save_comment(self):
        Comment.save_comment(self.new_comment)

        self.assertTrue(len(Comment.query.all()) >0)

    def test_get_pitch_by_id(self):
        self.assertEqual(self.new_comment.pitch_id,1)   