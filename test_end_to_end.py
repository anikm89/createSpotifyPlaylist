import os
import subprocess

class Complete_test_myplaylist:
    """
    This class performs end to end test for create spotify playlist
    """
    def test_case_1(self):
        print "test case1:"
        command_arg = "if i can't let it go out of my mind"
        print command_arg
        subprocess.call(["python", 'create_spotify_playlist.py',command_arg])
        print "\n"

    def test_case_2(self):
        print "test case2:"
        command_arg = "                           "
        print command_arg
        subprocess.call(["python", 'create_spotify_playlist.py',command_arg])
        print "\n"

    def test_case_3(self):
        print "test case 3:"
        command_arg = "letitgooutofmymind"
        print command_arg
        subprocess.call(["python", 'create_spotify_playlist.py',command_arg])
        print "\n"

    def test_case_4(self):
        print "test case 4:"
        command_arg = ""
        print command_arg
        subprocess.call(["python", 'create_spotify_playlist.py',command_arg])
        print "\n"


    def test_case_5(self):
        print "test case5:"
        command_arg = "if i cant let"
        print command_arg
        subprocess.call(["python", 'create_spotify_playlist.py',command_arg])
        print "\n"

    def test_case_6(self):
        print "test case6:"
        command_arg = "three little birds"
        print command_arg
        subprocess.call(["python", 'create_spotify_playlist.py',command_arg])
        print "\n"

    def test_case_7(self):
        print "test case7:"
        command_arg = "three little birds Turn your lights down low call me in afternoon "
        print command_arg
        subprocess.call(["python", 'create_spotify_playlist.py',command_arg])
        print "\n"

    def test_case_8(self):
        print "test case8:"
        command_arg = "let it go let it go let it go let it go let it go let it go"
        print command_arg
        subprocess.call(["python", 'create_spotify_playlist.py',command_arg])
        print "\n"

    def test_case_9(self):
        print "test case9:"
        command_arg = "The Handmaids Tale is not only a radical and brilliant departure for Margaret Atwood, " \
                      "it is a novel of such power that the reader will be unable to forget its images and its " \
                      "forecast. Set in the near future, it describes life in what was once the United States, now " \
                      "called the Republic of Gilead, a monotheocracy that has reacted to social unrest and a sharply declining " \
                      "birthrate by reverting to, and going beyond, the repressive intolerance of the original Puritans. " \
                      "The regime takes the Book of Genesis absolutely at its word, with bizarre consequences for the " \
                      "women and men of its population."
        print command_arg
        subprocess.call(["python", 'create_spotify_playlist.py',command_arg])
        print "\n"

    def test_case_10(self):
        print "test case10:"
        os.system("python create_spotify_playlist.py ")
        print "\n"

    def run_all(self):
        self.test_case_1()
        self.test_case_2()
        self.test_case_3()
        self.test_case_5()
        self.test_case_6()
        self.test_case_7()
        self.test_case_8()
        self.test_case_9()
        self.test_case_10()

testcases = Complete_test_myplaylist()
testcases.run_all()
print "All Test Cases Completed"