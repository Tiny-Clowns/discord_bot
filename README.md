# discord_bot

## Description

This discord bot allows the users to play GO on discord and allows the administrators to moderate discord servers.

## Table of Contents

- [Features](#Features)
- [Installation](#Installation)
- [Customisation](#Customisation)

## Features

- Play big two with your friends on discord
- Moderate servers

## Installation

1. Clone the git repository.

2. Install the python3.

3. Install the discord python3 library

4. Discord token should be simply placed in token.txt. The token may find it on application page of discord developer

5. To start the bot, run the main.py. By typing "python3 main.py" or execute the "run.sh" shellscript.

## Customisation

- Allow all commands usable to you and admin, your and admin's discord id are recommended to put into admin.txt
    Your discord id can be found by using bot command whoami
    Every line should contain only one id


- To change the prefix is to modify the variable name CLIENT_CMD_PREFIX to your prefer prefix characters in main.py
    The prefix characters are $$