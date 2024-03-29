# p99_login_helper.py

A fix for Linux clients running Project 1999 and getting an empty server list. I've only tested this using the built in Python 3.10.x that's included on all Steam Decks so no extra dependencies are needed and no need to compile code for this fix. This repo is "use at your own risk" and is released under the MIT license.

## How to setup EQ to start on a Steam Deck

### Install a MIDI synth

*This is optional but without it, you won't get the full nostalgia of the EverQuest loading screen.*
Follow 1-3 in this guide:
https://steamcommunity.com/sharedfiles/filedetails/?id=2809933598

### Setup EQ to run with fix in Gaming Mode

Assuming you have a copy of EverQuest: Titanium Edition client in Windows:

1. Zip the EverQuest root folder in your Windows machine (the folder that contains `EverQuest.bat`), transfer it to your Steam Deck and unzip it somewhere in the home directory.
2. In the Steam Deck Desktop Mode, open a browser and download (right click save as) [this Python script](https://raw.githubusercontent.com/rtrajano/p99_login_helper/main/p99_login_helper.py) into your copy of the EverQuest root folder.
    1. Make sure the script is executable. You can `chmod` it or navigate to the file in the file browser, right click the file > "Properties" > "Permissions" > and tick the "Is executable" checkbox.
3. Navigate to your EverQuest root folder and modify `eqhost.txt` to point to `Host=localhost:5998` instead of what is currently in there.
4. Open the desktop version of Steam. In the toolbar, click "Games" > "Add a Non-Steam Game to My Library" > "Browse" > Set "File type:" to "All Files"
5. In the file selection dialog, navigate to your EverQuest root folder and select `EverQuest.bat`
6. Copy Paste this into the "Launch Options" box: `flatpak run org.rncbc.qsynth & timeout 5m ./p99_login_helper.py & %command% ; killall -9 qsynth`
    1. This command will start the qsynth service
    2. Start the p99_login_helper.py with a 5 minute timeout so it's not running forever. If you need to logout and back in, just exit EQ altogether.
    3. Start EQ
    4. When EQ exits, it will kill the qsynth service
7. In the left navigation pane, select "Compatibility" and tick the checkbox then close the game settings window.
8. Switch back to Gaming Mode and enjoy!

If you need some pointers on configuring Steam Input, I highly recommend watching this for tips, and inspiration: https://www.youtube.com/watch?v=eUmUdcRhM6g

## Normal Linux Instructions

1. Navigate to your EverQuest root folder and modify `eqhost.txt` to point to `Host=localhost:5998` instead of what is currently in there.
2. You'll need a working Python 3 installation. Verify by typing `python3 --version` in a terminal. It should return with `Python 3.X.X`
3. git clone this repo and start the script via `python3 ./p99_login_helper.py` in a separate terminal or as a background process.
    1. It's only needed during login. Once in the game, you can end the process.

## What the script does

It makes a UDP server that acts as a proxy between the EQ client and the login server. The script is simple so you can inspect it yourself.

## Thanks

Special thanks to [@Zaela](https://github.com/Zaela) for figuring out the problem and their original tool https://github.com/Zaela/eqemu-login-helper
