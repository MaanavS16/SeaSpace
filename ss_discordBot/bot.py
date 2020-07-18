from dotenv import load_dotenv
import discord
import os
import random
from geolocation import Geolocate

load_dotenv('secrets.env')
discordToken = os.getenv('DISCORD_TOKEN')
geocodeToken = os.getenv('GEOCODE_TOKEN')

geolocator = Geolocate(geocodeToken = geocodeToken)
client = discord.Client()
commandKey = '#sea'

@client.event
async def on_ready():
    print("Bot Started")

@client.event
async def on_message(message):

    #prevent self-response
    if message.author == client.user:
        return

    # development command
    if 'end' in message.content.lower():
        await message.channel.send("Ok I will")
        exit()

    #detect commands
    if commandKey == message.content[0:len(commandKey)].lower():
        responseEmote = '\N{THUMBS UP SIGN}'


        if 'soothe' in message.content.lower():
            await message.channel.send("soothing")
            responseEmote = '\N{SLIGHTLY SMILING FACE}'
        elif 'spot' in message.content.lower() and message.content.lower():
            print(message.content.lower())
            try:
                searchLoc = message.content.lower()[(message.content.index("spot ") + 5):]
                await message.channel.send('`Searching location: {loc}`'.format(loc = searchLoc))
                res = geolocator.getCoordFromLoc(searchLoc)
                if res == 'error':
                    responseEmote = '😥'
                    await message.channel.send('`{loc} is not a recognized location`'.format(loc = searchLoc))
                else:
                    await message.channel.send('`The Coordinates for {loc} are longitude:{long} latitude:{lat}`'\
                    .format(loc = searchLoc, long=res[0], lat=res[1]))

                    if geolocator.isLand(*res):
                        await message.channel.send("```Oh no! It looks like you're on land: that's no fun\
                        \nI'll search for the nearest Ocean \N{SLIGHTLY SMILING FACE}```")

                        oceanCoords = geolocator.findClosestOcean(*res)
                        oceanName = geolocator.getLocFromCoord(*oceanCoords)
                        await message.channel.send("```The closest body of water I found is at longitude:{long} latitude:{lat}\
                        \nIt's close to {name} ```".format(long=oceanCoords[0], lat=oceanCoords[1], name=oceanName))

                        mapsLink = 'https://www.google.com/maps/dir/?api=1&destination={lat},{long}&dir_action=navigate'.format(lat=oceanCoords[1], long=oceanCoords[0])
                        await message.channel.send('Navigation Link: ' + mapsLink)
                    else:
                        await message.channel.send("```Awesome! You're ahead of the game and already at the ocean\
                        \nTry out #Sea Stats {24 hour time} {location} to learn more about where you are now.```")
            except:
                responseEmote = '😥'
                await message.channel.send('`Please use the format: #Sea Spot {Location}`')

        elif 'scene' in message.content.lower():
            pass
        else:
            responseEmote = '😥'
            await message.channel.send('```Command was not recognized. \
            \nEnter "#Sea help" for a full list of commands. \
            \nMore info can be found on: TheSea.Space```')

        await message.add_reaction(responseEmote)

    #await message.channel.send("Message")

client.run(discordToken)
