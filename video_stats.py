import requests
import json

import os
from dotenv import load_dotenv
load_dotenv(dotenv_path=r'./.env')
API_KEY = os.getenv('API_KEY')
CHANNEL_HANDLE = 'MrBeast'

def get_playlist_id(channel_handle):
    try:
        url = rf'https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={channel_handle}&key={API_KEY}'
        response = requests.get(url)
        data = response.json()
        channel_items = data["items"][0]
        return channel_items["contentDetails"]["relatedPlaylists"]["uploads"]
    except requests.exceptions.RequestException as e:
        raise e

if __name__ == "__main__":
    playlist_id = get_playlist_id(CHANNEL_HANDLE)
    print(playlist_id)
