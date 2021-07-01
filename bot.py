
import discord
from discord.ext import commands
from json import load
# Locals
from os import listdir

# Load Configs
with open("config.json", "r") as f:
    config = load(f)


bot = commands.Bot(command_prefix=commands.when_mentioned_or(config["prefix"]))



@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}:{bot.user.id}")
    game = discord.Game(config["status"])
    await bot.change_presence(status=discord.Status.idle, activity=game)

    
    
    
if __name__ == "__main__":
    # Load all cogs
    cogs = ["cogs."+f[0:-3] for f in listdir("./cogs") if f[-3:]==".py"]
    for cog in cogs:
        bot.load_extension(cog)   
    # Start Bot
    bot.run(config["login"]["token"])
