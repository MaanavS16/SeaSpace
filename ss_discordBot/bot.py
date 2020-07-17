from dotenv import load_dotenv
import discord
import os

load_dotenv('secrets.env')
Token = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print("I'm alive papi")
