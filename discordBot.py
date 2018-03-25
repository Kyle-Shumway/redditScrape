import discord
from discord.ext.commands import bot
from discord.ext import commands
from email.mime.text import MIMEText

redditFile = open("redditLog" , "r+")
steamFile = open("steamLog" , "r+")

Client = discord.client
bot_prefix = "?"
client = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))

@client.command(pass_context=True)
async def reddit(ctx):
    await client.say("Searching for reddit users!")
    lines = redditFile.readlines()
    for line in lines:
        print(line)
        await client.say(line)
        redditFile.truncate()

@client.command(pass_context=True)
async def steam(ctx):
    await client.say("Searching for steam users!")
    lines = steamFile.readlines()
    for line in lines:
        print(line)
        await client.say(line)
        steamFile.truncate()

client.run("CLIENT KEY")
