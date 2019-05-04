import discord
import json
from discogs import Discogs
from youtube import Youtube
from musicbrainz import musicBrainzSongSearch, musicBrainzArtistSearch
from discord.ext import commands
import random
import requests

discordToken = ""
filename = "D:/Repos/AudioManiac-Bot/credentials.json"

if filename:
    with open(filename, 'r') as f:
        data = json.load(f)
        discordToken = data["discordtoken"]

yt = Youtube()
yt.Init()

dscogs = Discogs()
dscogs.Init()

description = "An example bot to showcase the discord.ext.commands extension module."
bot = commands.Bot(command_prefix='?', description=description)
    
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def discogs(ctx, *queries):
    query = " ".join(queries)
    if "@everyone" in query:
        await ctx.send("Nice try, asshat.")
    else:
        message = dscogs.Search(query)
        await ctx.send(message)

@bot.command()
async def youtube(ctx, *queries):
    query = " ".join(queries)   
    if "@everyone" in query:
        await ctx.send("Nice try, asshat.")
    else:
        message = yt.Search(query)
        await ctx.send(message)

@bot.command()
async def musicbrainz(ctx, *queries):
    if(len(queries) >= 2):
        if(queries[0] == "release"):
            queryList = list(queries)
            del queryList[0]
            finalQuery = " ".join(queryList)
            if "@everyone" in finalQuery:
                await ctx.send("Nice try, asshat.")
            else:
                message = musicBrainzSongSearch(finalQuery)
                await ctx.send(message)
        elif(queries[0] == "artist"):
            queryList = list(queries)
            del queryList[0]
            finalQuery = " ".join(queryList)
            if "@everyone" in finalQuery:
                await ctx.send("Nice try, asshat.")
            else:
                message = musicBrainzArtistSearch(finalQuery)
                await ctx.send(message)
        else:
            await ctx.send("Invalid syntax.")



@bot.command()
async def shutdown(ctx):
    await bot.close()

bot.run(discordToken)
