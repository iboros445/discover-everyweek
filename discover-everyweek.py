import playlists
import spotipy
import argparse
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

SCOPE = ["playlist-modify-private","playlist-read-private"]


def argument_parsing():
    parser = argparse.ArgumentParser(description='Add discover weekly into another playlist')
    parser.add_argument('--playlist_name', help='name of new playlist to create, defaults to "discovery"', default="Discovery")
    parser.add_argument("--require_new_playlist", action=argparse.BooleanOptionalAction, default=True, help="Should create new playlist (will also be used in future) or use old one")
    # TODO: add functionality that can use old playlist with given name (we give a name in playlist_name and add to it.)
    args = parser.parse_args()
    return args

def main():
    args = argument_parsing()
    load_dotenv()
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE))
    playlist_to_move_to_id = playlists.get_or_create_playlist(sp, args.playlist_name)
    discover_weekly_id = playlists.get_discover_weekly(sp)
    playlists.copy_one_playlist_to_another(sp ,discover_weekly_id, playlist_to_move_to_id)

if __name__=="__main__":
    main()
