import requests
import base64
import os
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")

def get_access_token():
    auth_url = "https://accounts.spotify.com/api/token"
    auth_header = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    
    headers = {
        "Authorization": f"Basic {auth_header}"
    }

    data = {
        "grant_type": "client_credentials"
    }

    response = requests.post(auth_url, headers=headers, data=data)
    return response.json()["access_token"]

def search_artist(artist_name, access_token):
    url = f"https://api.spotify.com/v1/search"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    params = {
        "q": artist_name,
        "type": "artist",
        "limit": 1
    }

    response = requests.get(url, headers=headers, params=params)
    results = response.json()

    if results["artists"]["items"]:
        return results["artists"]["items"][0]["id"]
    else:
        return None

def get_top_tracks(artistID, accessToken):
    url = f"https://api.spotify.com/v1/artists/{artistID}/top-tracks"
    headers = {
        "Authorization": f"Bearer {accessToken}"
    }
    params = {
        "market": "US"
    }

    response = requests.get(url, headers=headers, params=params)
    tracks = response.json()["tracks"]

    print("\n🎵 Top Tracks:\n")
    for i, track in enumerate(tracks[:10], 1):
        print(f"{i}. {track['name']}")


artist_name = input("Enter the name of a music artist: ")
access_token = get_access_token()
artist_id = search_artist(artist_name, access_token)

if artist_id:
    get_top_tracks(artist_id, access_token)
else:
    print("Artist not found! Search for another one")
