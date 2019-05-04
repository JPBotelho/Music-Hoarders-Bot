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
        try:
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
            finalOutput = f"""**{items} releases found for** "{query}" **on Discogs.**\n**Artist:** {artist}\n**Title:** {title}\n**Year:** {year}\n**Genre:** {genre}\n**Tracks:** {trackCount}\n**Label:** {label}\n{url}"""
            return finalOutput
        except:
            return "Something went wrong."
    def SearchArtist(self, query):
        try:
            finalQuery = query.lower()
            results = self.d.search(finalQuery, type="artist")

            items = results.count
            name = results[0].name
            realName = results[0].real_name
            releaseCount = results[0].releases.count
            url = results[0].url
            finalOutput = f"""**{items} artists found for** "{query}" **on Discogs.**\n**Name:** {name}\n**Real Name:** {realName}\n**Releases:** {releaseCount}\n{url}"""
            return finalOutput
        except:
            return "Something went wrong."
