# Python Application to Create Spotify Playlist #

## Description: ##
* Application can takes any block of text
* creates an playlist of Spotify tracks using the Spotify API.
* Input to the application is provided in the form of command line arguments, if not provided
	scripts prompts the user to provide a query text


## Installation ##
pip install Spotify

## Quick Start Modules ##
* create_spotify_playlist.py:
	* Main class file
	* reads user input -> parses input -> authorizes spotify -> search for tracks
	* Following will give examples on how to execute the above script:
		* help on arguments: python create_spotify_playlist.py -h
		* Eg 1: python create_spotify_playlist.py "if i can't let it go out of my mind"
		* Eg 2: python create_spotify_playlist.py
			* when no argument provided the script will prompt user to enter the input

* test_end_to_end.py
	* Performs end to end testing on create_spotify_playlist.py
* test_unitest.py
	* Performs unittest

### Application Assumption ###
* Splits the user input into short text of size 3
* filter duplicate tracks
