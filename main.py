import discord
import asyncio
import os
from random import randint

### TODO: http://apscheduler.readthedocs.io/en/3.3.1/userguide.html#code-examples ###

if not discord.opus.is_loaded():
    discord.opus.load_opus('opus.dll')

client = discord.Client()

class PlaySong:
    def __init__(self, bot):
        self.current = None
        self.voice = None
        self.bot = bot
        self.audio_player = self.bot.loop.create_task(self.audio_player_task())


    async def audio_player_task(self):
        while True:
            self.

def get_songs():
    url = './songs'
    songs = os.listdir(url)
    return songs

async def select_song(songs):
    song_index = randint(0, len(songs))
    song_name = songs[song_index]

    await client.send_message(channel, 'HoHoHo, today we playing {}'.format(song_name))

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

    songs = get_songs()
    await select_song(songs)

    # await client.send_message(channel, 'Hello, the Christmas Spirit is HERE!!')

client.run('token')
