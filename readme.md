# Discover everyweek

## Overview
This code uses spotify's API in order to copy your discover weekly playlist into a playlist of your choosing.

## Why?
Some people want to keep a history of their spotify's recommendations since they might hear something nice in there and forget it's name, but spotify changes the songs every week.

## Prerequisites 
What you need:
1. A spotify account
2. Some time and a bit of technological intuition

## Setup
1. Like the discover weekly playlist on spotify so that it appears in your library.
2. Create a copy of ".env_example" and rename it to ".env" 
3. Enter spotify's developer dashboard [here](https://developer.spotify.com/dashboard)
4. Create a new app with the name of your choosing
5. Set the redirect-url to "http://NONE"
6. Enter the app's settings and click on "View client secret"
7. Copy the client id and client secret into your .env file in the appropriate fields.

## Usuage
When using the script you can perform 2 functions:
### Rename the playlist you want the discover weekly to be saved into.
In order to rename the playlist you need to run the script as follows:  
```python3 discover-everyweek --set_playlist_name YOUR_PLAYLIST_NAME```
### Copy the discover weekly playlist into your centrelaized playlist.
In order to run the script's intended functionality you just need to run it.  
```python3 discover-everyweek```

## How can I make sure my playlists stays up-to-date?
Get your script to run on a schedule, it's different between different operation systems.
**NOTE**: your playlist will stay up to date for as long as your PC is on, or as long as your spotify API keys are valid, if you are looking for a way to make it more reliable look into cloud hosting.
### Windows
In windows you can schedule the script using schtasks.
1. Open a cmd as administrator (winkey cmd, right click "run as administrator").
2. run the following command, and substitute the python path to what comes up when you run ```which python``` and the script's path to your script path.  
```schtasks /create /tn "WeeklyDiscoveryUpdate" /tr "C:\Python\python.exe C:\Path\to\your\script\discover-everyweek.py" /sc weekly /d MON /st 09:00```
3. from now on, once a week your pc should run the script and update your playlist.
### Linux / Macos
The process in linux is similar, but uses cron.
1. Open a terminal.
2. Run the following command:  
```echo "0 9 * * 1 /usr/bin/python3 /path/to/your/script.py" | crontab -```
**Make sure to subtitute the paths.**

# Known bugs and quirks
Assuming you rename the playlist to a name of a playlist you already have on your account, the script will create a new one instead of adding to the existing one, this is still a WIP.
