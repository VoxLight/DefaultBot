import discord
from discord.ext import commands

"""
Allows testing if online
"""
class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("Basic cog loaded.")
        
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Ping: {self.bot.latency}ms")

def setup(bot):
    bot.add_cog(Basic(bot))