import re
import requests
import os

SOURCE_URL = os.environ["SOURCE_URL"]
PLAYLIST_FILE = "playlist.m3u8"

def get_new_token():
    resp = requests.get(SOURCE_URL, allow_redirects=True)
    final_url = resp.url
    match = re.search(r'(\?hdnea=.+)', final_url)
    if match:
        return match.group(1)
    return None

def update_playlist(token):
    with open(PLAYLIST_FILE, 'r') as f:
        content = f.read()
    updated = re.sub(r'\?hdnea=[^\s]+', token, content)
    with open(PLAYLIST_FILE, 'w') as f:
        f.write(updated)
    print("Playlist updated with new token.")

if __name__ == "__main__":
    token = get_new_token()
    if token:
        print(f"New token fetched successfully.")
        update_playlist(token)
    else:
        print("Failed to get token!")
        exit(1)
