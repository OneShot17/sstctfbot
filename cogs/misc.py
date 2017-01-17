import discord
from discord.ext import commands

class Misc:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def killme(self):
        await self.bot.say('Suicide Hotline: 1-800-273-8255')

    @commands.command()
    async def documentation(self):
        await self.bot.say('''Is there any documentation for this? 
        
    Not at the moment.
    ''')

    @commands.command()
    async def tamir(self):
        await self.bot.say('Feels bad man :(')

def setup(bot):
    bot.add_cog(Misc(bot))
