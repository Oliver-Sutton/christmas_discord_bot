import discord
import asyncio

client = discord.Client()

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
    await client.send_message(channel, 'Hello, the Christmas Spirit is HERE!!', tts=True)


client.run('token')
