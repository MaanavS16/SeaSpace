from dotenv import load_dotenv
import discord
import os
import random
from geolocation import Geolocate
from stats import Stats
from convert import Converter
from animal import Predictor


load_dotenv('secrets.env')
discordToken = os.getenv('DISCORD_TOKEN')
geocodeToken = os.getenv('GEOCODE_TOKEN')
statPassword = os.getenv('METEOMATICS_PASSWORD')
statUsername = os.getenv('METEOMATICS_USERNAME')

animalPredictor = Predictor()
geolocator = Geolocate(geocodeToken = geocodeToken)
statloader = Stats(username=statUsername, password=statPassword)
converter = Converter()
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


    # check images for aquatic animals
    if len(message.attachments) > 0:
        imgURL = message.attachments[0].url
        print(imgURL)
        preds = animalPredictor.predictPic(imgURL)
        await message.channel.send('`Hey that looks like a {pred}!`'.\
        format(pred = preds.replace('_', ' ')))
        message.add_reaction('\N{THUMBS UP SIGN}')


    #detect commands
    if commandKey == message.content[0:len(commandKey)].lower():
        responseEmote = '\N{THUMBS UP SIGN}'


        if 'spot' in message.content.lower() and message.content.lower():
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

                        mapsLink = 'https://www.google.com/maps/dir/?api=1&destination={lat},{long}&dir_action=navigate'\
                        .format(lat=oceanCoords[1], long=oceanCoords[0])

                        await message.channel.send('Navigation Link: ' + mapsLink)
                    else:
                        await message.channel.send("```Awesome! You're ahead of the game and already at the ocean\
                        \nTry out #Sea Stats {24 hour time} {location} to learn more about where you are now.```")
            except:
                responseEmote = '😥'
                await message.channel.send('`Please use the format: #Sea Spot {Location}`')


        elif 'size' in message.content.lower():
            print(message.content.lower())
            try:
                content = message.content.lower()[(message.content.index("size ") + 5):].split()
                converted = converter.convert(content[0], content[1])
                await message.channel.send('` The ocean is {:,} {unit}s `'.format(converted, unit=content[1]))
                print(content)
            except:
                responseEmote = '😥'
                await message.channel.send('`Please use the format: #Sea Size {metric} {unit}`')
        elif 'stats' in message.content.lower():
            print(message.content.lower())
            try:
                content = message.content.lower()[(message.content.index("stats ") + 6):].split()
                # x, y = geolocator.getCoordFromLoc(" ".join(content[1:]))
                x, y = content[1], content[2]

                if content[0] == "temp":
                    metric = statloader.get_temp(x, y)
                    print("Metric is", metric)
                    await message.channel.send('`The ocean temperature is {metric} degrees Celsius at this location: coordinates {y} degrees latitude, {x} degrees longitude`'.format(metric = metric, x = x, y = y))
                elif content[0] == "salinity":
                    metric = statloader.get_salinity(x, y)
                    await message.channel.send('`The ocean salinity is {metric} psu at this location: coordinates {y} degrees latitude, {x} degrees longitude`'.format(metric = metric, x = x, y = y))
                elif content[0] == "depth":
                    metric = statloader.get_depth(x, y)
                    await message.channel.send('`The ocean depth is {metric} km at this location: coordinates {y} degrees latitude, {x} degrees longitude`'.format(metric = metric, x = x, y = y))
                elif content[0] == "temp_pic":
                    print("getting pic")
                    statloader.get_temp_pic(x, y)
                    print("got pic")
                    await message.channel.send(file = discord.File('temp_pic.png'))
            except:
                responseEmote = '😥'
                await message.channel.send('`Please use the format: #Sea Stats {metric} {x} {y} `')
        elif 'help' in message.content.lower():
            await message.channel.send(
            "Commands: \n"
            "#sea spot {location}  : Plays Aarush's Playlist. Can only be utilized by everyone \n"
            "#sea size  : Enables custom messages. Can only be utilized by Powerplant \n"
            "#sea stats  : Disables custom messages. Can only be utilized by Powerplant \n"
            )

        else:
            responseEmote = '😥'
            await message.channel.send('```Command was not recognized. \
            \nEnter "#Sea help" for a full list of commands. \
            \nMore info can be found on: TheSea.Space```')

        await message.add_reaction(responseEmote)

    #await message.channel.send("Message")
client.run(discordToken)
