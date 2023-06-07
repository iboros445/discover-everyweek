import playlists
import spotipy
import argparse
import os
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

SCOPE = ["playlist-modify-private", "playlist-read-private"]


def argument_parsing():
    parser = argparse.ArgumentParser(
        description='Add discover weekly into another playlist')
    parser.add_argument(
        '--set_playlist_name',
        help='name of new playlist to create, defaults to "Discovery"')
    parser.add_argument(
        "--require_new_playlist",
        action=argparse.BooleanOptionalAction,
        default=False,
        help="Should create new playlist (will also be used in future) or use old one")
    args = parser.parse_args()
    return args


def main():
    load_dotenv()
    args = argument_parsing()
    if args.set_playlist_name:
        playlists.set_playlist_name(args.set_playlist_name)
        print(">>INFO: Playlist name set correctly. please run again!")
        exit(0)
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE))
    playlist_to_move_to_id = playlists.get_or_create_playlist(
        sp, os.getenv("DISCOVER_EVERYWEEK_NAME"))
    discover_weekly_id = playlists.get_discover_weekly(sp)
    playlists.copy_one_playlist_to_another(
        sp, discover_weekly_id, playlist_to_move_to_id)


if __name__ == "__main__":
    main()
