import requests
import discord
from discord.ext import commands
import random
import json

headers = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',    
}

filename = "D:/Repos/AudioManiac-Bot/credentials.json"
class Youtube:
    key = ""
    def Init(self):
        if filename:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.key = data["ytkey"]
    def Search(self, query):
        try:
            finalQuery = query.lower()
            url = f"https://www.googleapis.com/youtube/v3/search?q={finalQuery}&part=snippet&type=video&maxResults=1&key={self.key}"
            downloadData = requests.get(url, headers=headers).text
            parser = json.loads(downloadData)
            videoId = parser["items"][0]["id"]["videoId"]
            totalResults = parser["pageInfo"]["totalResults"]
            title = parser["items"][0]["snippet"]["title"]
            url = "https://www.youtube.com/watch?v="+videoId


        
            finalOutput = f"""**{totalResults} items found for** "{query}" **on Youtube.**\n**Title:** {title}\n{url}"""
            return finalOutput
        except:
            return "No results found."
