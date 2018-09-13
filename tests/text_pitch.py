import unittest
from app.models import Pitch

class PitchModelTest(unittest.TestCase):

    def setUp(self):
        self.new_pitch = Pitch(password = 'banana')

    