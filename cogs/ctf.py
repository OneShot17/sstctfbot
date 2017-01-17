import discord
from discord.ext import commands

import string
import hashlib
import base64

class CTF:

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(description='Caesar Cipher')
    async def caesar(self, shift:int, plaintext:str):
        alphabet = string.ascii_lowercase
        shifted_alphabet = alphabet[shift%26:] + alphabet[:shift%26]
        table = str.maketrans(alphabet, shifted_alphabet)
        await self.bot.say(plaintext.lower().translate(table))

    @commands.command()
    async def add(self, *args:int):
        await self.bot.say(sum(args))

    @commands.command()
    async def addbin(self, *args:str):
        tmp = [int(k, 2) for k in args]
        await self.bot.say(bin(sum(tmp)))

    @commands.command()
    async def addhex(self, *args:str):
        tmp = [int(k, 16) for k in args]
        await self.bot.say(hex(sum(tmp)))

    @commands.command()
    async def md5(self, message:str):
        await self.bot.say(hashlib.md5(message.encode()).hexdigest())

    @commands.command()
    async def sha1(self, message:str):
        await self.bot.say(hashlib.sha1(message.encode()).hexdigest())

    @commands.command()
    async def sha256(self, message:str):
        await self.bot.say(hashlib.sha256(message.encode()).hexdigest())

    @commands.command()
    async def bintohex(self, number:str):
        await self.bot.say(hex(int(number, 2)))

    @commands.command()
    async def bintodec(self, number:str):
        await self.bot.say(int(number, 2))

    @commands.command()
    async def dectohex(self, number:int):
        await self.bot.say(hex(number))

    @commands.command()
    async def dectobin(self, number:int):
        await self.bot.say(bin(number))

    @commands.command()
    async def hextodec(self, number:str):
        await self.bot.say(int(number, 16))

    @commands.command()
    async def hextobin(self, number:str):
        await self.bot.say(bin(int(number, 16)))

    @commands.command()
    async def base64(self, message:str):
        await self.bot.say(base64.b64encode(message.encode('utf-8')).decode('utf-8'))

    @commands.command()
    async def base64d(self, message:str):
        await self.bot.say(base64.b64decode(message.encode('utf-8')).decode('utf-8'))

def setup(bot):
   bot.add_cog(CTF(bot))
