import requests
import discord
from discord.ext import commands
import random
import json
import discogs_client

headers = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',    
}


filename = "D:/Repos/AudioManiac-Bot/credentials.json"
class Discogs:
    d = None
    key = ""
    secret = ""
    token = ""
    def Init(self):
        if filename:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.key = data["discogskey"]
                self.secret = data["discogssecret"]
                self.token = data["discogstoken"]
                self.d = discogs_client.Client('Bot', user_token=self.token)

    def SearchRelease(self, query):
        #try:
        finalQuery = query.lower()
        results = self.d.search(finalQuery, type="release")
        artist = results[0].artists[0].name
        #country = results[0].country
        genre = results[0].genres[0]
        title = results[0].title
        year = results[0].year
        url = results[0].url
        trackCount = len(results[0].tracklist)
        label = results[0].labels[0].name
        items = results.count
        #print(results[0].artists[0].name)
        finalOutput = f"""**{items} items found for** "{query}" **on Discogs.**\n**Artist:** {artist}\n**Title:** {title}\n**Year:** {year}\n**Genre:** {genre}\n**Tracks:** {trackCount}\n**Label:** {label}\n{url}"""
        return finalOutput
        #except:
        #	return "No results found."
