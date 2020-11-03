from imports import *

#link to manage bot
#https://discord.com/developers/applications/773035122982387712/information

#establishes client for bot
client = commands.Bot(command_prefix = '.')

#create first event, readies the bot for use
@client.event
async def on_ready():
    print("Bot ready to go")

#run bot from token, DO NOT SHARE TOKEN
client.run(token)
time.sleep(6)