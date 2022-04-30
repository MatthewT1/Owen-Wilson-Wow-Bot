# Owen-Wilson-Wow-Bot

This is a simple Discord bot that uses the Owen Wilson API to reply to Discord messages with a random video. 

## Description

I saw the [Owen Wilson API](https://owen-wilson-wow-api.herokuapp.com/) on reddit today and thought it'd be fun to play around with. I'd also been wanting to test making a Discord bot, so I put two and two together to come up with this. 

The bot will respond to any message containing 'wow' with a random video of Owen Wilson saying "Wow". 

https://user-images.githubusercontent.com/5216489/166086208-9a51224a-af9e-44d4-9ee4-7fb07c5bbc06.mp4

## Getting Started

I followed [this tutorial](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/) , so its suggested to follow the steps there to make your own bot that runs this code. 

After you have a token change this line - 

client.run('')

to 

client.run('YOURTOKEN')

Then just run it with Python - I did this the lazy way with nohup(see [here](https://janakiev.com/blog/python-background/) for details), and I have it running on a cheap VPS. It overwrites the video file each time it grabs one, so space isn't really a concern. 

### Dependencies

* It should only need requests and discord.py
