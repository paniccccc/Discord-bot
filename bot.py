import discord
from discord.ext import commands 

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Bot is up and running !")

@client.command()
async def hello(ctx):
    await ctx.send("Fuck off you cunt")



client.run("NzY5MjA4MTg1OTM1NjI2MzEx.X5Lq8g._Pk6q6eTTFhfm8ytfXE0398lpvc")

