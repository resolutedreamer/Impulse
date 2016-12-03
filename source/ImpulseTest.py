import unittest
import sys
from Impulse import ImpulseController

class Test_ImpulseHubTest(unittest.TestCase):
    def setUp(self):
        self.newImpulse = ImpulseController(playlist, com)

    def test_play_all(self):
        self.newImpulse.play_all()

if __name__ == '__main__':
    playlist = []
    com = ""
    if len(sys.argv) >= 3:
        com = sys.argv[1]
        for i in range(2, len(sys.argv)):
            playlist.append(sys.argv[i])            
    print playlist
    sys.argv = sys.argv[:1]
    unittest.main()