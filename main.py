import discord
import asyncio
import os

### TODO: http://apscheduler.readthedocs.io/en/3.3.1/userguide.html#code-examples ###

client = discord.Client()

def get_song():
    url = './songs'
    songs = os.listdir(url)
    print(songs)

@client.event
async def on_ready():
    print('''
                                            ----------------------------
                                            Starting Above Christmas Bot
                                            ----------------------------
        ''')
    print('''
                                     Logged in as {} {}
        '''.format(client.user.name, client.user.id))

    channel = discord.utils.get(client.get_all_channels())
    get_song()
    # await client.send_message(channel, 'Hello, the Christmas Spirit is HERE!!')

client.run('token')
