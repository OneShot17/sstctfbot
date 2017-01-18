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

    @commands.command()
    async def tamir2(self):
        await self.bot.say('''Interviewer: What\'s your greatest accomplishment?

Tamir: I got a 9 in AP Lang once!''')

    @commands.command()
    async def d6(self):
        await self.bot.say('''4  
http://xkcd.com/221/''')

def setup(bot):
    bot.add_cog(Misc(bot))
