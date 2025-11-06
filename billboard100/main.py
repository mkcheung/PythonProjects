from bs4 import BeautifulSoup
from datetime import datetime
from dotenv import load_dotenv
import os
from pathlib import Path
from pprint import pprint
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
SPOTIFY_REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI')

class Billboard100:
    def __init__(self):
        self.billboardEndpoint = "https://www.billboard.com/charts/hot-100/"
        self.workingDirectory = Path(__file__).resolve().parent
        self.getDate()

    def getDate(self):
        while True:
            try:
                # Original assignment was based off on an old api. Substitute with current date for now
                # selectedDateTime = input("What you do you want the top 100 songs of? Please enter in this format YYYY-MM-DD: ")
                selectedDateTime = input("Enter current date. Please enter in this format YYYY-MM-DD: ")
                validate = datetime.strptime(selectedDateTime, "%Y-%m-%d")
                self.dateForTop100 = selectedDateTime
                break;
            except:
                print("Date must be entered in the following format: YYYY-MM-DD. Please try again: \n\n")
    
    def executeRequest(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
        }
        # Original assignment was based off on an old api. Substitute with current date for now
        # response = requests.get(f"{self.billboardEndpoint}{self.dateForTop100}", headers=headers)
        response = requests.get(f"https://www.billboard.com/charts/hot-100/", headers=headers)
        response.raise_for_status();
        self.top100Songs = response.text

    def parseSongs(self):
        soup = BeautifulSoup(self.top100Songs, 'html.parser')
        self.songs = soup.select("div.o-chart-results-list-row-container li.o-chart-results-list__item h3#title-of-a-story")
        self.artists = soup.select("div.o-chart-results-list-row-container li.o-chart-results-list__item span a")
        titles = [song.get_text(strip=True) for song in self.songs]
        artistNames = [artist.get_text(strip=True) for artist in self.artists]
        self.songsAndArtists = [ f"{song} by {artist}" for song, artist in zip(titles, artistNames)]
        return self.songsAndArtists
    
    def createSpotifyPlaylist(self):
        sp = spotipy.Spotify(
                auth_manager=SpotifyOAuth(
                scope="playlist-modify-private",
                redirect_uri=SPOTIFY_REDIRECT_URI,
                client_id=SPOTIFY_CLIENT_ID,
                client_secret=SPOTIFY_CLIENT_SECRET,
                show_dialog=True,
                cache_path=f"{self.workingDirectory}/token.txt",
                username="mkcheung0", 
            )
        )
        user_id = sp.current_user()["id"]
        songuris = [];
        for song_title in self.songs:
            result = sp.search(q=song_title, limit=1, type='track')
            songuris.append(result['tracks']['items'][0]['uri'])

        playlist = sp.user_playlist_create(
            user=user_id,
            name=f"{self.dateForTop100} Billboard 100",
            public=False
        )
        playlist_id = playlist['id']
        sp.playlist_add_items(playlist_id=playlist_id, items=songuris)


billboard100 = Billboard100()
billboard100.executeRequest()
billboard100.parseSongs()
billboard100.createSpotifyPlaylist()
# 2000-08-12/

