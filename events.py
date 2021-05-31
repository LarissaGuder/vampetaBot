import discord
import os
import random

from dotenv import load_dotenv
load_dotenv()

client = discord.Client()
TOKEN = os.getenv('TOKEN')
options = [
    "./dataset/v.jpg",
    "./dataset/va.jpg",
    "./dataset/vam.jpg",
    "./dataset/vamp.jpg",
    "./dataset/vampe.jpg",
    "./dataset/vampet.jpg",
    "./dataset/vampeta.jpg"
]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await message.author.send(file=discord.File(random.choice(options)))

client.run(TOKEN)