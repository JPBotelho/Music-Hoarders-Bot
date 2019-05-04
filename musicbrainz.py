import requests
import discord
from discord.ext import commands
import random
import json
import sys

headers = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',    
    'Music Hoarder\'s Discord bot': 'https://discord.gg/qYyxEM2'
}


def musicBrainzSongSearch(query):
    try:
        finalQuery = query.lower()
        #searchPage = f"https://musicbrainz.org/search?query={finalQuery}&type=release&limit=25&method=indexed"
        url = f"https://musicbrainz.org/ws/2/release?query={finalQuery}&limit=25&fmt=json"
        downloadData = requests.get(url, headers=headers).text
	
        parser = json.loads(downloadData)
        totalResults = parser["count"]
        title = parser["releases"][0]["title"]
        status = "?"
        artist = parser["releases"][0]["artist-credit"][0]["artist"]["name"]
        date = "?"
        try:
            date = parser["releases"][0]["date"]
            status = parser["releases"][0]["status"]
        except:
            pass
        trackCount = parser["releases"][0]["track-count"]
        discCount = parser["releases"][0]["media"][0]["disc-count"]
        
        releaseID = parser["releases"][0]["id"]
        releaseUrl = "https://musicbrainz.org/release/" + releaseID

        if(discCount == 0):
            discCount = 1
        print (releaseUrl)
        finalOutput = f"""**{totalResults} releases found for** "{query}" **on MusicBrainz.**\n**Title:** {title}\n**Artist:** {artist}\n**Status:** {status}\n**Released:** {date}\n\n**Disc Count:** {discCount}\n**Track count:** {trackCount}\n**Release URL:** {releaseUrl}"""
        return finalOutput
    except:
    	raise sys.exc_info()

def musicBrainzArtistSearch(query):
    try:
        finalQuery = query.lower()
        searchPage = f"https://musicbrainz.org/search?query={finalQuery}&type=artist&limit=25&method=indexed"
        url = f"https://musicbrainz.org/ws/2/artist?query={finalQuery}&limit=25&fmt=json"
        downloadData = requests.get(url, headers=headers).text
    
        parser = json.loads(downloadData)
        totalResults = parser["count"]
        name = parser["artists"][0]["name"]
        artistType = parser["artists"][0]["type"]
        gender = "?"
        born = "?"
        died = "?"

        try:
            gender = parser["artists"][0]["gender"]
            born = parser["artists"][0]["life-span"]["begin"].capitalize()
            died = parser["artists"][0]["life-span"]["ended"]
        except:
            pass
        
        if(died == None): died = "Alive"

        #Release information needs another request
        artistID = parser["artists"][0]["id"]
        artistURL = f"https://musicbrainz.org/ws/2/release?artist={artistID}&fmt=json"
        artistData = requests.get(artistURL, headers=headers).text
        artistParser = json.loads(artistData)
        releaseCount = artistParser["release-count"]


        artistPage = "https://musicbrainz.org/artist/"+artistID
        
        finalOutput = f"""{totalResults} results found for "**{query}**" on MusicBrainz.\n**Name:** {name}\n**Type:** {artistType}\n**Gender:** {gender}\n**Born:** {born}\n**Died:** {died}\n**Releases:** {releaseCount}\n\n**Artist page:** {artistPage}"""
        return finalOutput
    except:
        raise sys.exc_info()
