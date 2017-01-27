from discord.ext import commands
import discord.utils

def is_owner_check(message):
    return message.author.id == "156372767166562305"

def is_owner():
    return commands.check(lambda ctx: is_owner_check(ctx.message))

def is_admin_check(message):
    for role in message.author.roles:
        if role.id == "190584251341602817":
            return True
    return False

def is_admin():
    return commands.check(lambda ctx: is_admin_check(ctx.message))
