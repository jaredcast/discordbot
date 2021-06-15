import praw
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

token = "NzQyNDk4NzYwMTM5MjEwOTUz.XzG_2w.GgnT65-feDPowJPwPNPGyTzYrlA" #Discord

omdbKey = "c76ae378" #For accessing movies

reddit = praw.Reddit(client_id="ffhuYrE2AX_XiQ",
                     client_secret="7inPNHVqBr5Cm9OmlzEt4j6fLV4",
                     user_agent="theguywithraybans")

ytkey = "AIzaSyBKMfkHWKojWgITEWSgwD41wlbFdD3J1GU"

spotifyID = "29d06803b3b040759b7764f0e1aa2800"
spotifySecret = "d62023ddf33b4fe8846a7bb7c93146f9"
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id = spotifyID, client_secret=spotifySecret))

'''Name	Artwork bot
Client Id	bf278dd04a50bcc73ea1
Client Secret	210179c193ef5e258453ed1209794651'''