import discord
from discord.ext import commands
import asyncio
import json

import string
import hashlib
import base64

startup_extensions = ["cogs.ctf", "cogs.misc"]
bot = commands.Bot(command_prefix='!', description='Offical SSTCTF Club Bot')

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='Try !killme'))

    print('------')
    print('Logged in as:')
    print('Username: ' + bot.user.name)
    print('ID: ' + bot.user.id)
    print('------')

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message) and message.mention_everyone:
        await bot.send_message(message.channel, 'Feels bad man')

    await bot.process_commands(message)

def load_credentials():
    with open('credentials.json') as f:
        return json.load(f)

if __name__ == '__main__':
    credentials = load_credentials()
    
    for extension in startup_extensions:
        bot.load_extension(extension)

    bot.run(credentials['token'])
