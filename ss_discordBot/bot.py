from dotenv import load_dotenv
import discord
import os

load_dotenv('secrets.env')
Token = os.getenv('DISCORD_TOKEN')

client = discord.Client()
commandKey = '?Sea'

@client.event
async def on_ready():
    print("I'm alive papi")

@client.event
async def on_message(message):

    #prevent self-response
    if message.author == client.user:
        return

    if commandKey in message.content[0:len(commandKey)]:
        responseEmote = '\N{THUMBS UP SIGN}'

        await message.add_reaction(responseEmote)

    await message.channel.send("Message")

client.run(Token)
