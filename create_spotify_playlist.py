import argparse
import re
import spotipy
import spotipy.oauth2 as oauth2

class MyTracks:

    """
    user creadentials required for spotify API access
    """
    client_id = "b7b40ecaa6d24e83bad635789982e49a"
    client_secret = "ac16b9958e68445f8c13c2b6a9970c9b"
    redirect_uri = 'http://localhost:8888/callback'

    def __init__(self):
        """
        This is the constructor for class MyTracks, handles variable initialization
        :return:
        """
        self.tracks_not_found = []
        self.in_ = []
        self.tracks_dict = {}
        self.poem_len = 3
        self.errmsg_invalid_input = "Please enter the valid input, exiting the script"
        self.errmsg_credentials = ", please check credentials, exiting the script"
        self.errmsg_cannot_find = 'Cannot find a track for the string passed :'

    def authenticate_spotify(self, client_id, client_secret):
        """
        This function handles authentication for spotify webapi.
        provides user credentials to get access and return a response token object

        :param client_id:user credential,global variable
        :param client_secret:user credential,global variable
        :return:spotify authorization object
        """
        try:
            credentials = oauth2.SpotifyClientCredentials\
                            (client_id=client_id, client_secret=client_secret)
            token = credentials.get_access_token()
            spotify = spotipy.Spotify(auth=token)
            return spotify
        except spotipy.oauth2.SpotifyOauthError as errmsg:
            print errmsg, self.errmsg_credentials
            raise SystemExit()
        except AttributeError as errmsg:
            print errmsg
            raise SystemExit()

    def getinput(self):
        """
        This function requests customer to provide input text to search for tracks.
        It handles user input either in the form of command line, in case not provided
        prompts user to enter the query string

        :return:input_str, string value from command line or user provided input
        """
        parser = argparse.ArgumentParser()
        parser.add_argument('string',
                            nargs=argparse.REMAINDER,
                            type=str,
                            help='Please provide a valid input enclosed in quotes(" ")')

        args = parser.parse_args()
        if len(args.string) > 1:
            parser.print_help()
            raise SystemExit

        try:
            input_str = args.string[0]
            return input_str
        except IndexError:
            print 'Command line input was not provided'
            input_str = str(raw_input("please enter query string here :"))
            return input_str

    def parse_input(self, search_str):
        """
        This function accepts the input string provided by the user.
         1. It parses through the string using a regular expressiosn removes unwanted characters
            and splits the string into a list.
            "if I can't let it go out of my mind" =>
                 ['if', "can't", 'let', 'it', 'go', 'out', 'of', 'my', 'mind']

         2. It then groups them into a minimum size of 3
            ['if', "can't", 'let', 'it', 'go', 'out', 'of', 'my', 'mind'] =>
                 ['"if can't let", 'it go out', 'of my mind']

            if the overall length is <=3, it will keep the string as its
            eg: ["let", "it"] => ["let it"]

        :param search_str: text provided by the user
        :return:input_str_list, list of small poems
        """
        search_str = search_str.decode('string_escape')
        regex = r'[a-zA-Z0-9\']+'
        search_str = re.findall(regex, search_str)
        search_str_len = len(search_str)

        if search_str_len > self.poem_len:
            input_str_list = [" ".join(search_str[i:i+self.poem_len])
                              for i in range(0, search_str_len, self.poem_len)]
            str_len = len(input_str_list)
            if len(input_str_list[str_len-1].split(" ")) != self.poem_len:
                input_str_list[str_len-1] = " ".join(input_str_list[str_len-2:str_len])
                input_str_list.pop(str_len-2)
            print input_str_list
            return input_str_list
        else:
            self.in_ = []
            self.in_.append(" ".join(search_str))
            print self.in_
            return self.in_

    def tracksearch(self, search_str, spotify):
        """
        This function utilizes the provided list of small poems (query strings)
        and spotify authorization token. It then make calls to spotify API
        searching for tracks related to the query passed.

        The response is in JSON format. Further filtering into the JSON schema to print
        the required url.

        A check is enabled to store the poem(query string) in a dictionary
        if the poem is already present in the dictionary, it will then just try to access url
        from there instead of accessing the API.
        dictionary format:
        {"let it go": "https://open.spotify.com/track/13HVjjWUZFaWilh2QUJKsP"}

        :param search_str:list of small poems
        :param spotify:Authorization token object, to call spotify api methods
        :return:tracks_dict, dictionary of small poems with their track url's
        """
        self.tracks_list = []

        if len(search_str) <= 1:
            if search_str[0] == '':
                print self.errmsg_invalid_input
                raise SystemExit
        flag = False
        for index, str_ in enumerate(search_str):
            try:
                if str_.lower() not in self.tracks_dict:
                    response = spotify.search(str_, limit=1, offset=0, market=None)
                    tracks_url = response["tracks"]["items"][0]["external_urls"]["spotify"]
                    self.tracks_dict[str_.lower()] = tracks_url
                    flag = True
                    print "*", tracks_url
            except spotipy.client.SpotifyException:
                print 'No Search Query Provided exiting the script'
            except IndexError:
                errmsg = self.errmsg_cannot_find, str_
                self.tracks_list.append(errmsg)
                if flag is False and index == len(search_str)-1:
                    print self.errmsg_cannot_find, " ".join(search_str)
            except AttributeError as errmsg:
                print errmsg
        return self.tracks_dict, self.tracks_list


    def run(self):
        """
        This function acts as a main pipeline function.
        it calls the above function in the following sequence
        getuserinput -> parse input -> autheticate spotify -> spotify track search
        "
        :return:
        """
        input_str = self.getinput()
        input_str = self.parse_input(input_str)
        spotify = self.authenticate_spotify(self.client_id, self.client_secret)
        try:
            self.tracksearch(input_str, spotify)
        except TypeError:
            print self.errmsg_invalid_input

if __name__ == '__main__':
    create_playlist = MyTracks()
    create_playlist.run()
