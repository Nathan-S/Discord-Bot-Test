# bot.py

import os
import discord
import asyncio
from dotenv import load_dotenv

load_dotenv()


TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_SERVER')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

#message that is printed when new users join
messageNewbies = """
Welcome to the server, I am just
trying out this bot so this message 
will eventually change. If you see 
this and you think I have forgotten
about it, send the owner a message.
"""

#@client.event
#async def on_member_join(member):
#    print(member.name + " joined the server!")
#    try:
#        await client.send_message(member, messageNewbies)
#    except:
#        print("Message wasn't sent to " + member.name)
#    embed=discord.Embed(
#        title="Hello " + member.name + "!",
#        description="Glad you could join le server!!!",
#        colour=discord.Color.red()
#        )#to add color, add color=discord.Color.'Insert color name here'()


#Starts an event with async, async means it'll basically sit around and wait for the events to happen
#on_message is the function thatwill pass in the message as a parameter
@client.event
async def on_message(message):
    if message.author == client.user: #if the author of the message is the bot, then it returns and waits for the next message
        return

    response = 'Did somebody say Game?' #variable that the bot will respond with 

    if message.content == 'Game?':
        await message.channel.send(response) #sends the response to the channel that the message was in


client.run(TOKEN)
