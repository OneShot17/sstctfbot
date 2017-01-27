# CTFBot - SSTCTF's Discord Bot


**Version:** 1.0.0

**Authors:** Andrew Quach and SST CTF Club

## Introduction

CTFBot is a private discord bot created for SST CTF club.
The bot is fully modular. Sets of commands can be enabled
or disabled through the addition or deletion of files in
cogs. 

## Features

Currently, the default set of cogs loaded include:
* Ciphers
* Hashes
* Base Conversions
* Quick Updating
* Permissions
* Misc Fun Commands

## Usage

CTFBot should be run from [launcher.py](https://github.com/SST-CTF/sstctfbot/blob/master/launcher.py) using python 3.5
or higher.

##### Example Usage:
    ./launcher.py
    python3 launcher.py
    python3.5 launcher.py

## Dependencies

CTFBot requires [discord.py](https://github.com/Rapptz/discord.py)
and Python 3.5+ in order to run.

##### Installation of Python 3.5:
    sudo add-apt-repository ppa:fkrull/deadsnakes
    sudo apt-get update
    sudo apt-get install python3.5

##### Installation of Python3 Pip:
    sudo apt-get install python3-pip

##### Installation of Discord.py:
    python3 -m pip install -U discord.py

## License
CTFBot is released under the [MIT License](LICENSE).
