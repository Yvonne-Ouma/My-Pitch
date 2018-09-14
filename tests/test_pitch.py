import unittest
from app.models import Pitch,User
from app import db

class PitchModelTest(unittest.TestCase):

    def setUp(self):
        
        self.new_pitch = Pitch(id=187,title = "interview",category = "Interview", content = "the best")
    

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()
        
    def test_check_instance_variable(self):
        self.assertEquals(self.new_pitch.title,'interview')
        self.assertEquals(self.new_pitch.category,'Interview')
        self.assertEquals(self.new_pitch.content, 'the best')

    def test_save_pitch(self):
        Pitch.save_pitch(self.new_pitch)
        self.assertTrue(len(Pitch.query.all()) >0)

    def test_get_pitch_by_id(self):
        self.assertEqual(self.new_pitch.id,187)




    