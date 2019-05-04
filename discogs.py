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
class Discogs:
    key = ""
    secret = ""
    def Init(self):
        if filename:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.key = data["discogskey"]
                self.secret = data["discogssecret"]
    def Search(self, query):
        try:
            finalQuery = query.lower()
            url = f"https://api.discogs.com/database/search?q=\"{finalQuery}\"&key={self.key}&secret={self.secret}"
            downloadData = requests.get(url, headers=headers).text
    	
            parser = json.loads(downloadData)
            items = parser["pagination"]["items"]
            pages = parser["pagination"]["pages"]


            firstResultType = parser["results"][0]["type"]
            firstResultId = parser["results"][0]["id"]
            firstResultTitle = parser["results"][0]["title"]
            firstResultLink = "https://www.discogs.com"+parser["results"][0]["uri"]
            
            finalOutput = f"""**{items} items found for** "{query}" **on Discogs.**\n**Title:** {firstResultTitle}\n**Type:** {firstResultType}\n{firstResultLink}"""
            return finalOutput
        except:
        	return "No results found."
