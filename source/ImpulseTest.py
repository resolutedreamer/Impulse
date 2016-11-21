import unittest
import sys
from Impulse import ImpulseController

class Test_ImpulseHubTest(unittest.TestCase):
    def setUp(self):
        self.assertTrue(len(sys.argv) < 1)
        playlist = []
        for i in range(1, len(sys.argv)):
            playlist.append(sys.argv[i])
        self.newImpulse = ImpulseController(playlist)

    def test_play_song(self):
        self.newImpulse.play_song()

    def test_play_all(self):
        self.newImpulse.play_all()

if __name__ == '__main__':
    unittest.main()