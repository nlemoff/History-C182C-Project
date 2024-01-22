# Spotify Activity Reader

## Overview
This Python script was originally used to collect empirical data while conducting an experiment for History C182C: Introduction to Science, Technology and Society at UC Berkeley, the results of which can be viewed [here](https://docs.google.com/document/d/1AihURqtPM_gjCDILBot2BaV0z2UUntyKcxRa3jzwzMI/edit?usp=sharing). It utilizes the `spotipy` library to interact with the Spotify Web API, specifically to fetch information about the track currently playing on a user's Spotify account. The main purpose of this script is to assist in recording data for an empirical experiment related to new features on Spotify.

## Features
- Fetches the currently playing track's title and artist from a user's Spotify account.
- Utilizes the Spotify Web API for real-time data access.
- Can be integrated into larger systems for empirical data collection and analysis.

## Requirements
- Python 3
- `spotipy` library
- A Spotify account
- Spotify Developer credentials (Client ID, Client Secret, and Redirect URI)

## Setup
1. **Install Spotipy**: You need to have the `spotipy` library installed. You can install it using pip:
   ```bash
   pip install spotipy
   ```
2. **Spotify Developer Credentials**: You must register your application on the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) to get your Client ID and Client Secret. You also need to set a Redirect URI for your application in the dashboard.

3. **Environment Variables**: It's recommended to set your Spotify credentials (Client ID, Client Secret, and Redirect URI) as environment variables for security reasons. Alternatively, you can directly insert them into the script.

## Usage
To run the script, execute it in your Python environment:
```bash
python current_track_info.py
```

If a song is currently playing on your Spotify account, the script will output the track's title and artist. If no song is playing, it will notify you accordingly.

## Note
This script is intended for personal and experimental use, particularly in relation to studying Spotify's features. It's important to adhere to Spotify's terms of use when interacting with their API.

## Disclaimer
This project is not affiliated with Spotify and is created for educational purposes. Spotify is a registered trademark of Spotify AB.

---

Remember to replace `"YOUR_CLIENT_ID"`, `"YOUR_CLIENT_SECRET"`, and `"YOUR_REDIRECT_URI"` in the script with your actual Spotify Developer credentials. For detailed instructions on how to obtain these credentials, refer to the Spotify Developer Documentation.
