import discord
from discord.ext import commands 

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Bot is up and running !")

@client.command()
async def hello(ctx):
    await ctx.send("Fuck off you cunt")



client.run("NzY5MjA4MTg1OTM1NjI2MzEx.X5Lq8g.9r-cml5TiTsI87Ienki5M0wKQDQ")

