import unittest
from create_spotify_playlist import MyTracks

c = MyTracks()

class TestUM(unittest.TestCase):
    """
    This class contains unittest cases for the spotify create playlist
    """

    client_id = "b7b40ecaa6d24e83bad635789982e49a"
    client_secret = "ac16b9958e68445f8c13c2b6a9970c9b"
    redirect_uri = 'http://localhost:8888/callback'

    def test_parseinput(self):
        self.assertEqual( c.parse_input("hello"), ["hello"])

    def test_parseinput1(self):
        self.assertEqual( c.parse_input("if i can't let it go out of my mind"), ["if i can't", "let it go", "out of my mind"])

    def test_parseinput2(self):
        self.assertEqual( c.parse_input("if i can't let"), ["if i can't let"])

    def test_parseinput3(self):
        self.assertEqual( c.parse_input("world there"), ["world there"])

    def test_parseinput4(self):
        self.assertEqual( c.parse_input(""), [""])

    def test_parseinput5(self):
        self.assertEqual( c.parse_input("if i can't let it"), ["if i can't let it"])

    def test_parseinput6(self):
        self.assertEqual( c.parse_input("let it go let it go let it go let it go let it go let it go"),
                          ["let it go","let it go","let it go","let it go","let it go","let it go"])

    def test_parseinput7(self):
        self.assertEqual( c.parse_input("Let it go \n \t out of my -mind !!! ##"), ['Let it go', 'out of my mind'])


if __name__ == '__main__':
    unittest.main()
    print " Finished executing Unit test Cases"