import discord
from discord.ext import commands
from .utils import checks
from __main__ import Bot
import datetime

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

    @commands.command()
    async def uptime(self):
        await self.bot.say("CTFBot has been up for: **{}**".format(self.get_uptime()))

    def get_uptime(self):
        now = datetime.datetime.utcnow()
        elapsed = now - self.bot.start_time
        hours, remainder = divmod(int(elapsed.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)

        if days:
            fmt = '{d} days, {h} hours, {m} minutes, and {s} seconds'
        else:
            fmt = '{h} hours, {m} minutes, and {s} seconds'

        return fmt.format(d=days, h=hours, m=minutes, s=seconds)

def setup(bot):
    bot.add_cog(Admin(bot))
