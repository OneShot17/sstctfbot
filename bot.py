#!/usr/bin/env python3

import asyncio
import json
import sys
import datetime

try:
    assert sys.version_info >= (3, 5)
    import discord
    from discord.ext import commands
except ImportError:
    print("Discord.py needs to be installed")
    sys.exit()
except AssertionError:
    print("Bot needs Python 3.5 or higher to run.")
    sys.exit()

description = "Offical SSTCTF Club Bot"

class Bot(commands.Bot):
    def __init__(self, description):
        self.shutdown_mode = None
        self.update_mode = False
        self.start_time = datetime.datetime.utcnow()
        self.command_prefix = '!'
        self.default_status = 'Now with custom statuses!'
        super().__init__(command_prefix=self.command_prefix, description=description)

    async def shutdown(self, restart=False, update=False):
        self.shutdown_mode = not restart
        self.update_mode = update
        await self.logout()

def initialize(bot_class=Bot):
    bot = bot_class(description)
    
    @bot.event
    async def on_ready():
        await bot.change_presence(game=discord.Game(name=bot.default_status))

        print('------')
        print('SST CTF Discord Bot')
        print('Logged in as:')
        print('Username: ' + bot.user.name)
        print('ID: ' + bot.user.id)
        print('------')

    @bot.event
    async def on_message(message):
        if bot.user.mentioned_in(message) and not message.mention_everyone:
            await bot.send_message(message.channel, 'Feels bad man')

        await bot.process_commands(message)

    # TODO: Implement Errors
    @bot.event
    async def on_command_error(error, ctx):
        channel = ctx.message.channel
        if isinstance(error, commands.MissingRequiredArgument):
            pass
        elif isinstance(error, commands.BadArgument):
            pass
        elif isinstance(error, commands.DisabledCommand):
            pass
        elif isinstance(error, commands.CommandInvokeError):
            pass
        elif isinstance(error, commands.CommandNotFound):
            pass
        elif isinstance(error, commands.CheckFailure):
            pass
        elif isinstance(error, NoPrivateMessage):
            pass
        else:
            pass

    return bot

def load_cogs(bot):
    startup_extensions = ["cogs.ctf", "cogs.misc", "cogs.admin"]
    
    for extension in startup_extensions:
        bot.load_extension(extension)

def load_credentials():
    with open('credentials.json') as f:
        return json.load(f)

def main(bot):
    load_cogs(bot)
    token = load_credentials()['token']
    yield from bot.login(token)
    yield from bot.connect()

if __name__ == '__main__':
    bot = initialize()
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(bot))
    except KeyboardInterrupt:
        loop.run_until_complete(bot.logout())
    except Exception as e:
        loop.run_until_complete(bot.logout())
    finally:
        loop.close()
        if bot.shutdown_mode is True:
            exit(0)
        elif bot.shutdown_mode is False:
            if bot.update_mode is True:
                exit(25)
            else:
                exit(26)
        else:
            exit(1)
