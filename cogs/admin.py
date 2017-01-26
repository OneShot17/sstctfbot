import discord
from discord.ext import commands
from .utils import checks
from __main__ import Bot

class Admin:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.is_owner()
    async def shutdown(self):
        await self.bot.shutdown(restart=False)
        
    @commands.command()
    @checks.is_owner()
    async def update(self):
        await self.bot.shutdown(restart=True, update=True)

    @commands.command()
    @checks.is_owner()
    async def restart(self):
        await self.bot.shutdown(restart=True)
    
    @commands.command()
    @checks.is_owner()
    async def status(self, status: str):
        await self.bot.change_presence(game=discord.Game(name=status)) 


def setup(bot):
    bot.add_cog(Admin(bot))
