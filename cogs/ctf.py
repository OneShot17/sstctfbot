import discord
from discord.ext import commands

import string
import hashlib
import base64

class CTF:

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(description='Caesar Cipher')
    async def caesar(shift:int, plaintext:str):
        alphabet = string.ascii_lowercase
        shifted_alphabet = alphabet[shift%26:] + alphabet[:shift%26]
        table = str.maketrans(alphabet, shifted_alphabet)
        await bot.say(plaintext.lower().translate(table))

    @commands.command()
    async def add(*args:int):
        await bot.say(sum(args))

    @commands.command()
    async def addbin(*args:str):
        tmp = [int(k, 2) for k in args]
        await bot.say(bin(sum(tmp)))

    @commands.command()
    async def addhex(*args:str):
        tmp = [int(k, 16) for k in args]
        await bot.say(hex(sum(tmp)))

    @commands.command()
    async def md5(message:str):
        await bot.say(hashlib.md5(message.encode()).hexdigest())

    @commands.command()
    async def sha1(message:str):
        await bot.say(hashlib.sha1(message.encode()).hexdigest())

    @commands.command()
    async def sha256(message:str):
        await bot.say(hashlib.sha256(message.encode()).hexdigest())

    @commands.command()
    async def bintohex(number:str):
        await bot.say(hex(int(number, 2)))

    @commands.command()
    async def bintodec(number:str):
        await bot.say(int(number, 2))

    @commands.command()
    async def dectohex(number:int):
        await bot.say(hex(number))

    @commands.command()
    async def dectobin(number:int):
        await bot.say(bin(number))

    @commands.command()
    async def hextodec(number:str):
        await bot.say(int(number, 16))

    @commands.command()
    async def hextobin(number:str):
        await bot.say(bin(int(number, 16)))

    @commands.command()
    async def base64(message:str):
        await bot.say(base64.b64encode(message.encode('utf-8')).decode('utf-8'))

    @commands.command()
    async def base64d(message:str):
        await bot.say(base64.b64decode(message.encode('utf-8')).decode('utf-8'))

def setup(bot):
   bot.add_cog(CTF(bot))
