# Python Application to Create Spotify Playlist #

## Description: ##
* Application can takes any block of text
* creates an playlist of Spotify tracks using the Spotify API.
* Input to the application is provided in the form of command line arguments, if not provided
	scripts prompts the user to provide a query text


## Dependency / Installation ##
pip install spotipy

## Quick Start Modules ##
* create_spotify_playlist.py:
	* Main class file
	* reads user input -> parses input -> authorizes spotify -> search for tracks
	* Following will give examples on how to execute the above script:
		* help on arguments: python create_spotify_playlist.py -h
		* Eg 1: python create_spotify_playlist.py "if i can't let it go out of my mind"
			* Output Format:
				* https://open.spotify.com/track/7JeKXMQKm6GoLGTkNy2jZ0
				* https://open.spotify.com/track/13HVjjWUZFaWilh2QUJKsP
				* https://open.spotify.com/track/7m4HUtdXRUHEitLIqbVWxf

		* Eg 2: python create_spotify_playlist.py
			* when no argument provided the script will prompt user to enter the input (shown below)
			* please enter query string here : "if i can't let it go out of my mind"

## Testing ##
* test_end_to_end.py
	* Performs end to end testing of the application
	* execution: python test_end_to_end.py

* test_unitest.py
	* Performs unittest
	* execution: python test_unitest.py

### Application Assumption ###
* Splits the user input into short text of size 3
* filter duplicate tracks
