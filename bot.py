import discord
from discord.ext import commands 

client = commands.Bot(command_prefix="!")

f=open("rules.txt","r")
rules=f.readlines()

@client.event
async def on_ready():
    print("Bot is up and running !")

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')


@client.command()
async def hello(ctx):
    await ctx.send("Hey there !")


@client.command()
async def cringe(ctx):
    await ctx.send("Cringe")

@client.command()
async def 
@client.command()
async def rule(ctx,*,number): 
    await ctx.send(rules[int(number)-1])




client.run("NzY5MjA4MTg1OTM1NjI2MzEx.X5Lq8g._Pk6q6eTTFhfm8ytfXE0398lpvc")

