import discord
import os
import re
import requests
import json

client = discord.Client()

#for storing temporary files
if not os.path.exists('/tmp/videos'):
    os.makedirs('/tmp/videos')

#Grabbed from Stackoverflow, not my function
def downloadFile(url, fileName):
    r = requests.get(url, stream=True)
    with open(fileName, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    return fileName

def getWow():
    owenData = requests.get('https://owen-wilson-wow-api.herokuapp.com/wows/random')
    owenJson = json.loads(owenData.text)
    lowQualityVidURI = owenJson[0]['video']['360p']
    videoPath = downloadFile(lowQualityVidURI, '/tmp/videos/wow.mp4')
    return videoPath

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    messageText = message.content.lower()
    if message.author == client.user:
        return

    if messageText.find("wow") != -1:
        async with message.channel.typing():
            wowVideo = getWow()
            await message.channel.send(
                content = '**WOW!**',
                file=discord.File(wowVideo),
                mention_author = True
            )
        #await message.channel.send("Wow!")

#put your token in below
client.run('')